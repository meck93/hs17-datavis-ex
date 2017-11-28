# -*- coding: utf-8 -*-
"""
Data Visualization HS 17 - Exercise 4
Moritz Eck - 14-715-296
"""

import ex4_reader as data_reader
import matplotlib.pyplot as plt

# load the terrain data
terrain_data = data_reader.read_terrain_data()

# create the plot 
terrain_fig, terrain_plot = plt.subplots()

# set title of the window
terrain_fig.canvas.set_window_title("DataVis HS17 Ex04 - Task 1")

# create the axis and layout
terrain_plot.set_title("color filled terrain visualization")
terrain_plot.set_xlabel("longitude (X-coord)")
terrain_plot.set_ylabel("latitude (Y-coord)")
terrain_plot.set_aspect(1)

# invert the y and x axis
terrain_plot.invert_yaxis()

# plot the data
plot = terrain_plot.contourf(terrain_data, cmap='terrain')

# colorbar for the terrain_plot
plot_colorbar = plt.colorbar(plot)
plot_colorbar.set_label("elevation in meters above sea level")

plt.show()