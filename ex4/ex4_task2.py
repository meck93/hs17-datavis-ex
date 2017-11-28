# -*- coding: utf-8 -*-
"""
Data Visualization HS 17 - Exercise 4
Moritz Eck - 14-715-296
"""

import ex4_reader as data_reader
import numpy as np
import matplotlib.pyplot as plt

# z-value constants
MIN_HEIGHT = 0.035
MAX_HEIGHT = 19.835
STEP_SIZE = 0.2

# x & y position
X_POS = 200
Y_POS = 250

# load the temperature data: hour 1
tc_d01 = data_reader.read_geo_data('TC',1)

# y-values: list of temperature data for location (200, 250)
temperatures = tc_d01[X_POS-1][Y_POS-1]

# x-values: list containing the heights of the plot
heights = np.arange(MIN_HEIGHT, MAX_HEIGHT + STEP_SIZE, STEP_SIZE)

# create the plot
temp_fig, temp_plot = plt.subplots()

# set title of the window
temp_fig.canvas.set_window_title("DataVis HS17 Ex04 - Task 2")

# setup the axis and layout
temp_plot.set_title("Temperature at different altitude levels.\n" + "At Position: (" + str(X_POS) + ", " + str(Y_POS) + "). Simulated Hour 1.")
temp_plot.set_xlabel("Altitude Level [km]")
temp_plot.set_ylabel("Temperature [C°]")
temp_plot.minorticks_on()

# plot the data
temp_plot.plot(heights, temperatures, color='black', linestyle='dashed')

# show the plot
plt.show()
