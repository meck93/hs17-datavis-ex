# -*- coding: utf-8 -*-
""" Data Visualization HS 17
    Implemenation of Exercise 3
    
    Moritz Eck - 14 715 296"""          

def readCSV(filename):
    """
    Reads the .data file and creates a list of the rows
    
    Input
    filename - string - filename of the input data file
    
    Output
    data - list containing all rows of the csv as elements
    """
    import csv
    
    data = []
    with open(filename, 'rt', encoding='utf8') as csvfile:
        lines = csv.reader(csvfile)
        for row in lines:
            data.append(row)
    
    return data

def splitDataSet(data, split):
    """
    Split the datat set into two sub-sets (training, test) of approximately sizes: 70% / 30%
    """
    import random
    
    training_set = []
    test_set = []

    for x in range(len(data)-1):
        # Convert the first four entries of each row into type: float
        for y in range(4):
            data[x][y] = float(data[x][y])
        
        # split the data set into training and test set 
        # according to the value of the split criterion
        if random.random() < split:
            training_set.append(data[x])
        else:
            test_set.append(data[x])
    
    return training_set, test_set

def euclideanDistance(element1, element2, length):
    """
    Computes the euclidean width between two entires
    """
    import math
    
    distance = 0
    
    for x in range(length):
        distance += pow((element1[x] - element2[x]), 2)
        
    return math.sqrt(distance)

def getNeighbors(training_set, test_instance, k_neighbors):
    """
    Computes the k-nearest neighbors of the test_instance on the set of training images
    
    Input
    training_set
    test_instance
    k_neighbors
    
    Output
    neighbors - list - the k-nearest neighbors
    weights - list - the distance of each neighbor to the test_instance (weight of each vote)
    
    """
    import operator
    
    distances = []
    # Ensure the distance is only computed without taking the last value into account 
    # Last value = label of the instance
    length = len(test_instance) - 1
    
    # Compute the Euclidean widths between the current test_instance and each training_instance
    for x in range(len(training_set)):
        dist = euclideanDistance(test_instance, training_set[x], length)
        distances.append((training_set[x], dist))
        
    # Sort the distances by the shortest distance
    distances.sort(key=operator.itemgetter(1))
    
    neighbors = []
    weights = []
    
    # create a list of all neighbors and their associated voting-weight (distance to test_instance)
    for x in range(k_neighbors):
        neighbors.append(distances[x][0])
        weights.append(distances[x][1])
        
    return neighbors, weights

def getPrediction(neighbors, weights):
    """
    Computes the weighted vote of each of the k-neighbors
    Adds up all votes of each entry. And retruns the key of the entry with the highest number of votes.
    """
    import operator
    
    votes = {}
    
    for x in range(len(neighbors)):        
        response = neighbors[x][-1]
                
        # value exists
        # weight = 0 => add 1
        # weight != 0 => add 1/weights[x]
        if response in votes:
            if weights[x] == float(0):
                votes[response] += 1
            else:
                votes[response] += 1/weights[x]
                
        # value doesn't exist yet
        # weight = 0 => add 1 
        # weight != 0 => add 1/weights[x]
        else:
            if weights[x] == float(0):
                votes[response] = 1
            else:
                votes[response] = 1/weights[x]
    
    # Sort the keys in the dictionary of entries in desc order
    # according the the entry with the highest # of votes                  
    sortedVotes = sorted(votes.items(), key=operator.itemgetter(1),reverse=True)
    
    # return the entry with the highest vote
    return sortedVotes[0][0]

def getAccuracy(test_set, predictions):
    """
    Computes the accuracy of the k-nearest neighbor algorithm: 
    Comparing the prediction of the label and the actual result
    """
    correct = 0
    wrong_guesses = []
    correct_instead = []
    
    # check if the label of the test_set[x] is the prediction
    for x in range(len(test_set)):        
        if test_set[x][-1] == predictions[x]:
            correct += 1
        else:
            wrong_guesses.append(predictions[x])
            correct_instead.append(test_set[x])
    
    # Compute the accuracy of the whole test
    accuracy = (correct/float(len(test_set)))*100.0   
    
    return (accuracy, wrong_guesses, correct_instead)

def visualize(test_set, wrong_guesses, correct_instead):   
    from bokeh.plotting import figure
    from bokeh.io import output_file, show
            
    # 3 sepearte dataframes for each type - only the correct values
    setosa = []
    setosa_x_values = []
    setosa_y_values = []
    
    versicolor = []
    versicolor_x_values = []
    versicolor_y_values = []
    
    virginica = []
    virginica_x_values = []
    virginica_y_values = []  
    
    for i in range(0, len(test_set)):
        if test_set[i][-1] == "Iris-setosa":
            setosa.append(test_set[i])
            setosa_x_values.append(test_set[i][0])
            setosa_y_values.append(test_set[i][1])
            
        elif test_set[i][-1] == "Iris-versicolor":
            versicolor.append(test_set[i])
            versicolor_x_values.append(test_set[i][0])
            versicolor_y_values.append(test_set[i][1])
            
        elif test_set[i][-1] == "Iris-virginica":
            virginica.append(test_set[i])
            virginica_x_values.append(test_set[i][0])
            virginica_y_values.append(test_set[i][1])
    
    # same procedure wrong guesses
    wrong_x_values = []
    wrong_y_values = []
    
    for i in range(0, len(correct_instead)):
        wrong_x_values.append(correct_instead[i][0])
        wrong_y_values.append(correct_instead[i][1])
    
    # Plotting all three dataframes as seperate circles
    fig = figure(title="K-Nearest Neighbor on Test-Set",
                  plot_width=600, 
                  plot_height=400,
                  tools="pan,reset,save,wheel_zoom", 
                  toolbar_location="right")
               
    #Plotting the setosa
    fig.circle(x=setosa_x_values, 
                y=setosa_y_values, 
                fill_color='black',
                line_color='white',
                legend='setosa')
    
    #Plotting the setosa
    fig.circle(x=versicolor_x_values, 
                y=versicolor_y_values, 
                fill_color='green',
                line_color='white',
                legend='versicolor')
    
    #Plotting the setosa
    fig.circle(x=virginica_x_values, 
                y=virginica_y_values, 
                fill_color='blue',
                line_color='white',
                legend='virginica')
    
    #Plotting the wrongly guessed values
    fig.circle(x=wrong_x_values, 
                y=wrong_y_values, 
                fill_color='red',
                line_color='white',
                legend='wrongly guessed')
    
    #X-Axis design 
    fig.xaxis.axis_label = 'Sepal Length'
        
    #Y-Axis design 
    fig.yaxis.axis_label = 'Sepal Width'
    
    show(fig)  

# =============================================================================
# Main Programm
# =============================================================================
   
# Load the data
data = readCSV('iris.data')

# Remove the header
data = data[1:]

# Split the dataset into training and test set
training_set, test_set = splitDataSet(data, 0.7)

predictions = []

# Compute the k-nearest neighbor for every test_instance
for i in range(len(test_set)):
    # Computes the neighbors and the weights of each vote of each neighbor
    neighbors, weights = getNeighbors(training_set, test_set[i], 5)
    
    # Lets the neighbors vote & returns the prediction
    guess = getPrediction(neighbors, weights)
    predictions.append(guess)

result = getAccuracy(test_set, predictions)

visualize(test_set, result[1], result[2])