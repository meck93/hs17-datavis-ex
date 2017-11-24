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

def computeMeanAttributes(flower):
    # Seperate each column 
    sepal_length = flower[:, 0]
    sepal_width = flower[:, 1]
    petal_length = flower[:, 2]
    petal_width = flower[:, 3]
    
    # Compute the mean for each attribute of the flower type
    mean_sepal_length = sum(sepal_length) / len(sepal_length)
    mean_sepal_width = sum(sepal_width) / len(sepal_width)
    mean_petal_length = sum(petal_length) / len(petal_length)
    mean_petal_width = sum(petal_width) / len(petal_width)

    return mean_sepal_length, mean_sepal_width, mean_petal_length, mean_petal_width

def euclideanDistance(point1, point2):
    """Computes the euclidean width between two entires.
    Same function as in task 2.
    """
    import math

    if not len(point1) == len(point2):
        print("Wrong dimensions!")
        return None

    dist = 0
    
    for x in range(len(point1)):
        dist += pow((point1[x] - point2[x]), 2)

    return math.sqrt(dist)

def dissimilarity(vector1, vector2):
    """
    Computes the dissimilarity between two vectors.
    In this case the vectors contain the mean values of each attribute. 
    """

    return round(euclideanDistance(vector1, vector2), 4)

def similarity(vector1, vector2):
    """
    Computes the similarity between two vectors.
    In this case the vectors cointain the mean values of each attribute.
    """
    return round(1 / (1 + dissimilarity(vector1, vector2)), 4)

# =============================================================================
# Main Program
# =============================================================================

# Load the data from csv
data = readCSV('iris.data')

# Dataset per flower types
(setosa, versicolor, virginica) = splitDataIntoGroups(data)

# Mean vectors per flower type
setosa_means = computeMeanAttributes(setosa)
versicolor_means = computeMeanAttributes(versicolor)
virginica_means = computeMeanAttributes(virginica)

# Task 7 - Headline
print("Below the dissimilarities and similarities between the different flower types can be seen:\n")

# Compute the dissimilarity and similarity between setosa and versicolor
dis_setosa_versicolor = dissimilarity(setosa_means, versicolor_means)
sim_setosa_versicolor = similarity(setosa_means, versicolor_means)

print("1. Setosa vs. Versicolor")
print("Dissimilarity:\t", dis_setosa_versicolor, "\nSimilarity:\t", sim_setosa_versicolor)

# Compute the dissimilarity and similarity between setosa and versicolor
dis_setosa_virginica = dissimilarity(setosa_means, virginica_means)
sim_setosa_virginica = similarity(setosa_means, virginica_means)

print("\n2. Setosa vs. Virginica")
print("Dissimilarity:\t", dis_setosa_virginica, "\nSimilarity:\t", sim_setosa_virginica)

# Compute the dissimilarity and similarity between setosa and versicolor
dis_versicolor_virginica = dissimilarity(versicolor_means, virginica_means)
sim_versicolor_virginica = similarity(versicolor_means, virginica_means)

print("\n3. Setosa vs. Versicolor")
print("Dissimilarity:\t", dis_versicolor_virginica, "\nSimilarity:\t", sim_versicolor_virginica)

"""
This is what the printout looks like...
Below the dissimilarities and similarities between the different flower types can be seen:

1. Setosa vs. Versicolor
Dissimilarity:   3.2052
Similarity:      0.2378

2. Setosa vs. Virginica
Dissimilarity:   4.7526
Similarity:      0.1738

3. Setosa vs. Versicolor
Dissimilarity:   1.6205
Similarity:      0.3816
"""
