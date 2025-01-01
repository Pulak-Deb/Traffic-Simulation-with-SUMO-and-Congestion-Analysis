# Traffic Simulation and Congestion Analysis

This project simulates traffic flow and congestion levels using **SUMO** (Simulation of Urban Mobility) and **Python**. It focuses on generating dynamic traffic flows and analyzing congestion patterns during different times of the day. The project also includes data collection and classification of congestion levels, as well as prediction and visualization of peak congestion periods.

## Table of Contents
- [Overview](#overview)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Data Analysis](#data-analysis)
  - [Classifying Congestion Levels](#classifying-congestion-levels)
  - [Congestion Over Time](#congestion-over-time)
  - [Congestion by Time of Day](#congestion-by-time-of-day)
- [Dependencies](#dependencies)
- [License](#license)

## Overview
The simulation generates dynamic traffic flow and congestion data based on the real-time traffic simulation conditions. The analysis focuses on identifying peak congestion periods by classifying congestion levels (Low, Moderate, High) based on lane occupancy. The project also uses this data to predict high congestion periods, allowing for improved traffic management strategies.

### Key Features:
- Simulation of traffic flow and congestion using SUMO.
- Classification of congestion levels (Low, Moderate, High).
- Analysis of congestion patterns during morning, midday, and evening periods.
- Visualization of congestion data and flow trends.
- Export of traffic flow and congestion data to CSV files for further analysis.

## Setup Instructions

### Prerequisites:
1. **SUMO**: Make sure SUMO (Simulation of Urban MObility) is installed. Follow the instructions on [SUMO's official website](https://www.eclipse.org/sumo/) to install SUMO.
2. **Python**: Python 3.x should be installed.
3. **Required Python Libraries**:
   - `traci`: Interface for Python to control the SUMO simulation.
   - `matplotlib`: For data visualization.
   - `pandas`: For data manipulation and analysis.

You can install the required libraries using pip:

```bash
pip install traci matplotlib pandas
