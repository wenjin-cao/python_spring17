
# coding: utf-8

# In[1]:

import pandas as pd
employee_compensation = pd.read_csv('Data/employee_compensation.csv')


# In[2]:

groups = list(set(employee_compensation['Organization Group']))
#Calculate the mean for each departement
groups_depts_means = []
for g in groups:
    depts = list(set(employee_compensation[employee_compensation['Organization Group']==g]['Department']))
    #For each department in the group:
    for d in depts:
        num_compen = employee_compensation[employee_compensation['Department']==d]['Total Compensation'].shape[0]
        sum_compen = employee_compensation[employee_compensation['Department']==d]['Total Compensation'].sum()
        mean_compen = sum_compen/num_compen
        group_dept_mean = [g,d,mean_compen]
        groups_depts_means.append(group_dept_mean)


# In[3]:

#Sort groups_depts_means by the third value 'mean'
sortedlist = sorted(groups_depts_means, key=lambda x: x[2],reverse=True)
df_mean = pd.DataFrame(sortedlist,columns=['Organization Group','Department','Total Compensation'])


# In[4]:

df_mean.to_csv('outputs/Q2_1.csv', index=False)


# In[5]:

df_mean.head()


# In[ ]:



