# -*- coding: utf-8 -*-
"""
Data Visualization Exercise 02
University of Zurich

Moritz Eck
14-715-296
"""
import numpy as np

from scipy import ndimage

from PIL import Image

from bokeh.plotting import figure, show, output_file, curdoc
from bokeh.layouts import row, column, widgetbox
from bokeh.models import Div, Tabs, Panel, Slider

# =============================================================================
# Page Setup: Title, Description, Heights, Widths, Standard Settings, etc. 
# =============================================================================

#New visualization page 
output_file(filename="exercise2.html", title="HS17: DataVis Ex2")

#Title & Description
title = "Dashboard - Data Visualization UZH HS17 - Exercise 2"
description = "This dashboard visualizes Scrat from Ice Age with different color channels or filters (© Moritz Eck)"

 # CSS & HTML 
css = "text-align: center; margin-bottom: 0;"
page_width=1433

# Title and description DIV tags
page_title = Div(text="<h1 style=\"" + css + "\">" + 
                 title + "</h1>", width=page_width)
page_description = Div(text="<p style=\"" + css + "\">" + 
                       description + "</p>", width=page_width)

# Different Constants: Widths & Heights
im1_height = 768
im1_width = 1024

ch_height = im1_height // 3
ch_width = im1_width // 3

side_height = int(im1_height / 2.5)
side_width = int(im1_width / 2.5)

# List containing all the plots
figures = []
gen_tools = "reset,wheel_zoom,pan"

# =============================================================================
# Reading the main image from the provided file 'image.jpg'
# =============================================================================

# Open image and make sure it's RGB*A*
iceage_img = Image.open('image.jpg').convert('RGBA')
xdim, ydim = iceage_img.size

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
main_img = figure(title="Original Image: Scrat", tools = gen_tools,
                  plot_width=im1_width, plot_height=im1_height, 
                  x_range=(0,xdim), y_range=(0,ydim))

main_img.image_rgba(image=[view], x=0, y=0, dw=xdim, dh=ydim)

figures.append(main_img)

# =============================================================================
# 3 Images: Different Color Channels (Red, Green, Blue)
# =============================================================================
# Creating the three different color channel images: red, green, blue
red = view.copy()
green = view.copy()
blue = view.copy()

for y in range(0,ydim):
    for x in range(0, xdim):
        # Red Color Channel = Zero Blue & Green Channel 
        red[y, x][1] = 0
        red[y, x][2] = 0        
        # Green Color Channel = Zero Blue & Green Channel       
        green[y, x][0] = 0
        green[y, x][2] = 0        
        # Blue Color Channel = Zero Blue & Green Channel
        blue[y, x][0] = 0
        blue[y, x][1] = 0
             
# Red Color Channel
red_img = figure(title='Red Color Channel', tools = gen_tools,
                  plot_width=ch_width, plot_height=ch_height, 
                  x_range=(0,ch_width), y_range=(0,ch_height))

red_img.image_rgba(image=[red], x=0, y=0, dw=ch_width, dh=ch_height)

figures.append(red_img)

# Green Color Channel
green_img = figure(title='Green Color Channel', tools = gen_tools,
                  plot_width=ch_width, plot_height=ch_height, 
                  x_range=(0,ch_width), y_range=(0,ch_height))

green_img.image_rgba(image=[green], x=0, y=0, dw=ch_width, dh=ch_height)

figures.append(green_img)

# Blue Color Channel
blue_img = figure(title='Blue Color Channel', tools = gen_tools,
                  plot_width=ch_width, plot_height=ch_height, 
                  x_range=(0,ch_width), y_range=(0,ch_height))

blue_img.image_rgba(image=[blue], x=0, y=0, dw=ch_width, dh=ch_height)

figures.append(blue_img)

# =============================================================================
# Image 5.1 - Grayscale Image 
# =============================================================================
def createGrayScale(image):
    # Grayscale weights (Red, Green, Blue)
    grayscale_weights = [0.3,0.59,0.11]
    
    # Empty matrix (array containing arrays) size ydim x xdim
    values = np.empty((ydim, xdim), dtype=np.uint32) 
    
    for y in range(0,ydim):
        for x in range(0, xdim):
            red_ch = view[y,x][0]*grayscale_weights[0]
            green_ch = view[y,x][1]*grayscale_weights[1]
            blue_ch = view[y,x][2]*grayscale_weights[2]
            
            values[y,x] = round(red_ch+green_ch+blue_ch)
    
    return values

# Grayscale weights
gray_data = createGrayScale(view)

# Grayscale Image
gray_img = figure(plot_width=side_width, plot_height=side_height, 
                  x_range=(0,side_width), y_range=(0,side_height),
                  tools = gen_tools)

gray_img.image(image=[gray_data], x=0, y=0, dw=side_width, dh=side_height)

figures.append(gray_img)

tab1 = Panel(child=gray_img, title='Grayscale')

# =============================================================================
# Image 5.2 - Color Reduction Median Cut 
# =============================================================================
def reduceColors(img, size):
    return ndimage.median_filter(img.copy(), size)

reduced_data = reduceColors(view, size=3)

# Median Reduction Image
reduced_img = figure(plot_width=side_width, plot_height=side_height, 
                     x_range=(0,side_width), y_range=(0,side_height),
                     tools = gen_tools)

reduced_img.image_rgba(image=[reduced_data], x=0, y=0, dw=side_width, dh=side_height)

figures.append(reduced_img)

tab2 = Panel(child=reduced_img, title='Median Cut')

# Combining Image 5.1 & 5.2 into two tabs
img5 = Tabs(tabs=[tab1,tab2])

# =============================================================================
# Image 6 - Salt & Pepper Filter
# =============================================================================
def createSaltPepperNoise(img, density=0.1, ratio=0.5):
    out = img.copy()
    
    # Creating the number of salt pixels (white pixels)
    num_salt = np.ceil(density*xdim*ydim*ratio)
    # Randomly determining the cells in the array (1024, 768) to place the pixels
    # Returns the cells where to place the white pixels
    coords = [np.random.randint(0, i - 1, int(num_salt)) for i in view.shape]
    out[coords[0],coords[1],:] = [255,255,255,255]

    # Creating the number of pepper pixels (black pixels)
    num_pepper = np.ceil(density*xdim*ydim*(1.0-ratio))
    # Randomly determining the cells in the array (1024, 768) to place the pixels
    # Returns the cells where to place the black pixels
    coords = [np.random.randint(0, i - 1, int(num_pepper)) for i in view.shape]
    out[coords[0],coords[1],:] = [0,0,0,255]
    
    return out       

salt_data = createSaltPepperNoise(view, density=0.1)
    
# Green Color Channel
salt = figure(title='Salt & Pepper Noise', tools = gen_tools,
              plot_width=side_width, plot_height=side_height, 
              x_range=(0,side_width), y_range=(0,side_height))

salt_img = salt.image_rgba(image=[salt_data], x=0, y=0, dw=side_width, dh=side_height)

salt_slider = Slider(start=0, end=0.5, value=0.1, step=0.1, 
                     width=side_width-40, 
                     title='Salt and Pepper Filter - Adjust the Density')

def updateSaltPepper(attrname, old, new):
    # Compute the new values with the input from the slider
    salt_data = createSaltPepperNoise(view, density=salt_slider.value)
    # Update the datasource of the gauss_img - key: image - value: salt_data
    salt_img.data_source.data = {'image':[salt_data]}

salt_slider.on_change('value', updateSaltPepper)

figures.append(salt)

# =============================================================================
# Image 7 - Gaussian Smoothing Filter 
# =============================================================================
gauss_data = ndimage.gaussian_filter(view.copy(), 1)

# Green Color Channel
gauss = figure(title='Gaussian Filter', tools = gen_tools,
               plot_width=side_width, plot_height=side_height, 
               x_range=(0,side_width), y_range=(0,side_height))

gauss_img = gauss.image_rgba(image=[gauss_data], x=0, y=0, dw=side_width, dh=side_height)

sigma_slider = Slider(start=0, end=5, value=2, step=1, 
                      width=side_width-40, 
                      title='Gaussian Filter - Sigma Level')

def updateSigma(attrname, old, new):
    # Compute the new values with the input from the slider
    gauss_data = ndimage.gaussian_filter(view.copy(), sigma_slider.value)
    # Update the datasource of the gauss_img - key: image - value: gauss_data
    gauss_img.data_source.data = {'image':[gauss_data]}

sigma_slider.on_change('value', updateSigma)

figures.append(gauss)

# =============================================================================
# Adjusting the axis, format and styles of all figures
# =============================================================================
for fig in figures:
    fig.toolbar_location = "right"
    fig.xaxis.visible = False
    fig.yaxis.visible = False    
    fig.xgrid.grid_line_color = None
    fig.ygrid.grid_line_color = None

# Open the output file in a browser
#show(column(main_img, row(red_img, blue_img, green_img)))
curdoc().add_root(column(page_title, page_description,
                         row(column(main_img, row(red_img, green_img, blue_img)),
                             column(row(img5), 
                                     column(salt, widgetbox(salt_slider)), 
                                     column(gauss, widgetbox(sigma_slider))))))