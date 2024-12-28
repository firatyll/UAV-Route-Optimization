from ui import plot_environment
from utils import *
from simulatedAnnealing import *

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