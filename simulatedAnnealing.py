import numpy as np
from utils import *

INITIAL_TEMP = 1000
COOLING_RATE = 0.95

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