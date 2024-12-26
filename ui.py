import matplotlib.pyplot as plt

def plot_environment(depot_coordinates, task_coordinates, solution, title="Solution Visualization", best_cost=None, initial_cost=None):

    plt.figure(figsize=(10, 10))

    for i, depot in enumerate(depot_coordinates):
        plt.scatter(depot[0], depot[1], c='red', label=f"Depot" if i == 0 else None, s=100, marker='s')

    for task in task_coordinates:
        plt.scatter(task[0], task[1], c='blue', label="Task" if task == task_coordinates[0] else None, s=50)

    for depot_idx, tasks in enumerate(solution):
        depot = depot_coordinates[depot_idx]
        route = [depot] + tasks + [depot]
        x_coords, y_coords = zip(*route)
        plt.plot(x_coords, y_coords, label=f"Route {depot_idx+1}")

    if best_cost is not None:
        plt.text(0.05, 0.95, f"Best Cost: {best_cost:.2f}", transform=plt.gca().transAxes, fontsize=12, color='green', verticalalignment='top')
    if initial_cost is not None:
        plt.text(0.05, 0.90, f"Initial Cost: {initial_cost:.2f}", transform=plt.gca().transAxes, fontsize=12, color='blue', verticalalignment='top')

    plt.title(title)
    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")
    plt.legend()
    plt.grid(True)
    plt.show()