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

def computeMax(datagroup):
    # Seperate each column (attribute)
    sepal_length = datagroup[:, 0]
    sepal_width = datagroup[:, 1]
    petal_length = datagroup[:, 2]
    petal_width = datagroup[:, 3]

    # Compute the max value of each attribute
    max_sepal_length = max(sepal_length)
    max_sepal_width = max(sepal_width)
    max_petal_length = max(petal_length)
    max_petal_width = max(petal_width)

    return max_sepal_length, max_sepal_width, max_petal_length, max_petal_width

def computeMin(datagroup):
    # Seperate each column (attribute)
    sepal_length = datagroup[:, 0]
    sepal_width = datagroup[:, 1]
    petal_length = datagroup[:, 2]
    petal_width = datagroup[:, 3]

    # Compute the min values of each attribute
    min_sepal_length = min(sepal_length)
    min_sepal_width = min(sepal_width)
    min_petal_length = min(petal_length)
    min_petal_width = min(petal_width)

    return min_sepal_length, min_sepal_width, min_petal_length, min_petal_width 

def computeMean(datagroup):
    # Seperate each column (attribute)
    sepal_length = datagroup[:, 0]
    sepal_width = datagroup[:, 1]
    petal_length = datagroup[:, 2]
    petal_width = datagroup[:, 3]

    # Compute the mean of each attribute
    mean_sepal_length = sum(sepal_length) / len(sepal_length)
    mean_sepal_width = sum(sepal_width) / len(sepal_width)
    mean_petal_length = sum(petal_length) / len(petal_length)
    mean_petal_width = sum(petal_width) / len(petal_width)

    return mean_sepal_length, mean_sepal_width, mean_petal_length, mean_petal_width

def computeDeviationGroup(datagroup):
    # Seperate each column (attribute)
    sepal_length = datagroup[:, 0]
    sepal_width = datagroup[:, 1]
    petal_length = datagroup[:, 2]
    petal_width = datagroup[:, 3]

    # Compute the means of the group
    means = computeMean(datagroup)

    # Compute the standard deviation of each intra class
    stand_sepal_length = computeStandardDeviation(sepal_length, means[0])
    stand_sepal_width = computeStandardDeviation(sepal_width, means[1])
    stand_petal_length = computeStandardDeviation(petal_length, means[2])
    stand_petal_width = computeStandardDeviation(petal_width, means[3])

    return stand_sepal_length, stand_sepal_width, stand_petal_length, stand_petal_width

def computeStandardDeviation(datatype, mean):
    """Computes the standard deviation of the inputed data values
    """
    import math

    sum = 0

    for row in datatype:
        sum += (float(row) - mean)**2
    
    return round(math.sqrt(sum / len(datatype)), 3)

def computeStatistics(data):
    """Computes the min, max, mean and standard deviation of a flower
    """
    class_min = computeMin(data)
    class_max = computeMax(data)
    class_mean = computeMean(data)
    class_stand = computeDeviationGroup(data)

    return class_min, class_max, class_mean, class_stand

def printSpecies(flower, name):
    stats_values = computeStatistics(flower)

    flower_spec = ["Sepal Length: ", "Sepal Width: ", "Petal Length: ", "Petal Width: "]
    stats_names = ["Min: ", "Max: ", "Mean: ", "Standard deviation: "]

    print("\n#####\tSpecies Type: " + name + "\t#####")

    for j in range(0, len(stats_values)):
        print("")
        for i in range(0, len(stats_values[j])):
            # First Row (min) of a flower type
            if i == 0:
                print(flower_spec[j] + "\t" + stats_names[i] + "\t\t\t" + str(stats_values[i][j]))
            elif i < 3:
                # print row max and mean
                print("\t\t" + stats_names[i] + "\t\t\t" + str(stats_values[i][j]))
            else:
                # print standard deviation row
                print("\t\t" + stats_names[i] + "\t" + str(stats_values[i][j]))


# =============================================================================
# Main Program
# =============================================================================

# Load the data from csv
data = readCSV('iris.data')

# Dataset for different types
(setosa, versicolor, virginica) = splitDataIntoGroups(data)

# Total Data Set
total = data[1:]
total = np.array(total)
total = total[:, :-1]
total = np.array(total, dtype=float)

# Print Results
print("\n############### TASK 4 ############### ")
print("The Min, Max, Mean and Standard Deviation per Flower Type and in Total:")
printSpecies(setosa, "Setosa")
printSpecies(versicolor, "Versicolor")
printSpecies(virginica, "Virginica")
printSpecies(total, "Total")

''' This is what the printout looks like 

Species Type: Setosa

Sepal Length:   Min:                    4.3
                Max:                    5.8
                Mean:                   5.006
                Standard deviation:     0.349

Sepal Width:    Min:                    2.3
                Max:                    4.4
                Mean:                   3.418
                Standard deviation:     0.377

Petal Length:   Min:                    1.0
                Max:                    1.9
                Mean:                   1.464
                Standard deviation:     0.172

Petal Width:    Min:                    0.1
                Max:                    0.6
                Mean:                   0.244
                Standard deviation:     0.106

Species Type: Versicolor

Sepal Length:   Min:                    4.9
                Max:                    7.0
                Mean:                   5.936
                Standard deviation:     0.511

Sepal Width:    Min:                    2.0
                Max:                    3.4
                Mean:                   2.77
                Standard deviation:     0.311

Petal Length:   Min:                    3.0
                Max:                    5.1
                Mean:                   4.26
                Standard deviation:     0.465

Petal Width:    Min:                    1.0
                Max:                    1.8
                Mean:                   1.326
                Standard deviation:     0.196

Species Type: Virginica

Sepal Length:   Min:                    4.9
                Max:                    7.9
                Mean:                   6.588
                Standard deviation:     0.629

Sepal Width:    Min:                    2.2
                Max:                    3.8
                Mean:                   2.974
                Standard deviation:     0.319

Petal Length:   Min:                    4.5
                Max:                    6.9
                Mean:                   5.552
                Standard deviation:     0.546

Petal Width:    Min:                    1.4
                Max:                    2.5
                Mean:                   2.026
                Standard deviation:     0.272

Species Type: Total

Sepal Length:   Min:                    4.3
                Max:                    7.9
                Mean:                   5.84333333333
                Standard deviation:     0.825

Sepal Width:    Min:                    2.0
                Max:                    4.4
                Mean:                   3.054
                Standard deviation:     0.432

Petal Length:   Min:                    1.0
                Max:                    6.9
                Mean:                   3.75866666667
                Standard deviation:     1.759

Petal Width:    Min:                    0.1
                Max:                    2.5
                Mean:                   1.19866666667
                Standard deviation:     0.761 '''
