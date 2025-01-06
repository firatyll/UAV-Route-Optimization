from ui import plot_environment
from utils import *
from simulatedAnnealing import *
from geneticAlgorithm import *

def main():
    initializeEnvironment()
    depot_list = list(DEPOT_COORDINATES)
    task_list = list(TASK_COORDINATES)
    initial_solution = generateInitialSolution(task_list, depot_list)
    initial_cost = calculateTotalCost(initial_solution, depot_list)
    simulated_annealing_best_solution, simulated_annealing_best_cost = simulatedAnnealing(depot_list, initial_solution, initial_cost)
    genetic_best_solution, genetic_best_cost = geneticAlgorithm(task_list, depot_list) 

    plot_environment(depot_list, task_list, initial_solution, simulated_annealing_best_solution, calculateTime, title="Simulated Annealing Solution", best_cost=simulated_annealing_best_cost, initial_cost=initial_cost)
    plot_environment(depot_list, task_list, initial_solution, genetic_best_solution, calculateTime, title="Genetic Algorithm Solution", best_cost=genetic_best_cost, initial_cost=initial_cost)

main()