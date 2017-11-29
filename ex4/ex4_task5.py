
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
plt2 = plt.subplot(grid[1, 0:4])

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

# coordinates where to start plot the quives - coord: (y, x)
coords = []

# creating the midpoint of each cell (10x10)
# starting @ (25, 25) in the first cell 
for i in range(0, 500, 50):
    coord_row = []

    for j in range(0, 500, 50):
        # coord (y, x)
        coord = ((j+25), (i+25)) 
        coord_row.append(coord)
    
    coords.append(coord_row)

# z-index for altitude @ 1km
HEIGHT = 5

# x component of the wind (west-east)
x_wind = data_reader.read_geo_data('U', 1)
x_wind = x_wind[:, :, HEIGHT]

# y component of the wind (south-north)
y_wind = data_reader.read_geo_data('V', 1)
y_wind = y_wind[:, :, HEIGHT]

# empty component arrays for the x, y, z-value @ 1km
x_comp = np.ndarray((10, 10), dtype=float)
y_comp = np.ndarray((10, 10), dtype=float)

x = 0
y = 0

# creating the means of the cells with size (50,50)
for i in range(0, 500, 50):
    x = 0

    for j in range(0, 500, 50):
        x_val = []
        y_val = []
        
        for u in range(0, 50):
            for v in range(0, 50):
                # only add the value if it is within the allowed range
                if not x_wind[i+u][j+v] > 100:
                    x_val.append(x_wind[i+u][j+v])
                if not y_wind[i+u][j+v] > 100:
                    y_val.append(y_wind[i+u][j+v])
        
        # compute the means of the x and y components for the (50, 50) cell 
        x_comp[y][x] = data_reader.computeMean(x_val)
        y_comp[y][x] = data_reader.computeMean(y_val)
        
        x += 1
    y += 1

# plotting the quivers (vectors) 
for i in range(0, 10):
    for j in range(0, 10):
        plt1.quiver(coords[i][j][0], 
                    coords[i][j][1], 
                    x_comp[i][j], 
                    y_comp[i][j], 
                    pivot='middle', units='height', scale=200)
        #print("Row:", i, "\tX-Coord:", coordinates[i][j][0],"\tY-Coord:", coordinates[i][j][1], "\tX:", x_comp[i][j], "\tY:", y_comp[i][j])

# colorbar for the wind
# wind_colorbar = plt.colorbar(quivers, ax=plt1, orientation='vertical')
# wind_colorbar.set_label("wind speed in [m/s]")

plt.show()

''' # TODO: Implement four scatterplots of four different locations
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
scatter_matrix(df, alpha=1, figsize=(6, 6), diagonal='kde') '''
