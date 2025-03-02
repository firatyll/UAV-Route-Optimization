import numpy as np
import random
from utils import *

NUM_ANTS = 20
ALPHA = 1.0
BETA = 2.0
RHO = 0.7
Q = 500.0
EPSILON = 0.1

def initialize_pheromone_trails(task_list, depot_list):
    num_nodes = len(task_list) + len(depot_list)
    pheromone_matrix = np.ones((num_nodes, num_nodes)) * 0.1
    np.fill_diagonal(pheromone_matrix, 0)
    return pheromone_matrix

def select_next_node(current_node, unvisited_tasks, pheromone_trails, task_list, depot_list):
    if not unvisited_tasks:
        return None
    if np.random.rand() < EPSILON:
        return random.choice(list(unvisited_tasks))
    
    all_nodes = task_list + depot_list
    probabilities = []
    denominator = 0.0
    
    for node in unvisited_tasks:
        distance = calculateDistance(all_nodes[current_node], all_nodes[node])
        distance = max(distance, 0.0001)
        
        pheromone = pheromone_trails[current_node][node]
        attractiveness = (pheromone ** ALPHA) * ((1.0 / distance) ** BETA)
        probabilities.append(attractiveness)
        denominator += attractiveness
    
    probabilities = [p / denominator for p in probabilities] if denominator > 0 else [1.0 / len(unvisited_tasks)] * len(unvisited_tasks)
    return np.random.choice(list(unvisited_tasks), p=probabilities)

def update_pheromone_trails(pheromone_trails, ant_solutions, ant_costs, task_list, depot_list):
    pheromone_trails *= (1 - RHO)
    all_nodes = task_list + depot_list
    
    for solution, cost in zip(ant_solutions, ant_costs):
        if cost > 0:
            deposit = Q / cost
            for path in solution:
                for i in range(len(path) - 1):
                    from_idx = all_nodes.index(path[i])
                    to_idx = all_nodes.index(path[i + 1])
                    pheromone_trails[from_idx][to_idx] += deposit
                    pheromone_trails[to_idx][from_idx] += deposit
    
    return pheromone_trails

def antColony(task_list, depot_list, initial_solution):
    best_solution = initial_solution.copy()
    best_cost = calculateTotalCost(best_solution, depot_list)
    pheromone_trails = initialize_pheromone_trails(task_list, depot_list)
    
    for iteration in range(ITERATION_COUNT):
        ant_colony = []
        
        for _ in range(NUM_ANTS):
            ant_solution = []
            unvisited_tasks = set(range(len(task_list)))
            
            flag = True 
            assignment = []
            while flag:
                assignment = [np.random.randint(2, UAV_CAPACITY) for _ in range(len(depot_list)-1)]
                last_assignment = len(task_list) - sum(assignment)
                assignment.append(last_assignment)
                if all(2 <= tasks <= UAV_CAPACITY for tasks in assignment):
                    flag = False
            
            for depot_idx, depot in enumerate(depot_list):
                path = [depot]
                current_node = len(task_list) + depot_idx
                tasks_to_assign = assignment[depot_idx]
                
                for _ in range(tasks_to_assign):
                    next_node = select_next_node(current_node, unvisited_tasks, pheromone_trails, task_list, depot_list)
                    if next_node is None:
                        break
                    path.append(task_list[next_node])
                    unvisited_tasks.remove(next_node)
                    current_node = next_node
                
                path.append(depot)
                ant_solution.append(path)
            
            ant_colony.append((ant_solution, calculateTotalCost(ant_solution, depot_list)))
        
        ant_solutions = [solution for solution, _ in ant_colony]
        ant_costs = [cost for _, cost in ant_colony]
        
        min_cost_idx = np.argmin(ant_costs)
        if ant_costs[min_cost_idx] < best_cost:
            best_solution = ant_solutions[min_cost_idx]
            best_cost = ant_costs[min_cost_idx]
        
        if iteration % 100 == 0:
            print(f"Iteration {iteration}: Best cost = {best_cost}")
        
        pheromone_trails = update_pheromone_trails(pheromone_trails, ant_solutions, ant_costs, task_list, depot_list)
    
    print(f"Final best cost = {best_cost}")
    return best_solution, best_cost