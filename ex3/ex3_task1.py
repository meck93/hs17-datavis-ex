# -*- coding: utf-8 -*-

""" Data Visualization HS 17
    Implemenation of Exercise 3
    
    Moritz Eck - 14 715 296"""
               
def readDataSet(filename, separator, split):
    import pandas as pd
    
    return pd.read_csv(filename, sep=separator, encoding='utf8')

def visualize_plot1():   
    import pandas as pd
    from bokeh.plotting import figure
    from bokeh.io import output_file, show

    output_file("ex3_task1.html")
    
    # Read the raw data from the 'iris.data' file
    data = readDataSet('iris.data', ',', 0.7)
    
    # 3 sepearte dataframes for each type
    setosa = pd.DataFrame(data.loc[data['species'] == "Iris-setosa"], copy=True)
    versicolor = pd.DataFrame(data.loc[data['species'] == "Iris-versicolor"], copy=True)
    virginica = pd.DataFrame(data.loc[data['species'] == "Iris-virginica"], copy=True)
    
    # x & y value extraction for each type
    setosa_x_values = list(setosa['sepal_length'])
    setosa_y_values = list(setosa['sepal_width'])
    
    versicolor_x_values = list(versicolor['sepal_length'])
    versicolor_y_values = list(versicolor['sepal_width'])
    
    virginica_x_values = list(virginica['sepal_length'])
    virginica_y_values = list(virginica['sepal_width'])
    
    # Plotting all three dataframes as seperate circles
    fig1 = figure(title="Sepal Length and Widths",
                  plot_width=600, 
                  plot_height=400,
                  tools="pan,reset,save,wheel_zoom", 
                  toolbar_location="right")
               
    #Plotting the setosa
    fig1.circle(x=setosa_x_values, 
                y=setosa_y_values, 
                fill_color='black',
                line_color='white',
                legend='setosa')
    
    #Plotting the setosa
    fig1.circle(x=versicolor_x_values, 
                y=versicolor_y_values, 
                fill_color='green',
                line_color='white',
                legend='versicolor')
    
    #Plotting the setosa
    fig1.circle(x=virginica_x_values, 
                y=virginica_y_values, 
                fill_color='blue',
                line_color='white',
                legend='virginica')
    
    #X-Axis design 
    fig1.xaxis.axis_label = 'Sepal Length'
        
    #Y-Axis design 
    fig1.yaxis.axis_label = 'Sepal Width'
    
    show(fig1)    

# =============================================================================
# Main Program
# =============================================================================
visualize_plot1()
