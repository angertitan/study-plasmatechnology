import numpy as np
from os import listdir
from os.path import join, basename, dirname, splitext
import json


# parse file data into a more readable format
def parse(filepath: str):
    ''' parse file and save as json'''
    # open file
    file = open(filepath)

    # read data
    file_data = file.read()

    # get each line
    lines = file_data.split('\n')

    # remove last element from list
    lines.pop()

    data_array = []
    # iterate over lines
    for index, line in enumerate(lines):
        # get wavenumber and value from line
        line_data = line.split('\t')

        # save wavenumber and value seperatly
        wave_number = line_data[0]
        value = line_data[1]

        # convert date into a dict and make a json object
        data_dict = {"wavenumber": wave_number, "value": value}

        # add data to array
        data_array.append(data_dict)

    # convert array to json
    data_json = json.dumps(data_array)

    filepath_wo_ext = splitext(filepath)[0]
    # save data in new format
    parsed_filepath = join(dirname(filepath_wo_ext), '../parsed',
                           basename(filepath_wo_ext) + '.json')
    parsed_file = open(parsed_filepath, "w+")
    parsed_file.write(data_json)


# parse many files
def parse_many(dirpath: str):
    ''' parse many files and save them as json'''
    files = listdir(dirpath)

    # iterate over files, parse and save them as json
    for file in files:
        print('parse file {}'.format(file))
        filepath = join(dirpath, file)
        parse(filepath)


parse_many('data/original')
