# -*- coding: utf-8 -*-
"""
Data Visualization HS 17 - Exercise 4
Moritz Eck - 14-715-296

The idea is to use this script to read the whole dataset into memory,
such that it doesn't have to be read before every execution. 
"""

import numpy as np

RESOURCES = 'resources/'

def read_terrain_data():
    filename = RESOURCES + "HGTdata.bin"
    return np.memmap(filename, dtype=">f", mode="r", shape=(500, 500))

def read_geo_data(datatype, hour):
    # formating the hour input to string and format '##'
    str_hour = str(hour)
    
    if hour < 10:
        str_hour = '0' + str_hour

    filename = RESOURCES + datatype + 'f' + str_hour + '.bin'
    return np.memmap(filename, dtype=">f", mode="r", shape=(500, 500, 100), order='F')

def computeMean(values):
    return sum(values) / len(values)
