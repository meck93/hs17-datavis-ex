# -*- coding: utf-8 -*-

""" Data Visualization HS 17
    Implemenation of Exercise 1
    
    Moritz Eck - 14 715 296"""

import pandas as pd
from bkcharts import Donut
from bokeh.models import Title

class Figure3:
    """ This class creates the thrid figure (pie chart) of exercise 1 """
    
    def __init__(self, data):
        self.data = data
        self.pie_chart = self.createFigure()
    
    def createFigure(self):
        data = self.data
        
        # Only use year 2015
        data = data.loc[data['Jahr'] == 2015]
        
        # Removing the unnecessary columns
        data = data.drop("SexCd", axis=1)
        data = data.drop("StatZoneSort", axis=1)
        data = data.drop("StadtZone", axis=1)
        data = data.drop("Quartier", axis=1)
        data = data.drop("QuarSort", axis=1)
        data = data.drop("Jahr", axis=1)
                
        # Dataframe: Total female births per year
        femaleBirths = pd.DataFrame(data.loc[data['Sex'] == 'W'], copy=True)
        femaleBirths = femaleBirths.drop("Sex", axis=1) 
        femaleBirths = femaleBirths.sum()
        
        # Dataframe: Total male births per year
        maleBirths = pd.DataFrame(data.loc[data['Sex'] == 'M'], copy=True)
        maleBirths = maleBirths.drop("Sex", axis=1)
        maleBirths = maleBirths.sum()
              
        # Calculating the percentages of the births in relation to the total amount
        totalBirths = maleBirths['Births'] + femaleBirths['Births']
        male_percentage = (maleBirths['Births'] / totalBirths)*100     
        female_percentage = (femaleBirths['Births'] / totalBirths)*100
        
        # Creating the labels of the pie-chart
        male_label = "Male Births: {0}%".format(round(male_percentage, 2))
        female_label = "Female Births: {0}%".format(round(female_percentage, 2))
                
        # Creating a combined dataframe
        data = pd.Series([maleBirths['Births'], femaleBirths['Births']], index=[male_label, female_label])
        
        # Plotting the Pie Chart
        pie_chart = Donut(data, color=['blue', 'red'], hover_text='Births')
        
        # Designing the Donut
        pie_chart.title = Title(text="Ratio Male vs. Female Births in 2015")        
        pie_chart.width = 450
        pie_chart.height = 500
                
        return pie_chart