# Exercise 4 - Data Visualization - HS 17 - University of Zurich

 _Moritz Eck - 14 715 296_

## Prerequisites
* Python Version 3.6.2
* Pandas
* Seaborn 0.8.1
* The data files must be loaded into the /resources folder of the project. The following files are required but were too large to be uploaded: 
  * HGTdata.bin
  * Pf01.bin 
  * QRAINf01.bin 
  * TCf01.bin, TCf02.bin, TCf03.bin, TCf04.bin, TCf05.bin
  * Uf01.bin
  * Vf01.bin
  * Wf01.bin 

## How to run this project?
* Run all files in the commandline using the command:  __python ex4_main.py__
* Use the following command to run an individual file: __python ex4-task[_number_].py__
* Change the __number__ by an value: 1, 2, 3, 4, 5

For all tasks a seperate window with the visualization will open. 

### Notes on Task 5

Unfortunately, I haven't been able to combine both plots into one figure. 
Neither pandas' scatter matrix nor Seaborn's pairplot would allow me to do this. 
The existing figure was always overwritten by the secondary plot.