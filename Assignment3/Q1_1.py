
# coding: utf-8

# In[1]:

import pandas as pd
vehicle_collisions = pd.read_csv('Data/vehicle_collisions.csv')


# In[2]:

#Add column 'YEAR' and 'MONTH'
vehicle_collisions['YEAR'] = vehicle_collisions['DATE'].str[-2:]
vehicle_collisions['MONTH'] = vehicle_collisions['DATE'].apply(lambda x : x.split('/')[0])


# In[3]:

#Count collisions in manhanttan in a month
def count_collisions_manh_2016(month):
    collisions = 0
    collisions += vehicle_collisions[(vehicle_collisions['BOROUGH']=='MANHATTAN')&(vehicle_collisions['MONTH']==str(month))&(vehicle_collisions['YEAR']=='16')].shape[0]
    return collisions


# In[4]:

#Count collisions in new york in a month
def count_collisions_all_2016(month):
    collisions = 0
    collisions += vehicle_collisions[(vehicle_collisions['MONTH']==str(month))&(vehicle_collisions['YEAR']=='16')].shape[0]
    return collisions


# In[5]:

#Get collisions in manhanttan for each month
collisions_manh_monthly = []
for i in range(1,13):
    collisions_manh_monthly.append(count_collisions_manh_2016(i))


# In[6]:

#Get collisions in new york for each month
collisins_all_monthly = []
for i in range(1,13):
    collisins_all_monthly.append(count_collisions_all_2016(i))


# In[7]:

df_percent = pd.DataFrame()
df_percent['MONTH']=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
df_percent['MANHATTAN']=collisions_manh_monthly
df_percent['NYC']=collisins_all_monthly
df_percent['PERCENTAGE']=df_percent['MANHATTAN']/df_percent['NYC']


# In[8]:

df_percent.head()


# In[9]:

df_percent.to_csv('outputs/Q1_1.csv',index=False)


# In[ ]:



