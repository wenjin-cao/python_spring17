
# coding: utf-8

# In[1]:

import pandas as pd
employee_compensation = pd.read_csv('Data/employee_compensation.csv')


# In[2]:

#Filter data by calendar year
df_calendar = employee_compensation[employee_compensation['Year Type']=='Calendar']
#Find the people whose overtime salary is greater than 5% of salaries;then find the ‘Job Family’ these people are associated with
df_greaterSalary = df_calendar[df_calendar['Overtime']>(df_calendar['Salaries']*5/100)]
jobFamilies = list(set(df_greaterSalary['Job Family']))


# In[3]:

#Define a function to calculate average total benefits and average total compensation
def findMean(item):
    sum_item = df_greaterSalary[df_greaterSalary['Job Family']==jf][item].sum()
    num_item = df_greaterSalary[df_greaterSalary['Job Family']==jf][item].shape[0]
    mean_item = 0
    if num_item != 0:
        mean_item = sum_item/num_item
    return mean_item


# In[4]:

families_percents_rows = []
#For each job family, calculate the averages and the percentage value
for jf in jobFamilies:
    df_jf = df_greaterSalary[df_greaterSalary['Job Family']==jf]
    mean_benefits = findMean('Total Benefits')
    mean_compensation = findMean('Total Compensation')
    percentage = 0
    if mean_benefits!=0:
        percentage = mean_compensation/mean_benefits
    family_percent = [jf, mean_benefits, mean_compensation, percentage]
    families_percents_rows.append(family_percent)


# In[5]:

#Sort the job families by the percentage value
sortedlist = sorted(families_percents_rows,key = lambda x : x[2],reverse = True)
df_families_percents = pd.DataFrame(sortedlist,columns=['Job Family','Total Benefits','Total Compensation','Percentage'])


# In[6]:

df_families_percents.head()


# In[7]:

df_families_percents.to_csv('outputs/Q2_2.csv',index=False)


# In[ ]:



