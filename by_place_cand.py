# Anna Lin
# G20
# Part C

import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

contrib = pd.read_pickle('contrib_clean.pkl')
com_cand = pd.read_csv('com_cand_info.csv')

# Q3
merged = contrib.merge(com_cand, on='CMTE_ID', validate='m:1', indicator=True)

# Q4
print('Contrib and Com_cand has merged:')
print(merged)
merged = merged.drop(columns = "_merge")

# Q5
# Aggregating datasets
group_by_place_cand = merged.groupby(['STATE', 'zip', 'CAND_NAME']) 

# Q6
by_place_cand = group_by_place_cand['amt'].sum()

# Q7
by_place_cand.to_csv('by_place_cand.csv')

# Q8
# There might be some error here 
# Analyze which places provide largest contribution to each candidate
mil = by_place_cand.groupby(["STATE","CAND_NAME"]).sum()
mil = mil/1e6

# Q9
# Computing overall totals by candidate 
by_cand = mil.groupby("CAND_NAME").sum()

# Q10
# select top 10 candidates 
top_cand = by_cand.sort_values()[-10:]
print('These are the top 10 candidates:','\n')
print(top_cand)

# Q11
by_state = mil.groupby("STATE").sum()
top_state = by_state.sort_values()[-10:]
print('These are the top 10 states:', '\n')
print(top_state)

# Q12
fig, (ax1,ax2) = plt.subplots(1,2,dpi=300)

# Q13
fig.suptitle("Top Candidates and States, Millions of Dollars")

# Q14
top_cand.plot.barh(ax=ax1, fontsize=7)

# Q15
# turn y-axis off
ax1.set_ylabel("")

# Q16
top_state.plot.bar(ax=ax2, fontsize=7)

# Q17
ax2.set_xlabel('State')

# Q18
fig.tight_layout()
fig.savefig('top.png')

# Q19
# build a heatmap
reset = mil.reset_index()

# Q20
keep_cand = reset["CAND_NAME"].isin(top_cand.index)

# Q21
keep_state = reset["STATE"].isin(top_state.index)

# Q22
keep = keep_cand & keep_state

# Q23
# I don't think I did this part right 
sub = reset[keep]

# Q24
# sum things up over zip codes 

grouped = sub.groupby(['STATE', 'CAND_NAME'])

# Q25
summed = grouped['amt'].sum()

# Q26
# unstacking data to make columns by state
# grid should have one row per tope-ten candidate
grid = summed.unstack('STATE')

# Q27
fig2, ax3 = plt.subplots(dpi=300)

# Q28
fig2.suptitle("Contributions in Millions")

# Q29
# 'annot' and 'fmt' cause the cells in the heatmap to be labeled iwth values rounded to the integer
sns.heatmap(grid, annot=True, fmt=".0f", ax=ax3)

# Q30
ax3.set_xlabel('State')
ax3.set_ylabel('Candidate')

# Q31
fig2.tight_layout
fig2.savefig('heatmap.png')






