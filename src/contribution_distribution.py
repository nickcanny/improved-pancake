import pandas as pd
import numpy as np
import os

data_in = pd.read_table(os.curdir + './input/itcont_1.txt', sep='|', header = None)

#  get rid of unused columns
data_in = data_in[[0,7,10,13,14,15]]

data_in = data_in.rename(columns={0:'CMTE_ID', 7:'NAME',
                                      10: 'ZIP_CODE', 13: 'TRANS_DT',
                                      14: 'TRANS_AMT', 15: 'OTHER_ID'})

#making null/empty values zero
data = data_in.fillna(0)

#converting 0 into string for checking validity, iff cmte_id is empty
data['CMTE_ID'] = data['CMTE_ID'].astype('str')
cmte_id_check = data['CMTE_ID'] != '0'

#convert 0 into string for checking validity of name, iff name is empty
data['NAME'] = data['NAME'].astype('str')
name_check = data['NAME'] != '0'

#change the column for ZIP_CODE into string to get length
data['ZIP_CODE'] = data['ZIP_CODE'].astype('str')
zip_check = data['ZIP_CODE'].str.len() >= 5

date_check = data['TRANS_DT'] != 0

transaction_check = data['TRANS_AMT'] != 0

other_id_check = data['OTHER_ID'] == 0

clean_data = data[cmte_id_check & name_check & zip_check & date_check & transaction_check & other_id_check]

#changing the date so only the year is printed, after the date is checked
clean_data['TRANS_DT'] = pd.to_datetime(clean_data['TRANS_DT'], format ='%m%d%Y')
clean_data['TRANS_DT'] = clean_data['TRANS_DT'].dt.year

#To get the most current transactions according to the data
most_recent_donations = clean_data['TRANS_DT'] == max(clean_data['TRANS_DT'])

current_donations = clean_data[most_recent_donations]

def multi_donation(df):
  
    # creating a list of donations to use while getting percentile
    a = []
    a.append(df['TRANS_AMT'])
    percent = pd.read_table(os.curdir + './input/percentile.txt', header = None)
    
    # tottal contributions in zip code
    df['ACCUM_TOTAL'] = sum(a)
    
    # number of transactions in each zip code
    df['INDI_TRANS'] = df['TRANS_AMT']
    
    # number of transactions in each zip code
    df['NUM_TRANS'] = len(df)
    
    # getting the percentile using nearest rank method
    n = np.around((percent/100)*len(a))-1
    df['PERCENTILE'] = int(a[n])
    
    # adding the columns and printing them out
    try:
        return df.loc[:, ['ACCUM_TOTAL', 'NUM_TRANS', 'PERCENTILE', 'INDI_TRANS']]
    except:
        pass

most_recent_donations.groupby('ZIP_CODE').apply(multi_donation).reset_index(drop = True).head()

end_data = data['CMTE_ID','ZIP_CODE','TRANS_DT','PERCENTILE','ACCUM_TOTAL','NUM_TRANS']

end_data.to_csv(r os.curdir +'./output/repeat_donors.txt', header=None, index=None, mode='a', sep='|')
