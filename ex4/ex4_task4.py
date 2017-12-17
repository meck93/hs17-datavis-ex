# -*- coding: utf-8 -*-
"""
Data Visualization HS 17 - Exercise 4
Moritz Eck - 14-715-296
"""

import ex4_reader as data_reader
import matplotlib.pyplot as plt
import numpy as np

# z-value constants
MIN_HEIGHT = 0.035
MAX_HEIGHT = 19.835
STEP_SIZE = 0.2

# desired height
HEIGHT = 1.0

# x-values: list containing the heights of the plot
heights = np.arange(MIN_HEIGHT, MAX_HEIGHT + STEP_SIZE, STEP_SIZE)

# load the terrain data
terr_data = data_reader.read_terrain_data()

# create the plot 
fig, plot = plt.subplots()

# set title of the window
fig.canvas.set_window_title("DataVis HS17 Ex04 - Task 1")

# create the axis and layout
plot.set_title("color filled terrain visualization")
plot.set_xlabel("longitude (X-coord)")
plot.set_ylabel("latitude (Y-coord)")
plot.set_aspect(1)

# invert the y axis
plot.invert_yaxis()

# plot the terrain data layer
terr_plot = plot.contourf(terr_data, cmap='terrain')

# colorbar for the terrain_plot
plot_colorbar = plt.colorbar(terr_plot)
plot_colorbar.set_label("elevation [m (above sea level)]")

# index for z-value at altitude: 1km
index = 0

# find the correct index for the HEIGHT
for i in range(len(heights)):
    if heights[i] > HEIGHT:
        index = i
        break

# load the temperature data: hour 1
temp_hour_1 = data_reader.read_geo_data('TC', 1)

# y-values: list of temperature data for location (200, 250)
temp_data = temp_hour_1[:, :, index]
print(temp_data)

# plotting the temperature data
temp_plot = plot.contourf(temp_data, cmap="gist_heat_r", alpha=1.0)

# colorbar for the temp_plot
plot_colorbar = plt.colorbar(temp_plot)
plot_colorbar.set_label("temperature at 1km altitude")

# show both plots
plt.show()