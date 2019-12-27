# %%
import pandas as pd

data = {'Name': ['Tom', 'Nick', 'Bob', 'Jack'],
        'Age': [20, 21, 19, 18]}

# Create Dataframe from lists using dictionary
df = pd.DataFrame(data)
print(df.head())

beauty_data = pd.read_csv('data_structures/dataframe/data/beauty.csv', sep=';')

# Method type()
print(f'Method type(): {type(beauty_data)}\n')

# Method head()
print(f'Method head(): \n{beauty_data.head()}\n')

# Method shape
print(f'Method shape: {beauty_data.shape}\n')

# Method info()
print(f'Method info(): \n{beauty_data.info()}\n')

# Method describe()
print(f'Method describe(): \n{beauty_data.describe()}\n')

# Select column by name
print(f'Select column by name: \n{beauty_data["exper"].head()}\n')

# Method loc
print(f'loc: \n{beauty_data.loc[0:5, ["wage", "female"]]}\n')

# Method iloc
print(f'iloc: \n{beauty_data.iloc[:, 2:4]}\n')

# Filtered only 'female'
print(beauty_data[beauty_data['female'] == 1])

# Compare wage between female and male
print(beauty_data[beauty_data['female'] == 1]['wage'].mean(), beauty_data[beauty_data['female'] == 0]['wage'].mean())

# Filtered all married male and found who wage more
print('Wage married male: ')
print(beauty_data[(beauty_data['female'] == 0) & (beauty_data['married'] == 1)]['wage'].median())

print('Wage not married male: ')
print(beauty_data[(beauty_data['female'] == 0) & (beauty_data['married'] == 0)]['wage'].median())
