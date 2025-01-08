from utils import * 
import numpy as np
import copy
from collections import Counter

CROSSOVER_RATE  = 0.9
MUTATION_RATE = 0.15
POPULATION_SIZE = 100
TOURNEMENT_SIZE = 4
MAX_ATTEMPTS = 50


def repairSolution(solution, task_list, depot_list):    

    all_routes_tasks = [] 
    route_task_lists = []

    for route_idx, route in enumerate(solution):
        internal = route[1:-1]
        route_task_lists.append(list(internal))
        all_routes_tasks.extend(internal)

    task_counter = Counter(all_routes_tasks)
    
    for route_idx in range(len(route_task_lists)):
        i = 0
        while i < len(route_task_lists[route_idx]):
            task = route_task_lists[route_idx][i]
            if task_counter[task] > 1:
                route_task_lists[route_idx].pop(i)
                task_counter[task] -= 1
            else:
                i += 1

    all_routes_tasks = []
    for tlist in route_task_lists:
        all_routes_tasks.extend(tlist)

    missing_tasks = set(task_list) - set(all_routes_tasks)

    for mtask in missing_tasks:
        for route_idx in range(len(route_task_lists)):
            if len(route_task_lists[route_idx]) < UAV_CAPACITY - 1:  
                route_task_lists[route_idx].append(mtask)
                break
        else:
            route_task_lists[-1].append(mtask)

    for route_idx in range(len(route_task_lists)):
        while len(route_task_lists[route_idx]) > (UAV_CAPACITY - 1):
            moved_task = route_task_lists[route_idx].pop()
            placed = False
            for other_idx in range(len(route_task_lists)):
                if other_idx == route_idx:
                    continue
                if len(route_task_lists[other_idx]) < (UAV_CAPACITY - 1):
                    route_task_lists[other_idx].append(moved_task)
                    placed = True
                    break
            if not placed:
                route_task_lists[-1].append(moved_task)

    repaired_solution = []
    for idx in range(len(route_task_lists)):
        depot = depot_list[idx]
        new_route = [depot] + route_task_lists[idx] + [depot]
        repaired_solution.append(new_route)

    return repaired_solution


def internal_nodes(route):
    return route[1:-1]

def applyCrossover(parent_1, parent_2):

    offspring_1 = None
    offspring_2 = None
    iteration = 0

    while offspring_1 is None or offspring_2 is None:

        iteration += 1
        if iteration == MAX_ATTEMPTS:
            return parent_1 , parent_2

        offspring_1 = copy.deepcopy(parent_1)
        offspring_2 = copy.deepcopy(parent_2)
        
        depot1 = np.random.choice(len(offspring_1))
        depot2 = np.random.choice(len(offspring_2))

        if len(offspring_1[depot1]) < 3 or len(offspring_2[depot2]) < 3:
            offspring_1, offspring_2 = None, None
            continue

        if set(internal_nodes(offspring_1[depot1])).intersection(set(internal_nodes(offspring_2[depot2]))):
            offspring_1, offspring_2 = None, None
            continue
        
        method = np.random.choice(['singlePoint' , 'multiPoint' , 'uniform'])

        if method == 'singlePoint':
            crossover_point = np.random.randint(1, min(len(offspring_1[depot1]), len(offspring_2[depot2])) - 1)

            new_depot1 = (
                [offspring_1[depot1][0]] + 
                offspring_1[depot1][1:crossover_point] +
                offspring_2[depot2][crossover_point:-1] +
                [offspring_1[depot1][-1]]
            )
            new_depot2 = (
                [offspring_2[depot2][0]] + 
                offspring_2[depot2][1:crossover_point] +
                offspring_1[depot1][crossover_point:-1] +
                [offspring_2[depot2][-1]]
            )
            offspring_1[depot1] = new_depot1
            offspring_2[depot2] = new_depot2

        if method == 'multiPoint':

            min_len = min(len(offspring_1[depot1]), len(offspring_2[depot2]))
            if min_len < 3:
                offspring_1, offspring_2 = None, None
                continue
            else:
                top_val = min_len // 2
            if top_val < 2:
                offspring_1, offspring_2 = None, None
                continue
            else:
                num_points = np.random.randint(2, top_val + 1)  
                crossover_points = sorted(np.random.choice(range(1, min_len - 1), num_points, replace=False))

                new_depot1 = offspring_1[depot1][:]
                new_depot2 = offspring_2[depot2][:]

                for i in range(len(crossover_points)):
                    start = crossover_points[i]
                    end = crossover_points[i+1] if (i+1 < len(crossover_points)) else -1
                    new_depot1[start:end], new_depot2[start:end] = new_depot2[start:end], new_depot1[start:end]

                offspring_1[depot1] = (
                    [offspring_1[depot1][0]] +
                    new_depot1[1:-1] +
                    [offspring_1[depot1][-1]]
                )
                offspring_2[depot2] = (
                    [offspring_2[depot2][0]] +
                    new_depot2[1:-1] +
                    [offspring_2[depot2][-1]]
                )

        if method == 'uniform':

            new_depot1, new_depot2 = offspring_1[depot1][:], offspring_2[depot2][:]

            for i in range(1, min(len(new_depot1), len(new_depot2)) - 1):
                if np.random.rand() < 0.5:
                    new_depot1[i], new_depot2[i] = new_depot2[i], new_depot1[i]

            offspring_1[depot1] = (
                [offspring_1[depot1][0]] +
                new_depot1[1:-1] +
                [offspring_1[depot1][-1]]
            )
            offspring_2[depot2] = (
                [offspring_2[depot2][0]] +
                new_depot2[1:-1] +
                [offspring_2[depot2][-1]]
            )

    return offspring_1, offspring_2

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
                offspring1, offspring2 = applyCrossover(parent1, parent2)
                offspring1 = repairSolution(offspring1,task_list,depot_list)
                offspring2 = repairSolution(offspring2,task_list,depot_list)

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

        best_old_idx = np.argmin(fitness_values)
        best_old_solution = population[best_old_idx]
        best_old_cost = fitness_values[best_old_idx]

        worst_new_idx = np.argmax(new_fitness_values)

        new_population[worst_new_idx] = best_old_solution
        new_fitness_values[worst_new_idx] = best_old_cost

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
