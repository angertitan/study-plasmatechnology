import numpy as np
from os import listdir
from os.path import join, basename, dirname, splitext
import json


def open_file(filepath):
    ''' open file and return lines'''
    # open file
    file = open(filepath)

    # read data
    file_data = file.read()

    # get each line
    lines = file_data.split('\n')

    return lines


def save_file(filepath, data):
    '''saves data in json file'''
    
    # convert array to json
    data_json = json.dumps(data)

    filepath_wo_ext = splitext(filepath)[0]
    # save data in new format
    parsed_filepath = join(dirname(filepath_wo_ext), '../parsed',
                           basename(filepath_wo_ext) + '.json')
    parsed_file = open(parsed_filepath, "w+")
    parsed_file.write(data_json)

# parse file data into a more readable format
def parse_lab1(filepath):
    ''' parse file and save as json'''
    # get each line from file
    lines = open_file(filepath)

    lines.pop()

    data_array = []
    # iterate over lines
    for line in lines:
        # get wavenumber and value from line
        line_data = line.split('\t')

        # save wavenumber and value seperatly
        wave_number = line_data[0]
        value = line_data[1]

        # convert date into a dict and make a json object
        data_dict = {"wavenumber": float(wave_number), "value": float(value)}

        # add data to array
        data_array.append(data_dict)

    save_file(filepath, data_array)

def parse_lab2(filepath):
    ''' parse file and save as json'''
    # get each line from file
    lines = open_file(filepath)

    # remove unneeded meta-data in textfile 
    lines_wo_meta = lines[:len(lines)-26]

    data_array = []
    for line in lines_wo_meta:

        # only second value is needed
        line_data = line.split('\t')

        data_array.append(int(line_data[1]))

    save_file(filepath, data_array)

# parse many files
def parse_many(dirpath, lab = 1):
    ''' parse many files and save them as json'''
    files = listdir(dirpath)
    print(files)
    # iterate over files, parse and save them as json
    for file in files:
        print('parse file {}'.format(file))
        filepath = join(dirpath, file)
        if (lab == 1):
            parse_lab1(filepath)
            
        
        parse_lab2(filepath)
        


parse_many('data/lab2/original', 2)