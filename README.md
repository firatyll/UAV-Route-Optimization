# UAV Route Optimization

This repository contains a project focused on optimizing Unmanned Aerial Vehicle (UAV) routes for efficient and cost-effective navigation. The solution incorporates advanced algorithms and mathematical models to ensure optimal route planning.

## Introduction

Unmanned Aerial Vehicles (UAVs) play a significant role in various industries, including logistics, surveillance, and environmental monitoring. Efficient route optimization is critical for minimizing energy consumption, reducing operational costs, and ensuring timely delivery. This project aims to address these challenges by implementing robust route optimization algorithms.

## Features

- **Optimal Route Planning:** Ensures minimum energy usage and cost.
- **Flexible Algorithm Integration:** Supports various optimization techniques like Genetic Algorithms, A* Search, etc.
- **Scalable Design:** Can handle multiple UAVs and complex route scenarios.
- **Visualization Tools:** Displays optimized routes for better understanding and analysis.

## Algorithm Evaluation & Comparison

After running the algorithms 100 times with the same input, the outputs are as in the table. As a result, the average genetic algorithm cost is **16% less** than the average simulated annealing algorithm cost. After update Genetic algorithm ([firatyll/UAV-Route-Optimization@8df3e75](https://github.com/firatyll/UAV-Route-Optimization/commit/8df3e75)) finds the best solution 46% of the time.


| Run     | SimulatedAnnealingCost | GeneticAlgorithmCost |
|---------|------------------------|----------------------|
| 1       | 46066.69885649407      | 37915.79059298257    |
| 2       | 48133.68677794399      | 37915.790592982565   |
| 3       | 44735.938534436046     | 38640.687078658906   |
| .       | .                      | .                    |
| .       | .                      | .                    |
| .       | .                      | .                    |
| 97      | 42011.86865275664      | 41341.65441974222    |
| 98      | 53230.45787862899      | 38640.687078658906   |
| 99      | 43226.38721936189      | 37915.79059298257    |
| 100     | 54413.253886268074     | 41341.65441974222    |
| Average | 48251.1957670732       | 38809.7242431605     |

### Simulated Annealing Visualization
![simulated annealing](<assets/simulated annealing.png>)
### Genetic Algorithm Visualization
![genetic algorithm](<assets/genetic algorithm.png>)


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

