# -*- coding: utf-8 -*-
"""
Data Visualization HS 17 - Exercise 4
Moritz Eck - 14-715-296
"""

import ex4_reader as data_reader
import matplotlib.pyplot as plt
import numpy as np

# load the terrain data
terrain_data = data_reader.read_terrain_data()

# create the plot 
fig, plot = plt.subplots()

# set title of the window
fig.canvas.set_window_title("DataVis HS17 Ex04 - Task 1")

# create the axis and layout
plot.set_title("color filled terrain visualization")
plot.set_xlabel("longitude (X-coord)")
plot.set_ylabel("latitude (Y-coord)")
plot.set_aspect(1)

# invert the y and x axis
plot.invert_yaxis()

# plot the data
terrain_plot = plot.contourf(terrain_data, alpha=1.0, cmap='terrain')

# colorbar for the terrain_plot
plot_colorbar = plt.colorbar(terrain_plot)
plot_colorbar.set_label("elevation in meters above sea level")

# index for z-value at altitude: 1km
# start at: 0.035 step size: 0.2 step 5: 1.035km
HEIGHT = 5

# load the temperature data: hour 1
temp_hour1 = data_reader.read_geo_data('TC', 1)

# y-values: list of temperature data for location (200, 250)
temp_data = temp_hour1[:, :, HEIGHT]

# plotting the temperature data
temp_plot = plot.contourf(temp_data, alpha=0.5, cmap="gist_heat_r")

# colorbar for the temp_plot
plot_colorbar = plt.colorbar(temp_plot)
plot_colorbar.set_label("temperature at 1km altitude")

# show both plots
plt.show()