import numpy as np
from math import sqrt

FIELD_AREA = 5000
DEPOT_COUNT = 4
TASK_COUNT = 20
TASK_COORDINATES = set()
DEPOT_COORDINATES = set()
UAV_COUNT = DEPOT_COUNT
UAV_SPEED = 27
ITERATION_COUNT = 1000
UAV_CAPACITY = TASK_COUNT // UAV_COUNT + 1
DEPOT_ALTITUDE = 0
CRUISE_ALTITUDE = 3000
TASK_ALTITUDE = 1500

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

    horizontal_distance= sqrt((pointX[0] - pointY[0])**2 + (pointX[1] - pointY[1])**2)
    vetrical_distance_to_depot = TASK_ALTITUDE - DEPOT_ALTITUDE
    vertical_distance_to_cruise = CRUISE_ALTITUDE - TASK_ALTITUDE

    if pointX in DEPOT_COORDINATES or pointY in DEPOT_COORDINATES:
        return sqrt(vetrical_distance_to_depot**2 + horizontal_distance**2)

    if horizontal_distance > 2*vertical_distance_to_cruise:
        horizontal_distance = horizontal_distance - 2*vertical_distance_to_cruise
        distance_to_top_of_climb = vertical_distance_to_cruise*sqrt(2)
        distance_from_top_of_descend = distance_to_top_of_climb
        horizontal_distance = distance_to_top_of_climb + horizontal_distance + distance_from_top_of_descend
        return horizontal_distance

    if horizontal_distance <= 2*vertical_distance_to_cruise:
        return 2 * ((horizontal_distance / 2) * sqrt(2))

    return horizontal_distance

def generateInitialSolution(task_list, depot_list):
    task_assignments = [[] for _ in range(DEPOT_COUNT)]

    for i in range(DEPOT_COUNT):
        task_assignments[i].append(depot_list[i])

    for task in task_list:
        while True:
            assigned_depot = np.random.randint(0, DEPOT_COUNT)
            if len(task_assignments[assigned_depot]) - 2 < UAV_CAPACITY:
                task_assignments[assigned_depot].append(task)
                break

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
                if len(neighbor_solution[depot1]) - 2 < UAV_CAPACITY and len(neighbor_solution[depot2]) - 2 < UAV_CAPACITY:
                    neighbor_solution[depot1].insert(task1_index, task2)
                    neighbor_solution[depot2].insert(task2_index, task1)
                else:
                    neighbor_solution = None

        elif method == 'relocateTask':
            depot1, depot2 = np.random.choice(len(neighbor_solution), 2, replace=False)

            if len(neighbor_solution[depot1]) > 3:
                task_index = np.random.randint(1, len(neighbor_solution[depot1]) - 1)
                task = neighbor_solution[depot1].pop(task_index)
                if len(neighbor_solution[depot2]) - 2 < UAV_CAPACITY:
                    insert_index = np.random.randint(1, len(neighbor_solution[depot2]))
                    neighbor_solution[depot2].insert(insert_index, task)
                else:
                    neighbor_solution = None

    return neighbor_solution

def calculateTime(cost):
    return cost/UAV_SPEED