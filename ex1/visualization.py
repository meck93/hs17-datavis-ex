# -*- coding: utf-8 -*-

""" Data Visualization HS 17
    Implemenation of Exercise 1
    
    Moritz Eck - 14 715 296"""

from Figure1 import Figure1
from Figure2 import Figure2

import pandas as pd

from bokeh.core.properties import value
from bokeh.io import output_file, show
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource
from bokeh.io import curdoc
from bokeh.layouts import row, column

#New visualization page 
output_file("output.html", title="Data Visualization Exercise 1")

#Read the data from the CSV file
data = pd.read_csv('births.csv', delimiter=',')
data = data.rename(columns={"StichtagDatJahr":"Jahr","SexKurz":"Sex", "StatZoneLang":"StadtZone", "QuarLang":"Quartier","AnzGebuWir":"Births"})
   
#Plot 1: Births in 2015 per gender
fig1 = Figure1(data)

show(fig1.plot1)

#Plot 2: 
fig2 = Figure2(data)

#show(fig2.plot2)