import matplotlib.pyplot as plt

def plot_environment(depot_coordinates, task_coordinates, initial_solution, best_solution, calculateTime, title="Solution Visualization", best_cost=None, initial_cost=None):

    fig, axs = plt.subplots(1, 2, figsize=(20, 10))

    axs[0].set_title("Initial Solution")
    for i, depot in enumerate(depot_coordinates):
        axs[0].scatter(depot[0], depot[1], c='red', label=f"Depot" if i == 0 else None, s=100, marker='s')

    for task in task_coordinates:
        axs[0].scatter(task[0], task[1], c='blue', label="Task" if task == task_coordinates[0] else None, s=50)

    for depot_idx, tasks in enumerate(initial_solution):
        depot = depot_coordinates[depot_idx]
        route = [depot] + tasks + [depot]
        x_coords, y_coords = zip(*route)
        axs[0].plot(x_coords, y_coords, label=f"Route {depot_idx+1}")

    axs[0].text(0.05, 0.95, f"Initial Cost: {initial_cost:.2f}", transform=axs[0].transAxes, fontsize=12, color='blue', verticalalignment='top')
    axs[0].text(0.05, 0.95, f"Initial Time: {calculateTime(initial_cost):.2f}", transform=axs[0].transAxes, fontsize=12, color='blue', verticalalignment='bottom')
    axs[0].set_xlabel("X Coordinate")
    axs[0].set_ylabel("Y Coordinate")
    axs[0].legend()
    axs[0].grid(True)

    axs[1].set_title("Best Solution")
    for i, depot in enumerate(depot_coordinates):
        axs[1].scatter(depot[0], depot[1], c='red', label=f"Depot" if i == 0 else None, s=100, marker='s')

    for task in task_coordinates:
        axs[1].scatter(task[0], task[1], c='blue', label="Task" if task == task_coordinates[0] else None, s=50)

    for depot_idx, tasks in enumerate(best_solution):
        depot = depot_coordinates[depot_idx]
        route = [depot] + tasks + [depot]
        x_coords, y_coords = zip(*route)
        axs[1].plot(x_coords, y_coords, label=f"Route {depot_idx+1}")

    axs[1].text(0.05, 0.95, f"Best Cost: {best_cost:.2f}", transform=axs[1].transAxes, fontsize=12, color='green', verticalalignment='top')
    axs[1].text(0.05, 0.95, f"Best Time: {calculateTime(best_cost):.2f}", transform=axs[1].transAxes, fontsize=12, color='green', verticalalignment='bottom')
    axs[1].set_xlabel("X Coordinate")
    axs[1].set_ylabel("Y Coordinate")
    axs[1].legend()
    axs[1].grid(True)

    plt.suptitle(title)
    plt.show()