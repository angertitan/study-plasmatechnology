#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 15:16:24 2020

@author: Jan
"""

import json
import math
import numpy as np
from scipy.integrate import trapz
from random import random
from matplotlib import pyplot as plt


def load_data(path):
    
    file = open(path)
    file_string = file.read()

    data_array = json.loads(file_string)

    x_values = []
    y_values = []
    for data in data_array:
        x_values.append(float(data["wavenumber"]))
        y_values.append(float(data["value"]))

    return [x_values, y_values]


def get_log(data):

    logged_data = []
    
    for d in data:
        logged_d = math.log(d) * -1
        logged_data.append(logged_d)

    return logged_data


def show(data):
    plt.plot(data)

    plt.show()


def cut_peaks(data):
    
    new_data = []
    
    for point in data:
        if point > 0.01:
            new_data.append(random() / 10)
        else:
            new_data.append(point)
            
    return new_data


def get_regr_func(x, y):
    
    n = np.size(x) 
  
    m_x, m_y = np.mean(x), np.mean(y) 
  
    SS_xy = np.sum(y*x) - n*m_y*m_x 
    SS_xx = np.sum(x*x) - n*m_x*m_x 
  
    b_1 = SS_xy / SS_xx 
    b_0 = m_y - b_1*m_x 
  
    def regr_func(x):
        if isinstance(x, int):
            y = b_0 + b_1 * x
            return y

        y_values = []
        for p in x:
            y = b_0 + b_1 * p
            y_values.append(y)
        
        return y_values

    return regr_func


def create_offset_data(interp_func, og_data):

    offset_data = interp_func(og_data)

    return offset_data

def plot_regression_line(x, y, y_pred): 
    plt.scatter(x, y, color = "m", 
               marker = "o", s = 30) 
  
    plt.plot(x, y_pred, color = "g") 
  
    plt.xlabel('x') 
    plt.ylabel('y') 
  
    plt.show() 

def remove_offset(data, y_regr):
    x_values = np.array(data[0])
    y_values = np.array(data[1])
    y_values_regr = np.array(y_regr) - 0.005

    y_values_subtracted = y_values - y_values_regr
    y_values_subtracted[y_values_subtracted < 0] = 0
    
    return x_values, y_values_subtracted


def get_cutout(data, upper_tresh, lower_tresh): 
    x_values = data[0]
    y_values = data[1]

    new_x = []
    new_y = []
    for index, value in enumerate(x_values):
        if value <= upper_tresh and value >= lower_tresh:
            new_x.append(value);
            new_y.append(y_values[index])
    
    return new_x, new_y         


def get_line_strength(data):
    L = 15 # [cm]
    n = 7.369e+16 # [cm^-3]
    
    y_values = np.array(data[1])
    y_values = np.flip(y_values)

    integrated_data = trapz(y_values)
    print('trapz', integrated_data)
    S = (1 / (n * L )) * integrated_data
    
    return S

def plot_new_fig(data, save=False):
    fig = plt.figure()
    plt.gca().invert_xaxis()
    if save:
        fig.tight_layout()
        plt.savefig("./charts/cutout.png", format="png")
    plt.plot(data[0], data[1])

data = load_data('data/parsed/Gruppe3.15.json')
x = data[0]
y = data[1]
log_y = get_log(y)
x_values = np.linspace(0, len(log_y), len(log_y))
regr_func = get_regr_func(x_values, log_y)
y_values_regr = regr_func(x_values)
# plot_regression_line(x_values, log_y, y_values_regr)
new_data = [x, log_y]
corrected_data = remove_offset(new_data, y_values_regr)

plot_new_fig(corrected_data)

cutout = get_cutout(corrected_data, 2195, 2185)
line1 = get_cutout(corrected_data, 2193.5, 2193.05)
line2 = get_cutout(corrected_data, 2190.15, 2189.7)
line3 = get_cutout(corrected_data, 2186.75, 2186.33)

plot_new_fig(line1)
plot_new_fig(line2)
plot_new_fig(line3)
plot_new_fig(cutout)

S1 = get_line_strength(line1)
S2 = get_line_strength(line2)
S3 = get_line_strength(line3)