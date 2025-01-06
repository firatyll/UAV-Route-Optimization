from utils import * 
import numpy as np

CROSSOVER_RATE  = 0.9
MUTATION_RATE = 0.15
POPULATION_SIZE = 100
TOURNEMENT_SIZE = 4

def applyCrossover(solution):

    neighbor_solution = None
    while neighbor_solution is None:
        neighbor_solution = [list(routes) for routes in solution]
        method = np.random.choice(['singlePoint', 'multiPoint','uniform'])
        depot1, depot2 = np.random.choice(len(neighbor_solution), 2, replace=False)

        if len(neighbor_solution[depot1]) < 3 and len(neighbor_solution[depot2]) < 3:
            neighbor_solution= None
            continue

        if method == 'singlePoint':
            crossover_point = np.random.randint(1, min(len(neighbor_solution[depot1]), len(neighbor_solution[depot2])) - 1)

            new_depot1 = (
                [neighbor_solution[depot1][0]] + 
                neighbor_solution[depot1][1:crossover_point] +
                neighbor_solution[depot2][crossover_point:-1] +
                [neighbor_solution[depot1][-1]]
            )
            new_depot2 = (
                [neighbor_solution[depot2][0]] + 
                neighbor_solution[depot2][1:crossover_point] +
                neighbor_solution[depot1][crossover_point:-1] +
                [neighbor_solution[depot2][-1]]
            )
            neighbor_solution[depot1] = new_depot1
            neighbor_solution[depot2] = new_depot2


        if method == 'multiPoint':

            min_len = min(len(neighbor_solution[depot1]), len(neighbor_solution[depot2]))
            if min_len < 3:
                neighbor_solution = None
                continue
            else:
                top_val = min_len // 2
            if top_val < 2:
                neighbor_solution = None
                continue
            else:
                num_points = np.random.randint(2, top_val + 1)  
                crossover_points = sorted(np.random.choice(range(1, min_len - 1), num_points, replace=False))

                new_depot1 = neighbor_solution[depot1][:]
                new_depot2 = neighbor_solution[depot2][:]

                for i in range(len(crossover_points)):
                    start = crossover_points[i]
                    end = crossover_points[i+1] if (i+1 < len(crossover_points)) else -1
                    new_depot1[start:end], new_depot2[start:end] = new_depot2[start:end], new_depot1[start:end]

                neighbor_solution[depot1] = (
                    [neighbor_solution[depot1][0]] +
                    new_depot1[1:-1] +
                    [neighbor_solution[depot1][-1]]
                )
                neighbor_solution[depot2] = (
                    [neighbor_solution[depot2][0]] +
                    new_depot2[1:-1] +
                    [neighbor_solution[depot2][-1]]
                )

        if method == 'uniform':

            new_depot1, new_depot2 = neighbor_solution[depot1][:], neighbor_solution[depot2][:]

            for i in range(1, min(len(new_depot1), len(new_depot2)) - 1):
                if np.random.rand() < 0.5:
                    new_depot1[i], new_depot2[i] = new_depot2[i], new_depot1[i]

            neighbor_solution[depot1] = (
                [neighbor_solution[depot1][0]] +
                new_depot1[1:-1] +
                [neighbor_solution[depot1][-1]]
            )
            neighbor_solution[depot2] = (
                [neighbor_solution[depot2][0]] +
                new_depot2[1:-1] +
                [neighbor_solution[depot2][-1]]
            )

    return neighbor_solution

def selection(fitness_values):
    population_size = len(fitness_values)
    candidates = np.random.choice(range(population_size), TOURNEMENT_SIZE, replace=False)
    best_idx = candidates[0]
    for canditate in candidates:
        if fitness_values[canditate] < fitness_values[best_idx]:
            best_idx = canditate
    return best_idx

def mutate(solution):

    mutated_solution = [route[:] for route in solution]
    depot_idx = np.random.randint(len(mutated_solution))
    route = mutated_solution[depot_idx]

    if len(route) <= 3:
        return mutated_solution

    i, j = np.random.choice(range(1, len(route)-1), 2, replace=False)
    
    route[i], route[j] = route[j], route[i]
    mutated_solution[depot_idx] = route

    return mutated_solution


def geneticAlgorithm(task_list, depot_list):

    population = []
    for _ in range(POPULATION_SIZE):
        population.append(generateInitialSolution(task_list, depot_list))
    fitness_values = [calculateTotalCost(individual , depot_list) for individual in population]

    best_index = np.argmin(fitness_values)
    best_cost = fitness_values[best_index]
    best_solution = population[best_index]

    for iteration in range(ITERATION_COUNT):
        new_population = []

        for _ in range(POPULATION_SIZE // 2):

            parent1, parent2 = None,None

            while parent1 == parent2:
                parent1 = population[selection(fitness_values)]
                parent2 = population[selection(fitness_values)]

            if np.random.rand() < CROSSOVER_RATE:

                offspring1 = applyCrossover(parent1)
                offspring2 = applyCrossover(parent2)

            else:
                offspring1 = parent1[:]
                offspring2 = parent2[:]

            if np.random.rand() < MUTATION_RATE:
                offspring1 = mutate(offspring1)
            if np.random.rand() < MUTATION_RATE:
                offspring2 = mutate(offspring2)
            new_population.append(offspring1)
            new_population.append(offspring2)

        new_fitness_values = [calculateTotalCost(individual , depot_list) for individual in new_population]

        local_best_index = np.argmin(new_fitness_values)
        local_best_cost  = new_fitness_values[local_best_index]

        if local_best_cost < best_cost:
            best_cost = local_best_cost
            best_solution = new_population[local_best_index]

        population = new_population
        fitness_values = new_fitness_values

        if iteration % 100 == 0 or iteration == ITERATION_COUNT - 1:
            print(f"Iteration: {iteration}, Best Cost: {best_cost}")
    
    return best_solution, best_cost
