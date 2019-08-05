###
# Copyright 2019 Corin Buchanan-Howland
# Python 2.7
#
# Data mapper that takes a line of inmate CSV data and converts it into a data dictionary based on the column order set in inmate_data_mapper_config_constants.
# This class only has static methods, so does not need to be instantiated.
###

from inmate_data_mapper_config_constants import *

class InmateDataMapper:

    ###
    # input: a line of CSV data in the order specified in inmate_data_mapper_config_constants
    # output: a dictionary representation of the input data
    ###
    @staticmethod
    def map (line):
        line = line.split(',')
        data_dictionary = {}

        # Use the config column map to put all columns of data in the right variables.
        index = 0
        for datum in line:
            data_dictionary[FILE_COLUMN_ORDER[index]] = datum.strip()
            index += 1

        return data_dictionary
