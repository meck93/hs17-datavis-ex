# -*- coding: utf-8 -*-

""" Data Visualization HS 17
    Implemenation of Exercise 1
    
    Moritz Eck - 14 715 296"""

import pandas as pd

from bkcharts import Bar
from bokeh.models import HoverTool

class Figure1:
    """ This class creates the first figure (aggregated briths per city part) of exercise 1 """
    
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
        births = births.drop("Jahr", axis=1)        
        births = births.groupby(['Sex', 'Quartier'])['Births'].sum().reset_index()        
        
        colors = ["#e84d60", "#718dbf"]
        
        #Creating the vertical stacked bar chart            
        self.plot1 = Bar(births, label='Quartier', stack='Sex', values='Births', 
                         title='Aggregated Number of Births per City Part (Quartier) in 2015',
                         color=colors, )
                 
        # Designing the plot (legend, axis alignment & spacing)
        self.plot1.width = 1800
        self.plot1.height = 500
        self.plot1.legend.location = "top_right"
        self.plot1.legend.orientation = "horizontal"
        
        #X-Axis design 
        self.plot1.xaxis.major_label_orientation = 1
        self.plot1.x_range.range_padding = 0.05
        self.plot1.xgrid.grid_line_color = None
        self.plot1.xaxis.axis_label = 'City Parts in Zurich'
        
        #Y-Axis design 
        self.plot1.y_range.start = 0
        self.plot1.yaxis[0].ticker.max_interval = 50
        self.plot1.yaxis[0].ticker.num_minor_ticks = 0
        self.plot1.yaxis.axis_label = 'Number of Births'
        
        #Creating the hover tooltip
        hover = HoverTool(tooltips=[("Quartier", "@Quartier"), ("Sex", "@Sex"), ("Births", "@height")])        
        self.plot1.tools.append(hover)