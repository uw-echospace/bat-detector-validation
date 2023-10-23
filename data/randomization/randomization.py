import pandas as pd
from datetime import datetime
from datetime import timedelta
import random

df1 = pd.read_csv('ubna_data_01_collected_audio_records.csv')
df2 = pd.read_csv('ubna_data_02_collected_audio_records.csv')
df3 = pd.read_csv('ubna_data_03_collected_audio_records.csv')

df = pd.concat([df1, df2, df3], ignore_index=True)
# print(df['Datetime UTC'].dtype)
df['Datetime UTC'] = pd.to_datetime(df['Datetime UTC'])
# print(df['Datetime UTC'].dtype)

df2022 = df.loc[df['Datetime UTC'].dt.year == 2022]
print(df2022['Datetime UTC'].dt.month.unique())
#print(df2022['Site name'].unique())
df2022 = df2022[df2022['Site name'] != '(Site not found in Field Records)']

# Random select 2 rows for specific group
def select_random_rows(group):
    random.seed(48)
    if len(group) >= 2:
        return group.sample(2, random_state=1)
    else:
        return group
    
selected_rows = df2022.groupby([df2022['Datetime UTC'].dt.month, 'Site name'], 
                               group_keys=False).apply(select_random_rows).reset_index(drop=True)
print(selected_rows)

