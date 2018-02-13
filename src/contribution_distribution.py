import pandas as pd
import numpy as np
import os
import datetime

data_in = pd.read_table(os.curdir + './input/itcont_1.txt', sep='|', header = None)

#  get rid of unused columns
data_in = data_in[[0,7,10,13,14,15]]

data_in = data_in.rename(columns={0:'CMTE_ID', 7:'NAME',
                                      10: 'ZIP_CODE', 13: 'TRAN_DT',
                                      14: 'TRANS_AMT', 15: 'OTHER_ID'})

#making null/empty values zero
data = data_in.fillna(0)

#converting 0 into
data['CMTE_ID'] = data['CMTE_ID'].astype('str')
cmte_id_check = data['CMTE_ID'] != '0'

#
data['NAME'] = data['NAME'].astype('str')
name_check = data['NAME'] != ''

#change the column for ZIP_CODE into string to get length
data['ZIP_CODE'] = data['ZIP_CODE'].astype('str')
zip_check = data['ZIP_CODE'].str.len() >= 5

date_check = data['TRAN_DT'] != 0

transaction_check = data['TRANS_AMT'] != 0

other_id_check = data['OTHER_ID'] == 0

clean_data = data[other_id_check & cmte_id_check]


clean_data =





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
