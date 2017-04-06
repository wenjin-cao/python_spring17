
# coding: utf-8

# In[1]:

import pandas as pd
movies_awards = pd.read_csv('Data/movies_awards.csv')
awards = movies_awards['Awards'].dropna()


# ### Define functions for extracting data

# In[2]:

import re
re.split
#Calculate total number of wins
def count_won(x):
    #splits = x.lower().split()
    splits = re.findall(r"[\w']+|[.&;]",x.lower())
    count = 0
    if 'win' in splits:
        i_win = splits.index('win')
        count += int(splits[i_win-1])
    if 'wins' in splits:
        i_wins = splits.index('wins')
        count += int(splits[i_wins-1])
    if 'won' in splits:
        i_won = splits.index('won')
        count += int(splits[i_won+1])
    return count


# In[3]:

#Calculate total number of nominations
def count_nominated(x):
    splits = re.findall(r"[\w']+|[.&;]",x.lower())
    count = 0
    if 'nomination' in splits:
        i_nomination = splits.index('nomination')
        count += int(splits[i_nomination-1])
    if 'nominations' in splits:
        i_nominations = splits.index('nominations')
        count += int(splits[i_nominations-1])
    if 'nominated' in splits:
        i_nominated = splits.index('nominated')
        count += int(splits[i_nominated+2])
    return count


# In[4]:

#Calculate nominations of a certain award
def count_awards_nominated(x,award):
    splits = re.findall(r"[\w']+|[.&;]",x.lower())
    count = 0
    if award in splits:
        i_award = splits.index(award)
        if splits[i_award-3] == 'nominated':
            count = splits[i_award-1]
    return count


# In[5]:

#Calculate wins of a certain award
def count_awards_won(x,award):
    splits = re.findall(r"[\w']+|[.&;]",x.lower())
    count = 0
    if award in splits:
        i_award = splits.index(award)
        if splits[i_award-2] == 'won':
            count = splits[i_award-1]
    return count


# ### Create dataframe saving splited data

# In[6]:

df_awards = pd.DataFrame()
df_awards['Awards'] = awards


# In[7]:

#df_awards['Awards_Won'] = awards.str.split()
df_awards['Awards_Won'] = awards.apply(lambda x:count_won(x))
df_awards['Awards_Nominated'] = awards.apply(lambda x:count_nominated(x))

df_awards['Prime_Awards_Nominated'] = awards.apply(lambda x:count_awards_nominated(x,'primetime'))
df_awards['Oscar_Awards_Nominated'] = awards.apply(lambda x:count_awards_nominated(x,'oscar'))
df_awards['Golden_Globe_Awards_Nominated'] = awards.apply(lambda x:count_awards_nominated(x,'golden'))
df_awards['BAFTA_Awards_Nominated'] = awards.apply(lambda x:count_awards_nominated(x,'bafta'))

df_awards['Prime_Awards_Won'] = awards.apply(lambda x:count_awards_won(x,'primetime'))
df_awards['Oscar_Awards_Won'] = awards.apply(lambda x:count_awards_won(x,'oscar'))
df_awards['Golden_Globe_Awards_Won'] = awards.apply(lambda x:count_awards_won(x,'golden'))
df_awards['BAFTA_Awards_Won'] = awards.apply(lambda x:count_awards_won(x,'bafta'))


# In[8]:

df_awards.head(10)


# In[9]:

df_awards.to_csv('outputs/Q4.csv',index=False)


# In[ ]:



