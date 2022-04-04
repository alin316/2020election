# Anna Lin
# G20
# Part B

import pandas as pd 

# Q2
contrib = pd.read_pickle('contrib_clean.pkl')

# Q3
com_total = pd.read_csv('com_total.csv')

# Q4
com_info = pd.read_csv('fec_committees.csv', dtype=str)

# Q5
# trimming com_info
com_info = com_info[['CMTE_ID', 'CMTE_NM', 'CMTE_PTY_AFFILIATION', 'CAND_ID']]

# Q6
# join contributions into com_info
com_merged = com_info.merge(com_total, how='right', validate='m:1',  indicator=True)

# Q7
print('This is the merge indicator:', '\n')
print(com_merged)
com_merged = com_merged.drop(columns = "_merge")

# Q8
# is the committee funding mutliple candidates?
# '.size()' counts # entries in each 
# the results will be a series of number of times each commmittee appears
numcan = com_info.groupby('CMTE_ID').size()

# Q9
print('\n')
print(' How many committee members that fund more than one candidate:', "/n")
print(numcan[numcan > 1])

# Q10
# reading information about candidates
pres = pd.read_csv('fec_candidates.csv', dtype=str)

# Q11
# filter out people who wasn't running for Pres in 2020
is_pres = pres['CAND_OFFICE'] == 'P'

# Q12
is_2020 = pres['CAND_ELECTION_YR'] == '2020'

# Q13
# looks weird
keep = is_pres & is_2020

# Q14
# eliminate all other candidates and election year
pres = pres[keep]

# Q15
# dropping columns 
pres = pres.drop(columns='CAND_OFFICE')
pres = pres.drop(columns='CAND_ELECTION_YR')

# Q16
# join candidate date onto committee information
com_cand = com_merged.merge(pres, how='left', validate='m:1', indicator=True)
                 
# Q17
# Merge Correction Check
# should have candidate date and committee information
print(com_cand)           

# Q18
com_cand = com_cand[com_cand['_merge'] == 'both']
com_cand = com_cand.drop(columns='_merge')

# Q19
com_cand.to_csv('com_cand_info.csv', index=False)
