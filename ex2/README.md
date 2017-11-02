### READ ME

**How to display the dashboard?**
* Prerequisites: Python 3.6.* and Tornado 4.4.2. With the most recent version of Tornado - V4.5 - the sliders will not update the visualization accordingly.

To just display the dashboard (no interactivity): Open the ex2_main.html file.

**Interactive Version:**
1. Ensure you have Python 3.6.* and Tornado 4.4.2 installed
2. Open a command prompt 
3. Navigate to the folder containing the files (ex2_main.py & image.jpg)
4. Run 'bokeh serve --show ex2_main.py'
5. If the browser doesn't open automatically: Open http://localhost:5006/ex2_main
6. Wait until the page has loaded completly. Try adjusting the sliders. 

**What has been plotted?**
1. Original Image
2-4. Each RGB Color Channel (Red, Green, Blue)
5.1 A grayscale version of the original image using weights red, green, blue [0.3, 0.59, 0.11]
5.2 The original image with reduced colors (32 colors)
6. The original image with added artificially salt & pepper noise (black and white pixels)
7. The orignal image with the gaussian filter applied to each color channel

_Data Visualization Exercise 02
HS 17 - University of Zurich
Moritz Eck_