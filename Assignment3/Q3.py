
# coding: utf-8

# In[1]:

import pandas as pd
matches = pd.read_csv('Data/cricket_matches.csv')


# In[2]:

#Find teams which host the game and win the game
winnerTeams = list(set(matches[matches['home']==matches['winner']]['home']))
df_winnerTeams = matches[matches['home']==matches['winner']]


# In[3]:

teams_scores = []
for team in winnerTeams:
    #The score can be innings_1 runs or innings_2 runs
    df_winner_innings1 = df_winnerTeams[(df_winnerTeams['innings1']==df_winnerTeams['winner'])&(df_winnerTeams['winner']==team)]
    df_winner_innings2 = df_winnerTeams[(df_winnerTeams['innings2']==df_winnerTeams['winner'])&(df_winnerTeams['winner']==team)]
    sumscore = df_winner_innings1['innings1_runs'].sum()+df_winner_innings2['innings2_runs'].sum()
    numscore = df_winner_innings1['innings1_runs'].shape[0]+df_winner_innings2['innings2_runs'].shape[0]
    avgscore = sumscore/numscore
    team_score = [team, avgscore]
    teams_scores.append(team_score)


# In[4]:

df_scores = pd.DataFrame(teams_scores,columns=['Home','Score'])
df_scores.to_csv('outputs/Q3.csv',index=False)
df_scores.head()


# In[ ]:



