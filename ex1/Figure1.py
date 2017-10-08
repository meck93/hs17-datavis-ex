# -*- coding: utf-8 -*-

""" Data Visualization HS 17
    Implemenation of Exercise 1
    
    Moritz Eck - 14 715 296"""

import pandas as pd

from bokeh.core.properties import value
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, HoverTool

class Figure1:
    
    def __init__(self, data):
        self.data = data
        self.plot1 = None
        
        self.createFigure1()
        
    def createFigure1(self):     
        #Plot 1: Births in 2015 per gender
        births_2015 = pd.DataFrame(self.data.loc[self.data['Jahr'] == 2015], copy=True)
        
        # Removing the unnecessary columns
        births_2015 = births_2015.drop("SexCd", axis=1)
        births_2015 = births_2015.drop("StatZoneSort", axis=1)
        births_2015 = births_2015.drop("QuarSort", axis=1)
        
        #X-Axis Values: The names of the different parts of the city of Zurich
        quartier_names = []
        
        for name in births_2015['Quartier']:
            if name not in quartier_names:
                quartier_names.append(name)
            
        quartier_names.sort()
        
        #Y-Axis Values: Nr of Births (male & female) per city part in 2015
        births = pd.DataFrame(births_2015, copy=True)
        births = births.drop("StadtZone", axis=1)
        births = births.drop("Jahr", axis=1)
        
        maleBirths = pd.DataFrame(births.loc[births_2015['Sex'] == 'M'], copy=True)
        maleBirths = maleBirths.drop("Sex", axis=1)
        maleBirths = maleBirths.groupby("Quartier").sum()
        
        femaleBirths = pd.DataFrame(births.loc[births_2015['Sex'] == 'W'], copy=True)
        femaleBirths = femaleBirths.drop("Sex", axis=1)
        femaleBirths = femaleBirths.groupby("Quartier").sum()
        
        data= {'Quartier' : quartier_names, 
               'Male' : maleBirths['Births'].values.tolist(), 
               'Female' : femaleBirths['Births'].values.tolist()}
        
        print(data)
        
        dataSource = ColumnDataSource(data=data)
              
        #Creating the vertical stacked bar chart 
        self.plot1 = figure(x_range=quartier_names, title="Births in 2015 per Quartier in the city of Zurich",
                       plot_width=1000, plot_height=600,
                       tools="pan,reset,save,wheel_zoom", toolbar_location="right")
        
        genders = ['Male', 'Female']
        colors = ["#718dbf", "#e84d60"]
                  
        self.plot1.vbar_stack(genders, x='Quartier', width=0.75, color=colors, source=dataSource, 
                         legend=[value(x) for x in genders], line_width=0.1)
                 
        # Designing the plot (legend, axis alignment & spacing)
        self.plot1.y_range.start = 0
        self.plot1.xaxis.major_label_orientation = 1
        self.plot1.x_range.range_padding = 0.05
        self.plot1.xgrid.grid_line_color = None
        
        #Creating the hover tooltip
        hover = HoverTool(tooltips=[("Gender", "@"), ("Births", "@Male")])        
        self.plot1.tools.append(hover)
        
        self.plot1.legend.location = "top_right"
        self.plot1.legend.orientation = "horizontal"