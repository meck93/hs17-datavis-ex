# -*- coding: utf-8 -*-

""" Data Visualization HS 17
    Implemenation of Exercise 1
    
    Moritz Eck - 14 715 296"""
    
import pandas as pd
from bkcharts import Donut
from bokeh.models import Title

class Figure4:
    """ This class creates the fourth figure (wedge) of exercise 1 """
    
    def __init__(self, data):
        self.data = data
        self.plot = self.createFigure4()
        
    def createFigure4(self):
        data = self.data
        
        # Only use year 2015
        data = data.loc[data['Jahr'] == 2015]
        
        # Only use the quartier Oerlikon 
        data = data.loc[data['Quartier'] == 'Oerlikon']
        
        # Removing the unnecessary columns
        data = data.drop("SexCd", axis=1)
        data = data.drop("StatZoneSort", axis=1)
        data = data.drop("QuarSort", axis=1)
        data = data.drop("Jahr", axis=1)
        data = data.drop("Quartier", axis=1)
        
        # Sorting the Quartier: Oerlikon according to the top five most births in 2015
        data = data.groupby(['StadtZone'])['Births'].sum().reset_index()
        data = data.sort_values('Births', ascending=False)
        data = data.head(5).reset_index(drop=True)
       
        # Creating a combined dataframe
        dataSource = pd.Series(data['Births'].values, index=data['StadtZone'].values)
        
        # Plotting the Pie Chart
        pie_chart = Donut(dataSource, hover_text='Births')
        
        # Designing the Donut
        pie_chart.title = Title(text="Ratio of the Top 5 Statistical Zones in Zürich Oerlikon in 2015")
        pie_chart.width = 450
        pie_chart.height = 500
                
        return pie_chart