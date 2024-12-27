import numpy as np
from math import sqrt
from ui import plot_environment

FIELD_AREA = 5000
DEPOT_COUNT = 4
TASK_COUNT = 20
TASK_COORDINATES = set()
DEPOT_COORDINATES = set()
UAV_COUNT = DEPOT_COUNT
UAV_SPEED = 27
INITIAL_TEMP = 1000
COOLING_RATE = 0.95
ITERATION_COUNT = 1000

def initializeEnvironment():
    while len(TASK_COORDINATES) < TASK_COUNT:
        x = np.random.randint(0, FIELD_AREA)
        y = np.random.randint(0, FIELD_AREA)
        TASK_COORDINATES.add((x, y))

    while len(DEPOT_COORDINATES) < DEPOT_COUNT:
        x = np.random.randint(0, FIELD_AREA)
        y = np.random.randint(0, FIELD_AREA)
        DEPOT_COORDINATES.add((x, y))

def calculateDistance(pointX, pointY):
    return sqrt((pointX[0] - pointY[0])**2 + (pointX[1] - pointY[1])**2)

def generateInitialSolution(task_list, depot_list):
    task_assignments = [[] for _ in range(DEPOT_COUNT)]

    for i in range(DEPOT_COUNT):
        task_assignments[i].append(depot_list[i])

    for task in task_list:
        assigned_depot = np.random.randint(0, DEPOT_COUNT)
        task_assignments[assigned_depot].append(task)

    for i in range(DEPOT_COUNT):
        task_assignments[i].append(depot_list[i])

    return task_assignments

def calculateTotalCost(solution, depot_list):
    total_cost = 0
    for i, tasks in enumerate(solution):
        depot = depot_list[i]
        current_point = depot
        for task in tasks:
            total_cost += calculateDistance(current_point, task)
            current_point = task
        total_cost += calculateDistance(current_point, depot)
    return total_cost

def generateNeighbor(solution):
    neighbor_solution = None
    while neighbor_solution is None:
        neighbor_solution = [list(tasks) for tasks in solution]

        method = np.random.choice(['swapTasks', 'relocateTask'])

        if method == 'swapTasks':
            depot1, depot2 = np.random.choice(len(neighbor_solution), 2, replace=False)

            if len(neighbor_solution[depot1]) > 3 and len(neighbor_solution[depot2]) > 3:
                task1_index = np.random.randint(1, len(neighbor_solution[depot1]) - 1)
                task2_index = np.random.randint(1, len(neighbor_solution[depot2]) - 1)

                task1 = neighbor_solution[depot1].pop(task1_index)
                task2 = neighbor_solution[depot2].pop(task2_index)
                neighbor_solution[depot1].insert(task1_index, task2)
                neighbor_solution[depot2].insert(task2_index, task1)
            else:
                neighbor_solution = None

        elif method == 'relocateTask':
            depot1, depot2 = np.random.choice(len(neighbor_solution), 2, replace=False)

            if len(neighbor_solution[depot1]) > 3:
                task_index = np.random.randint(1, len(neighbor_solution[depot1]) - 1)
                task = neighbor_solution[depot1].pop(task_index)
                insert_index = np.random.randint(1, len(neighbor_solution[depot2]))
                neighbor_solution[depot2].insert(insert_index, task)
            else:
                neighbor_solution = None

    return neighbor_solution

def simulatedAnnealing(depot_list, initial_solution, initial_cost, INITIAL_TEMP, COOLING_RATE, ITERATION_COUNT):
    current_solution = initial_solution
    current_cost = initial_cost

    best_solution = current_solution
    best_cost = current_cost

    temp = INITIAL_TEMP

    for iteration in range(ITERATION_COUNT):
        neighbor_solution = generateNeighbor(current_solution)
        neighbor_cost = calculateTotalCost(neighbor_solution, depot_list)

        delta_cost = neighbor_cost - current_cost
        if delta_cost < 0 or np.random.rand() < np.exp(-delta_cost / temp):
            current_solution = neighbor_solution
            current_cost = neighbor_cost

        if current_cost < best_cost:
            best_solution = current_solution
            best_cost = current_cost

        temp = temp*COOLING_RATE
        if iteration % 100 == 0 or iteration==ITERATION_COUNT-1:
            print(f"Iteration {iteration}, Current Cost: {current_cost}, Best Cost: {best_cost}, Temperature: {temp}")

    return best_solution, best_cost

def calculateTime(cost):
    return cost/UAV_SPEED

def main():
    initializeEnvironment()
    depot_list = list(DEPOT_COORDINATES)
    task_list = list(TASK_COORDINATES)
    initial_solution = generateInitialSolution(task_list, depot_list)
    initial_cost = calculateTotalCost(initial_solution, depot_list)
    best_solution, best_cost = simulatedAnnealing(depot_list, initial_solution, initial_cost, INITIAL_TEMP, COOLING_RATE, ITERATION_COUNT)

    print("Best Solution")
    for sol in best_solution:
        print(sol)
    print("---")
    print("Best Cost:", best_cost)
    print("Total Time:", calculateTime(best_cost) , "Seconds")

    plot_environment(depot_list, task_list, initial_solution, best_solution, title="Simulated Annealing Solution", best_cost=best_cost, initial_cost=initial_cost)


main()
