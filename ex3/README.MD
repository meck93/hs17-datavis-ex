### Exercise 3 - Data Visualization - HS 17 - University of Zurich
_Moritz Eck - 14 715 296_

#### How to run this project?
* Python Version 3.6.2 & Bokeh 0.12.10
* Run all files in the commandline using the command:  __python ex3_main.py__
* Use the following command to run an individual file: __python ex3-task[_number_].py__
* Change the __number__ by an value: 1, 2, 4, 6, 7

For tasks 4, 6, 7 the result will be printed to the command line.
For task 1 and 2 (includes task3) a browers window will open with the respective plot. 

##### Other Files
* For both plots (task 1 & task 2/3), a html and jpg file is additionally attached.

##### Questions
Question 1: What type of variables has the Iris dataset? Refer the type of each variable.
* sepal_length: continuous variable (ordinal, numerical value)
* sepal_width: continuous variable (ordinal, numerical value)
* petal_length: continuous variable (ordinal, numerical value)
* petal_width: continuous variable (ordinal, numerical value)
* species: categorical variable (nominal, no intrinsic order)

Question 2: How many features are included in the Iris data set? Definition of a feature? 
* If each attribute is a feature then the dataset contains four features
* If the plot is referenced then the graphic has three features x & y coordinate and the color of the circle

Question 3 - Compare the clustering results with the original data?
* The error rate is very low. Only a very small number of values are erronous. 
* The training data set is therefore very accurate. Accuracy >= 95% in most of the executions. 
* A value that is wrongly classified mostly originates from the classes of Iris-versicolor and Iris-virginica. Iris-setosa values are almost always correclty classified as they're not as similiar as the other two clusters. 

Qustion 4 - What should be done to avoid overly dominat values or attributes? 
* The values need to be normalized to a range between 0 and 1 => Standard distribution with mean = 0 and standard deviation = 1.  

Question 5 - Which class presents the highest intraclass correlation? 
* The Iris-setosa cluster has the highest intraclass correlation between the sepal length and width.
* Correlation Value = 0.747

Question 6 - Which cluster presents the highest similarity and which one the highest dissimilarity? 
Highest similarity: Iris-versicolor vs. Iris-virginica
* Value: 0.3816

Highest dissimilarity: Iris-setosa vs. Iris-virginica
* Value: 4.7526

##### Data used for Question 6
Setosa vs. Versicolor
Dissimilarity:   3.2052
Similarity:      0.2378

Setosa vs. Virginica
Dissimilarity:   4.7526
Similarity:      0.1738

Versicolor vs. Virginica
Dissimilarity:   1.6205
Similarity:      0.3816