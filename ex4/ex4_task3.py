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

# load the temperature data for hours 1 - 5
raw_data = list()

for i in range(1, 6):
    raw_data.append(data_reader.read_geo_data('TC',i))

# y-values: list of temperature data for location (200, 250)
# temperatures[0] = hour1, etc.
temperatures = list()

for i in range(0, 5):
    temperatures.append(raw_data[i][X_POS - 1][Y_POS - 1])

stacked_data = list()
stacked_data.append(temperatures[0])

for i in range(1, 5):
    stacked_data.append(np.add(stacked_data[i-1], temperatures[i]))

# x-values: list containing the heights of the plot
heights = np.arange(MIN_HEIGHT, MAX_HEIGHT + STEP_SIZE, STEP_SIZE)

# create the plot
temp_fig, temp_plot = plt.subplots()

# set title of the window
temp_fig.canvas.set_window_title("DataVis HS17 Ex04 - Task 3")

# setup the axis and layout
temp_plot.set_title("Temperatures at different altitude levels.\n" + "At Position: (" + str(X_POS) + ", " + str(Y_POS) + ")")
temp_plot.set_xlabel("Altitude Level [km]")
temp_plot.set_ylabel("Temperature [C°]")
temp_plot.minorticks_on()

# plot the data
temp_plot.plot(heights, stacked_data[0], label='Hour 1')
temp_plot.plot(heights, stacked_data[1], label='Hour 2')
temp_plot.plot(heights, stacked_data[2], label='Hour 3')
temp_plot.plot(heights, stacked_data[3], label='Hour 4')
temp_plot.plot(heights, stacked_data[4], label='Hour 5')
temp_plot.legend()

# temp_plot2 = plt.subplot()
# temp_plot2.stackplot(heights, temperatures, baseline='zero')

# show the plot
plt.show()