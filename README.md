# Effects of Seasonal Births and Predation on Disease Spread

This repository contains the code and simulation data for the article "Effects of Seasonal Births and Predation on Disease Spread" by Allison Introne and Leah B. Shaw

All of the code was developed and run using Python version 3.8.3

## File Descriptions

- `Constant_Birth_Tutorial.ipynb`: shows how to define the system of ODEs, run the simulation for the constant birth linear predation and constant birth hyperbolic predation models, calculate the average number of infected individuals over one year, and plot the solutions after transient behavior

- `Pulsed_Birth_Tutorial.ipynb`: shows how to define the system of ODEs, run the simulation for the pulsed birth linear predation and pulsed birth hyperbolic predation models, calculate the average number of infected individuals over one period, and plot the solutions after transient behavior and the susceptible-infected phase plane. The notebook also includes documentation on the function used to determine the period of the solution. The parameters for figures 2 and 5 are given in the notebook so that the figures can be reproduced

- `Reproduce_figures.ipynb`: reproduces figures 1, 3, 4, 6, and 7

- `save_sim_data_fig4.py`: runs simulations and saves data needed to reproduce figure 4

- `save_sim_data_figs_6_7.py`: runs simulations and saves data needed to reproduce figures 6 and 7

- `sim_functions.py`: contains all the functions needed to run simulations. For documentation on the functions see Constant_Birth_Tutorial.ipynb and Pulsed_Birth_Tutorial.ipynb


## Simulation Data

The data needed to reproduce figures 4, 6, and 7 is stored in the folder named Data
