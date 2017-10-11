# -*- coding: utf-8 -*-

""" Data Visualization HS 17
    Implemenation of Exercise 1
    
    Moritz Eck - 14 715 296"""

from Figure1 import Figure1
from Figure2 import Figure2
from Figure3 import Figure3
from Figure4 import Figure4

import pandas as pd
from bokeh.io import output_file, show
from bokeh.layouts import row, column
from bokeh.models import Div

#New visualization page 
output_file(filename="output.html", title="HS17: DataVis Ex1")

#Read the data from the CSV file
data = pd.read_csv('births.csv', delimiter=',')
data = data.rename(columns={"StichtagDatJahr":"Jahr","SexKurz":"Sex", "StatZoneLang":"StadtZone", "QuarLang":"Quartier","AnzGebuWir":"Births"})
   
#Plot 1
fig1 = Figure1(data)

#Plot 2 
fig2 = Figure2(data)

#Plot 3
fig3 = Figure3(data)

#Plot 4
fig4 = Figure4(data)

#Title & Description
title = "Dashboard - Data Visualization UZH HS17 - Exercise 1"
description = "This dashboard visualizes the number of births in the city of Zurich between 1993 and 2015 (© Moritz Eck)"

 # CSS & HTML 
css = "text-align: center; margin-bottom: 0;"
page_width=1800

page_title = Div(text="<h1 style=\"" + css + "\">" + title + "</h1>",
                  width=page_width)
page_description = Div(text="<p style=\"" + css + "\">" + description + "</p>",
                        width=page_width)
 
#Displaying all visualizations
show(column(column(page_title, page_description), 
            row(fig1.plot1), 
            row(fig2.plot2, fig3.pie_chart, fig4.plot)))