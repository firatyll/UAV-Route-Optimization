# UAV Route Optimization

This repository contains a project focused on optimizing Unmanned Aerial Vehicle (UAV) routes for efficient and cost-effective navigation. The solution incorporates advanced algorithms and mathematical models to ensure optimal route planning.

## Introduction

Unmanned Aerial Vehicles (UAVs) play a significant role in various industries, including logistics, surveillance, and environmental monitoring. Efficient route optimization is critical for minimizing energy consumption, reducing operational costs, and ensuring timely delivery. This project aims to address these challenges by implementing robust route optimization algorithms.

## Features

- **Optimal Route Planning:** Ensures minimum energy usage and cost.
- **Flexible Algorithm Integration:** Supports various optimization techniques like **Genetic Algorithms, Ant Colony and Simulated Annealing.**
- **Scalable Design:** Can handle multiple UAVs and complex route scenarios.
- **Visualization Tools:** Displays optimized routes for better understanding and analysis.

## Algorithm Evaluation & Comparison

After running the algorithms 100 times with the same input, the outputs are as in the table. As a result, the average genetic algorithm cost is **16% less** than the average simulated annealing algorithm cost. Genetic Algorithm and Ant Colony algorithm costs are almost equal but Ant Colony beats Genetic Algorithm with **1.17%** difference. Whereas Genetic Algorithm best cost slighlty better than the Ant Colony best cost. Despite that Standard Deviation of Ant Colony executions **236.36** and Standard Deviation of Genetic Algorithms is **1346.20**. So **Ant Colony Standard Deviation 82.2%** lower than Genetic Algorithm Standard Deviation. This analysis indicates Ant Colony algorithm generates more **Consistent and Stable** results. 


| Run     | SimulatedAnnealingCost | GeneticAlgorithmCost | AntColonyAlgorithmCost |
|---------|------------------------|----------------------|------------------------|
| 1       | 52380.371568500275     | 37915.79059298257    | 38435.56212417904      |
| 2       | 50660.10815550388      | 38640.687078658906   | 37950.86388960772      |
| 3       | 43118.13231865587      | 41341.65441974222    | 37950.86388960771      |
| .       | .                      | .                    | .                      |
| .       | .                      | .                    | .                      |
| .       | .                      | .                    | .                      |
| 97      | 7614.44035412733       | 37915.79059298257    | 38191.310622302866     |
| 98      | 47800.36011347326      | 37915.790592982565   | 38244.911705488856     |
| 99      | 46356.56919404552      | 37915.79059298257    | 38146.04891815241      |
| 100     | 44833.89282566424      | 37915.79059298257    | 38148.31884491421      |
| Average | 48745.11326972345      | 38703.14466324456    | 38246.853112397686     |
| StdDev  | 4140.53                | 1346.20              | 263.36                 |
| Min     | 39970.05               | 37915.79             | 37950.86               |
| Max     | 57810.64               | 44764.163            | 39269.48               |

### Simulated Annealing Visualization
![simulated annealing](<assets/simulated annealing.png>)
### Genetic Algorithm Visualization
![genetic algorithm](<assets/genetic algorithm.png>)
### Ant Colony Visualization
![ant colony](<assets/ant colony.png>)


## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/firatyll/UAV-Route-Optimization.git
   ```
2. Navigate to the project directory:
   ```bash
   cd UAV-Route-Optimization
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Ensure all dependencies are installed.
2. Run the main script:
   ```bash
   python main.py
   ```
3. Follow the prompts to input parameters for the UAV route optimization.
4. Visualize the output routes and analyze the performance metrics.

## Contributing

Contributions are welcome! If you'd like to contribute:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Make your changes and commit them:
   ```bash
   git commit -m "Add feature description"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

