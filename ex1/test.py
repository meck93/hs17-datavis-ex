# -*- coding: utf-8 -*-

import pandas as pd

from bokeh.io import output_file, show
from bokeh.plotting import figure

#New visualization page 
output_file("output.html", title="Data Visualization Exercise 1")

#Read the data from the CSV file
data = pd.read_csv('births.csv', delimiter=',')
data = data.rename(columns={"StichtagDatJahr":"Jahr","SexKurz":"Sex", "StatZoneLang":"StadtZone", "QuarLang":"Quartier","AnzGebuWir":"Births"})
   
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
plot2 = figure(title="Births per year and gender in Zurich",
               plot_width=1000, plot_height=600,
               tools="pan,reset,save,wheel_zoom", toolbar_location="right")

plot2.multi_line(xs=[years, years, years], ys=[maleBirths['Births'].values.tolist(), femaleBirths['Births'].values.tolist(), totalBirths['Births'].values.tolist()], color=["blue", "red", "black"], line_width=2)

show(plot2)