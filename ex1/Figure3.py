# -*- coding: utf-8 -*-

""" Data Visualization HS 17
    Implemenation of Exercise 1
    
    Moritz Eck - 14 715 296"""

import pandas as pd

from bokeh.models import HoverTool
from bkcharts import Donut, show

class Figure3:
    """ This class creates the thrid figure (pie chart) of exercise 1 """
    
    def __init__(self, data):
        self.data = data
        self.pie_chart = self.createFigure()
    
    def createFigure(self):
        data = self.data
        
        # Removing the unnecessary columns
        data = data.drop("SexCd", axis=1)
        data = data.drop("StatZoneSort", axis=1)
        data = data.drop("StadtZone", axis=1)
        data = data.drop("Quartier", axis=1)
        data = data.drop("QuarSort", axis=1)
                
        # Dataframe: Total female births per year
        femaleBirths = pd.DataFrame(data.loc[data['Sex'] == 'W'], copy=True)
        femaleBirths = femaleBirths.drop("Sex", axis=1) 
        femaleBirths = femaleBirths.drop("Jahr", axis=1)
        femaleBirths = femaleBirths.sum()
        
        # Dataframe: Total male births per year
        maleBirths = pd.DataFrame(data.loc[data['Sex'] == 'M'], copy=True)
        maleBirths = maleBirths.drop("Sex", axis=1)
        maleBirths = maleBirths.drop("Jahr", axis=1)
        maleBirths = maleBirths.sum()
        
        data = pd.Series([maleBirths['Births'], femaleBirths['Births']], index=['Male', 'Female'])
        
        pie_chart = Donut(data, color=['blue', 'red'], hover_text='Births')
        
        return pie_chart