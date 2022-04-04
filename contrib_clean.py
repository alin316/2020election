# Anna Lin
# G20
# Part 1
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

contrib = pd.read_csv('contrib_by_zip.zip', dtype=str)

# Q2
# making it numeric
contrib['amt'] = contrib['amt'].astype(float)

# Q3
po = pd.read_csv('pocodes.csv')

# Q4
# dropping 'Name' column
po = po.drop(columns='Name')

# Q5
# filter out state codes that aren't in the 50 states
contrib = contrib.merge(po, left_on='STATE', right_on='PO', how='outer', validate='m:1', indicator=True)

# Q6
print(contrib['_merge'].value_counts())

# Q7
# remove the records that didn't match the 
# geographic entities in po
state_bad = contrib['_merge'] != 'both'

# Q8
contrib = contrib.drop(columns = '_merge')
contrib = contrib.drop(columns = 'PO')

# Q9
# tabulate the data that's going to be dropped
# when we exclude records with bad state codes
bad_recs = contrib[state_bad].groupby('STATE')

# Q10
# summing contributions
state_bad_amt = bad_recs['amt'].sum()

# Q11
print('state codes:')
print(state_bad_amt, '\n')
print('Total contributions:', '\n')
print(state_bad_amt.sum())

# Q12
contrib = contrib[state_bad == False]

# Q13
# look for bad zipcodes that are not purely numeric
num_zip = pd.to_numeric(contrib['zip'], errors='coerce')

# Q14
zip_bad = num_zip.isna()

# Q15
bad_recs = contrib[zip_bad].groupby('zip')
zip_bad_amt = bad_recs['amt'].sum()
print('\n')
print(zip_bad_amt)
print(zip_bad_amt.sum())

# Q16
# Compute total contributions by committee
# is it loc or iloc
contrib = contrib[zip_bad == False]

# Q17
# writing files on pickle
# do i need quotations? 
contrib.to_pickle('contrib_clean.pkl')

# Q18
by_com = contrib.groupby('CMTE_ID')
com_total = by_com['amt'].sum()

# Q19
com_total.name = 'total_amt'

# Q20 
com_total.to_csv('com_total.csv')





