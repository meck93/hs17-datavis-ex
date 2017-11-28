
# -*- coding: utf-8 -*-
"""
Data Visualization HS 17 - Exercise 4
Moritz Eck - 14-715-296
"""

import ex4_reader as data_reader
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
import pandas as pd
from pandas.plotting import scatter_matrix

# create the grid
grid = gridspec.GridSpec(3, 4)

# create figure and title
fig = plt.figure()
fig.canvas.set_window_title("DataVis HS17 Ex04 - Task 5")

# create the subplots
plt1 = plt.subplot(grid[0, 0:3])
plt2 = plt.subplot(grid[1, 0:3])

# create the axis and layout
plt1.set_title("color filled terrain visualization")
plt1.set_xlabel("longitude (X-coord)")
plt1.set_ylabel("latitude (Y-coord)")
plt1.set_aspect(1)

# invert the y and x axis
plt1.invert_yaxis()

# load the terrain data
terrain_data = data_reader.read_terrain_data()

# plot the data
terrain_plot = plt1.contourf(terrain_data, alpha=1.0, cmap='terrain')

# colorbar for the terrain_plot
plot_colorbar = plt.colorbar(terrain_plot, ax=plt1, orientation='vertical')
plot_colorbar.set_label("elevation in meters above sea level")

# TODO: Implement 10x10 grid with cells with containing the wind vectors
# use the arrows

# z-index for altitude @ 1km
HEIGHT = 5

# x, y and z-value of the raw wind data
x_wind = data_reader.read_geo_data('U', 1)
y_wind = data_reader.read_geo_data('V', 1)
z_wind = data_reader.read_geo_data('W', 1)

# empty component arrays for the x, y, z-value @ 1km
x_component = np.ndarray((10, 10), dtype=float)
y_component = np.ndarray((10, 10), dtype=float)
z_component = np.ndarray((10, 10), dtype=float)

x = 0
y = 0

min_x = 99999999999999999999
max_x = -99999999999999999999
min_y = 99999999999999999999
max_y = -99999999999999999999

# coordinates where to start locationwise with the arrows
coordinates = []

# filling the x, y, z components of the wind @ altitude 1km
for i in range(0, 500, 50):
    y = 0
    entry = []
    for j in range(0, 500, 50):
        x_component[x][y] = x_wind[i][j][HEIGHT]
        y_component[x][y] = y_wind[i][j][HEIGHT]

        # find the max and min values of x & y components
        if min_x > x_component[x][y]:
            min_x = x_component[x][y]
        
        if max_x < x_component[x][y]:
            max_x = x_component[x][y]
        
        if min_y > y_component[x][y]:
            min_y = y_component[x][y]
        
        if max_y < y_component[x][y]:
            max_y = y_component[x][y]

        entry.append(((i+25)/500, (j+25)/500))
        y += 1

    coordinates.append(entry)    
    x += 1

norm_x = np.ndarray((10, 10), dtype=float)
norm_y = np.ndarray((10, 10), dtype=float)

# normalizing the values to a range [0, 1]
for i in range(0, 10):
    for j in range(0, 10):
        norm_x[i][j] = (x_component[i][j] - min_x) / (max_x - min_x)
        norm_y[i][j] = (y_component[i][j] - min_y) / (max_y - min_y)

# plotting arrows 
for i in range(0, 10):
    for j in range(0, 10):
        plt2.arrow(coordinates[i][j][0], coordinates[i][j][1], norm_x[i][j], norm_y[i][j], head_width=0.025, head_length=0.05, fc='k', ec='k')

plt2.invert_yaxis()

# TODO: Implement four scatterplots of four different locations
# e.g. locations: (50, 50), (150, 150), (250, 250), (350, 350), (450, 450)

# read raw data
pressure = data_reader.read_geo_data('P', 1)
rain = data_reader.read_geo_data('QRAIN', 1)
temp = data_reader.read_geo_data('TC', 1)

# z-index for altitude @ 1km
HEIGHT = 5

# extracting the data @ 1km altitude
pressure = pressure[:, :, HEIGHT]
rain = rain[:, :, HEIGHT]
temp = temp[:, :, HEIGHT]

data = list()

# extracting the five different locations
for i in range(50, 500, 100):
    entry = list()
    entry.append(temp[i][i])
    entry.append(pressure[i][i])
    entry.append(rain[i][i])
    data.append(entry)

labels = ['Temperature', 'Pressure', 'Precipitation']

# plotting the scatter plot matrix
df = pd.DataFrame(data, columns=labels)
scatter_matrix(df, alpha=1, figsize=(6, 6), diagonal='kde')

plt.show()
