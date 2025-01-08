from ui import plot_environment
from utils import *
from simulatedAnnealing import *
from geneticAlgorithm import *

def main():
    initializeEnvironment()
    # depot_list = list(DEPOT_COORDINATES)
    depot_list = [(4953, 877), (889, 2279), (1372, 2028), (1297, 1768)]
    # task_list = list(TASK_COORDINATES)
    task_list = [(3856, 3831), (4209, 2231), (1005, 604), (274, 4644), (4382, 2253), (343, 3279), (4876, 2377), (4477, 193), (4877, 2369), (2476, 1987), (2181, 3900), (1691, 2648), (385, 3967), (3855, 2678), (209, 3872), (4642, 4753), (2289, 561), (2706, 1258), (155, 1240), (617, 4965)]
    initial_solution = generateInitialSolution(task_list, depot_list)
    initial_cost = calculateTotalCost(initial_solution, depot_list)
    simulated_annealing_best_solution, simulated_annealing_best_cost = simulatedAnnealing(depot_list, initial_solution, initial_cost)
    genetic_best_solution, genetic_best_cost = geneticAlgorithm(task_list, depot_list) 

    plot_environment(depot_list, task_list, initial_solution, simulated_annealing_best_solution, calculateTime, title="Simulated Annealing Solution", best_cost=simulated_annealing_best_cost, initial_cost=initial_cost)
    plot_environment(depot_list, task_list, initial_solution, genetic_best_solution, calculateTime, title="Genetic Algorithm Solution", best_cost=genetic_best_cost, initial_cost=initial_cost)

main()