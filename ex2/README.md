### READ ME
_Data Visualization Exercise 02_
_HS 17 - University of Zurich_
_Moritz Eck_

#### What has been plotted?
1. Original Image (Scrat from Ice Age)
2. Each RGB Color Channel (Red, Green, Blue): Image 2-4
3. A grayscale version of the original image using weights red, green, blue [0.3, 0.59, 0.11]  (Image 5.1)
4. The original image with reduced colors (32 colors) (Image 5.2)
5. The original image with added artificially salt & pepper noise (black and white pixels) (Image 6)
6. The orignal image with the gaussian filter applied to each color channel (Image 7)

#### How to show the plot?

**Prerequisites**
* Python 3.6.* 
* Tornado 4.4.2  _(With the most recent version of Tornado - V4.5 - the sliders will not update the visualization accordingly.)_

To just display the dashboard (no interactivity): Open the ex2_main.html file.

**Interactive Version:**
1. Ensure you have Python 3.6.* and Tornado 4.4.2 installed
2. Open a command prompt 
3. Navigate to the folder containing the files (ex2_main.py & image.jpg)
4. Run 'bokeh serve --show ex2_main.py'
5. If the browser doesn't open automatically: Open http://localhost:5006/ex2_main
6. Wait until the page has loaded completly. Try adjusting the sliders. 



