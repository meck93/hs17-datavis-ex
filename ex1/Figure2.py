# -*- coding: utf-8 -*-

""" Data Visualization HS 17
    Implemenation of Exercise 1
    
    Moritz Eck - 14 715 296"""

import pandas as pd

from bokeh.models import HoverTool
from bokeh.plotting import figure

class Figure2:
    """ This class creates the second figure (plot of three lines) of exercise 1 """
    
    def __init__(self, data):
        self.data = data
        self.plot2 = self.createFigure2()
    
    def createFigure2(self):
        data = self.data
        
        # Removing the unnecessary columns
        data = data.drop("SexCd", axis=1)
        data = data.drop("StatZoneSort", axis=1)
        data = data.drop("StadtZone", axis=1)
        data = data.drop("Quartier", axis=1)
        data = data.drop("QuarSort", axis=1)
        
        #X-Axis Values: The years 1993 - 2015 as a list
        years = []
        
        for year in data['Jahr']:
            if year not in years:
                years.append(year)
            
        years.sort()
        
        # Dataframe: Total births per year
        totalBirths = pd.DataFrame(data)
        totalBirths = totalBirths.drop("Sex", axis=1) 
        totalBirths = totalBirths.groupby("Jahr").sum()        
        
        # Dataframe: Total female births per year
        femaleBirths = pd.DataFrame(data.loc[data['Sex'] == 'W'], copy=True)
        femaleBirths = femaleBirths.drop("Sex", axis=1) 
        femaleBirths = femaleBirths.groupby("Jahr").sum()
        
        # Dataframe: Total male births per year
        maleBirths = pd.DataFrame(data.loc[data['Sex'] == 'M'], copy=True)
        maleBirths = maleBirths.drop("Sex", axis=1)
        maleBirths = maleBirths.groupby("Jahr").sum()

        # Plotting all three dataframes as seperate lines
        plot2 = figure(title="Number of Births between 1993 and 2015",
                       plot_width=900, plot_height=500,
                       tools="pan,reset,save,wheel_zoom", toolbar_location="right")
               
        #Plotting the male births
        plot2.line(x=years, y=maleBirths['Births'].values.tolist(),
                   legend='Male', color='red', line_width=2)
        plot2.circle(x=years, y=maleBirths['Births'].values.tolist(), 
                     line_width=1.5, fill_color='white', line_color='black')
        
        #Plotting the female births
        plot2.line(x=years, y=femaleBirths['Births'].values.tolist(),
                   legend='Female', color='blue', line_width=2)        
        plot2.circle(x=years, y=femaleBirths['Births'].values.tolist(), 
                     line_width=1.5, fill_color='white', line_color='black')
        
        #Plotting the total births
        plot2.line(x=years, y=totalBirths['Births'].values.tolist(),
                   legend='Total', color='black', line_width=2)
        plot2.circle(x=years, y=totalBirths['Births'].values.tolist(), 
                     line_width=1.5, fill_color='white', line_color='black')
                    
        # Designing the plot (legend, axis alignment & spacing)
        plot2.y_range.start = 0
        plot2.x_range.start = 1992        
                
        #Creating the hover tooltip
        hover = HoverTool(tooltips=[("Year", "@x"), ("Births", "@y")])
        plot2.tools.append(hover)
        
        # X-Axis design
        plot2.xaxis[0].ticker.max_interval = 1
        plot2.xaxis[0].ticker.num_minor_ticks = 0
        plot2.xgrid.grid_line_color = None
        plot2.xaxis.axis_label = 'Years'
        
        # Y-Axis design 
        plot2.yaxis[0].ticker.max_interval = 500
        plot2.yaxis[0].ticker.num_minor_ticks = 5
        plot2.yaxis.axis_label = 'Number of Births'
                
        # Legend 
        plot2.legend.location = "bottom_right"
        plot2.legend.orientation = "horizontal"
        
        return plot2