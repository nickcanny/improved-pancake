import pandas as import pd
import numpy as np
import os

data_import = pd.read_table(os.curdir + '\input\incont.txt')

data_columns = data_import[[0,7,10,13,14,15]]
#axis lables CMTE_ID, NAME, ZIP_CODE, TRANSACTION_DT, TRANSACTION_AMT, OTHER_ID

data_clean = {} # data that has correct input

def data_cleaning(stuff):
    row_num = 0
    for x in stuff:
        if stuff[0:4] = 'Nan': #check for empty inputs for first 5 rows
            data_correct_input.drop(data_correct_input.index[row_num])
        else:
            if len(stuff[2]) < 5:
                data_correct_input.drop(data_correct_input.index[row_num])
            else:
                if stuff[5] =/ 'NaN':
                    data_correct_input.drop(data_correct_input.index[row_num])
        data_correct_input.append(stuff)

clean_data = data_input_cleaning

data_ = {} #  cleaned and

def data_out(stuff_out):
    precentile_in = pd.read_table(os.curdir + '\input\percentile.txt')
    running_total_contributions = []
    number_of_contributions = []
    for x in stuff_out:
        running_percentile += 1
        
'''
final output into repeat_donors.txt column names seperated by '|'
1 CMTE_ID
2 ZIP_CODE
3 4 digit year of the contribution
4 running percentile (calling the precentile from percentile.txt and giving that amount) round up for .50 and down for .49
5 total contributions from ZIP_CODE ytd
6 total number of transations from ZIP_CODE ytd
'''
