# improved-pancake
Insight Data Challenge

Challengers Name: Nick Cantafio

Language used: Python
Version: 3.6.4

### Libraries used:
-pandas
-numpy
-io

### Data used:
(2013-2014)
indiv14.zip from https://cg-519a459a-0ea3-42c2-b7bc-fa1143481f74.s3-us-gov-west-1.amazonaws.com/bulk-downloads/2014/indiv14.zip

### Self tests include 3 different tests
test 1 is for a small data set (32 entries)

#### Information:
I used a slicing technique for cleaning the data. I find it easy to read and understand when looking over the code and simple to implement. On my computer I used jupyter notebooks for writing the code and testing on my machine and atom to edit text files.

 #### Code:
Reads in the data into a pandas data frame. Then choses the relevant columns needed to fulfill the challenge requirements, once chosen renamed to help identify the columns that are being used. Then checking the columns for correct data and eliminating the rows that do not comply with the requirements set forth by the front end. Data is then grouped by zip code and plugged into the function to get total transactions for a certain zip code, amount accumulated by said zip code, and given donation closest to the nearest percentile using the nearest rank method. Lastly, printing out the columns that are needed to give to the front end developer with no names and separated by |.



###### Column names for the raw data:
1. CMTE_ID |
2. AMNDT_IND|
3.	RPT_TP|
4. TRANSACTION_PGI|
5. IMAGE_NUM|
6. TRANSACTION_TP|
7. ENTITY_TP|
8.	NAME|
9. CITY|
10.	STATE|
11.	ZIP_CODE|
12.	EMPLOYER|
13.	OCCUPATION|
14.	TRANSACTION_DT|
15. TRANSACTION_AMT|
16.	OTHER_ID|
17.	TRAN_ID|
18.	FILE_NUM|
19.	MEMO_CD|
20.	MEMO_TEXT|
21.	SUB_ID|
