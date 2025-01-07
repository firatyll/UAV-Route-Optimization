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

After running the algorithms 100 times with the same input, the outputs are as in the table. As a result, the average genetic algorithm cost is **16% less** than the average simulated annealing algorithm cost.

| Run     | SimulatedAnnealingCost | GeneticAlgorithmCost |
|---------|------------------------|----------------------|
| 1       | 49954.97723010203      | 37950.86388960772    |
| 2       | 48930.8474596152       | 37915.790592982565   |
| 3       | 49411.75077769216      | 39899.537658400564   |
| .       | .                      | .                    |
| .       | .                      | .                    |
| .       | .                      | .                    |
| 97      | 42781.11966332571      | 42946.79459625984    |
| 98      | 41615.96144690286      | 45069.46126362633    |
| 99      | 52769.6205226033       | 44812.3042169015     |
| 100     | 47250.00750125875      | 38209.83840886371    |
| Average | 48023.8132721242       | 39986.98549336301    |

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

