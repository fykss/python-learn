# %%
# Work with Pandas

import numpy as np
import pandas as pd

data = {'Name': ['Tom', 'Nick', 'Bob', 'Jack'],
        'Age': [20, 21, 19, 18]}

# Create Dataframe from lists using dictionary
df = pd.DataFrame(data)
print(df.head())

beauty_data = pd.read_csv('data_structures/dataframe/data/beauty.csv', sep=';')

# Method type()
print(f'Method type(): {type(beauty_data)}\n')

# Method shape
print(f'Method shape: {beauty_data.shape}\n')

# Method show columns
print(f'Columns: {beauty_data.columns.values}')

# Method info()
print(f'Method info(): \n{beauty_data.info()}\n')

# Method describe()
print(f'Method describe(): \n{beauty_data.describe()}\n')

# Select column by name
print(f'Select column by name: \n{beauty_data["exper"].head()}\n')

# Count values
print(f'Count values: \n{beauty_data["female"].value_counts()}')

# Method loc
print(f'loc: \n{beauty_data.loc[0:5, ["wage", "female"]]}\n')

# Method iloc
print(f'iloc: \n{beauty_data.iloc[:, 2:4]}\n')

# Filtered only 'female'
print(beauty_data[beauty_data['female'] == 1])

# Compare wage between female and male
print(beauty_data[beauty_data['female'] == 1]['wage'].mean(), beauty_data[beauty_data['female'] == 0]['wage'].mean())

# %%
# Filtered all married male and found who wage more
print('Wage married male: ')
print(beauty_data[(beauty_data['female'] == 0) & (beauty_data['married'] == 1)]['wage'].median())

print('Wage not married male: ')
print(beauty_data[(beauty_data['female'] == 0) & (beauty_data['married'] == 0)]['wage'].median())

# Groupby column looks
for look, sub_df in beauty_data.groupby(['looks', 'female']):
    print(look)
    print(sub_df['wage'].median())

print(beauty_data.groupby(['looks'])[['wage', 'exper']].agg(np.median))

# Method Crosstab() - сводные таблицы
print(pd.crosstab(beauty_data['female'], beauty_data['looks']))

# %%
# Sort values by column and no ascending
beauty_data.sort_values(by='looks', ascending=False)
# Sort values by multiple columns
beauty_data.sort_values(by=['looks', 'educ'], ascending=[False, True])

# %%
# Creating new column
# Condition:
(beauty_data['wage'] > beauty_data['wage'].quantile(.75)).head()
# Convert boolean to int:
((beauty_data['wage'] > beauty_data['wage'].quantile(.75)).astype('int64')).head()
# Creating column by condition:
beauty_data['is_reach'] = (beauty_data['wage'] > beauty_data['wage'].quantile(.75)).astype('int64')
beauty_data.head()

# %%
# Apply and lambda function
beauty_data['female'].apply(lambda female: 'female' if female else 'male')

# %%
# Method Map()
dict = {1: 'union', 0: 'non-union'}
beauty_data['union'].map(dict).head()
