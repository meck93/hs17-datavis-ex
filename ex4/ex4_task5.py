
# -*- coding: utf-8 -*-
"""
Data Visualization HS 17 - Exercise 4
Moritz Eck - 14-715-296
"""

import ex4_reader as data_reader
import matplotlib
import matplotlib.cm as cm
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
plt1.set_title("Wind Speed @ Hour 1 and Altitude = 1km")
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

# coordinates for the 10x10 cells
x_coord = np.ndarray((10, 10), dtype=float)
y_coord = np.ndarray((10, 10), dtype=float)

x = 0
y = 0

vec = list()

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
        vec.append(((x_comp[y][x]**2) + (y_comp[y][x]**2))**0.5)

        # create the coordinates for this vector
        x_coord[y][x] = j+25
        y_coord[y][x] = i+25
        
        x += 1
    y += 1

# normalize the magintude of the quivers to [0, 1]
norm = matplotlib.colors.Normalize(vmin=min(vec), vmax=max(vec))

# choose a colormap
cm = matplotlib.cm.gist_heat_r

# create a ScalarMappable and initialize an empty array
sm = matplotlib.cm.ScalarMappable(cmap=cm, norm=norm)
sm.set_array([ ])

# plotting the wind vectors (quivers)
quiv = plt1.quiver(x_coord, y_coord, x_comp, y_comp, pivot='middle', units='height', scale=200, color=cm(norm(vec)))

# colorbar for the wind
wind_colorbar = plt.colorbar(sm, ax=plt1, orientation='vertical')
wind_colorbar.set_label("wind speed in [m/s]")

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