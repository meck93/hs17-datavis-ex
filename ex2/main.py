# -*- coding: utf-8 -*-
"""
Data Visualization Exercise 02
University of Zurich

Moritz Eck
14-715-296
"""
import numpy as np
from PIL import Image
from bokeh.plotting import figure, show, output_file

# Open image and make sure it's RGB*A*
iceage_img = Image.open('image.jpg').convert('RGBA')
xdim, ydim = iceage_img.size

print("Dimensions: ({xdim}, {ydim})".format(**locals()))

# Create an array representation for the image 'img'
# and 8 layer/RGBA version of it 'view'.
img = np.empty((ydim, xdim), dtype=np.uint32) 
view = img.view(dtype=np.uint8).reshape((ydim, xdim, 4))

# Copy the RGBA image into view, flipping it so it comes right-
# with a lower-left origin 
view[:,:,:] = np.flipud(np.asarray(iceage_img))

# =============================================================================
# Image 1: No modification
# =============================================================================

# Display the 32-bit RGBA image (Full Image)
fig = figure(title="Scrat", plot_width=1024, plot_height=768, tools="reset,wheel_zoom", toolbar_location="right")
fig.image_rgba(image=[img], x=0, y=0, dw=xdim, dh=ydim)

# Designing the plot (legend, axis alignment & spacing)
fig.y_range.start = 0
fig.y_range.end = 768
fig.x_range.start = 0
fig.x_range.end = 1024
                        
# X-Axis design
fig.xgrid.grid_line_color = None
fig.xaxis.visible = False
                       
# Y-Axis design 
fig.ygrid.grid_line_color = None
fig.yaxis.visible = False

#New visualization page 
output_file(filename="exercise2.html", title="HS17: DataVis Ex2")

# Open the output file in a browser
show(fig)