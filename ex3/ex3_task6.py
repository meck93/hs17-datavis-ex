# -*- coding: utf-8 -*-

""" Data Visualization HS 17
    Implemenation of Exercise 3
    
    Moritz Eck - 14 715 296"""
    
import numpy as np

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

def splitDataIntoGroups(data):        
    # 3 sepearte dataframes for each type
    setosa = []
    versicolor = []
    virginica = []
    
    for entry in data:
        if entry[4] == 'Iris-setosa':
            setosa.append(entry)
        elif entry[4] == 'Iris-versicolor':
            versicolor.append(entry)
        elif entry[4] == 'Iris-virginica':
            virginica.append(entry)

    # Convert to numpy array
    setosa = np.array(setosa)
    versicolor = np.array(versicolor)
    virginica = np.array(virginica)

    # Remove the last column: species_names
    setosa = np.array(setosa[:, :-1], dtype=float)
    versicolor = np.array(versicolor[:, :-1], dtype=float)
    virginica = np.array(virginica[:, :-1], dtype=float)
    
    return setosa, versicolor, virginica

def computeMean(datagroup):
    # Seperate each column 
    sepal_length = datagroup[:, 0]
    sepal_width = datagroup[:, 1]

    # Compute the mean
    mean_sepal_length = sum(sepal_length) / len(sepal_length)
    mean_sepal_width = sum(sepal_width) / len(sepal_width)

    return mean_sepal_length, mean_sepal_width

def computeDeviationGroup(datagroup):
    # Seperate each column 
    sepal_length = datagroup[:, 0]
    sepal_width = datagroup[:, 1]

    # Compute the means of the group
    means = computeMean(datagroup)

    # Compute the standard deviation of each intra class
    stand_sepal_length = computeStandardDeviation(sepal_length, means[0])
    stand_sepal_width = computeStandardDeviation(sepal_width, means[1])

    return stand_sepal_length, stand_sepal_width

def computeStandardDeviation(datatype, mean):
    """Comutes the standard deviation of the datatype values"""
    import math

    sum = 0

    for row in datatype:
        sum += (float(row) - mean)**2
    
    return math.sqrt(sum / len(datatype))

def correlateLengthWidth(flower_data):
    
    # Seperate each column 
    sepal_length = flower_data[:, 0]
    sepal_width = flower_data[:, 1]

    (mean_length, mean_width) = computeMean(flower_data)
    (std_length, std_width) = computeDeviationGroup(flower_data)

    return computeCorrelation(sepal_length, mean_length, std_length, sepal_width, mean_width, std_width)

def computeCorrelation(length, length_mean, length_std, width, width_mean, width_std):
    """Computes the correlation of the input data"""
    if not len(length) == len(width):
        print("Length of inputs don't match")
        return None

    sum = 0

    # compute the covariance
    for i in range(0, len(length)):
        sum += (length[i] - length_mean) * (width[i] - width_mean)

    covariance = sum / len(length)

    # divide by the product of the two std (pearson correlation coefficient)
    return round(covariance / (length_std * width_std), 6)

# =============================================================================
# Main Program
# =============================================================================

# Load the data from csv
data = readCSV('iris.data')

# Dataset for different types
(setosa, versicolor, virginica) = splitDataIntoGroups(data)

# headline of task 6
print("\n############### TASK 6 ############### ")
print("Sepal Length and Width - Correlation")

# setosa correlation
print("... of the Setosa flower type.")
print(correlateLengthWidth(setosa))
print()

# versicolor correlation
print("... of the Versicolor flower type")
print(correlateLengthWidth(versicolor))
print()

# virginica correlation
print("... of the Virginica flower type.")
print(correlateLengthWidth(virginica))
print()
