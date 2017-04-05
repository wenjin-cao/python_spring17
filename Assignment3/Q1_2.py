
# coding: utf-8

# In[1]:

import pandas as pd
vehicle_collisions = pd.read_csv('Data/vehicle_collisions.csv')


# In[2]:

#For values in each row, if they are in columns 'VEHICLE 1 TYPE','VEHICLE 2 TYPE','VEHICLE 3 TYPE','VEHICLE 4 TYPE','VEHICLE 5 TYPE', 
#count the number of non-null valus, as thus we get the collision scale. 
collisions = vehicle_collisions[['VEHICLE 1 TYPE','VEHICLE 2 TYPE','VEHICLE 3 TYPE','VEHICLE 4 TYPE','VEHICLE 5 TYPE']]
vehicle_collisions['SCALE'] = collisions.apply(lambda x : x.count(),axis=1)


# In[3]:

print('How many collision scales:')
set(vehicle_collisions['SCALE'])


# In[4]:

#Given a collision scale, count the number of collisions of each borough respectively and return a list
def count_scale(number):
    count = []
    for borough in ['STATEN ISLAND', 'MANHATTAN', 'BROOKLYN', 'QUEENS', 'BRONX']:
        c = vehicle_collisions[(vehicle_collisions['SCALE']==number)&(vehicle_collisions['BOROUGH']==borough)].shape[0]
        count.append(c)
    return count


# In[5]:

#Output the count of collisions of each scale
df_scale = pd.DataFrame()
df_scale['BOROUGH'] = ['STATEN ISLAND', 'MANHATTAN', 'BROOKLYN', 'QUEENS', 'BRONX']
df_scale['ONE_VEHICLE_INVOLVED'] = count_scale(1)
df_scale['TWO_VEHICLES_INVOLVED'] = count_scale(2)
df_scale['THREE_VEHICLES_INVOLVED'] = count_scale(3)
#df_scale['MORE_VEHICLE_INVOLVED'] = [x+y for x, y in zip(count_scale(4),count_scale(5))]
df_scale['MORE_VEHICLE_INVOLVED'] = [sum(x) for x in zip(*[count_scale(4),count_scale(5),count_scale(0)])]


# In[6]:

df_scale.to_csv('outputs/Q1_2.csv',index=False)


# In[7]:

df_scale.head()


# In[ ]:



