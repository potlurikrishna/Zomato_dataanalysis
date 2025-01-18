import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

df = pd.read_csv('Zomato-data-.csv')
print(df.head())

def convert_to(value):
    value = str(value).split('/')
    value = value[0]
    return value

df['rate'] = df['rate'].apply(convert_to)
print(df.head())
df.info()

sb.countplot(x=df['listed_in(type)'])
plt.xlabel('Type of Restaurent')
plt.show()

plt.clf()
grouped_data = df.groupby('listed_in(type)')['votes'].sum()
result = pd.DataFrame({'votes':grouped_data})
plt.plot(result,c='green',marker='o')
plt.xlabel('Type of Restaurent',c='red',size=20)
plt.ylabel('Votes',c='red',size=20)
plt.show()

max_votes = df['votes'].max()
print('max_votes',max_votes)
res_with_max_votes = df.loc[df['votes']==max_votes,'name']
print('Restaurant with maximum votes')
print(res_with_max_votes)

plt.clf()
sb.countplot(x=df['online_order'])
plt.show()

plt.clf()
plt.hist(df['rate'],bins=5)
plt.title('Rating Distributions')
plt.show()

plt.clf()
couple_data=df['approx_cost(for two people)']
sb.countplot(x=couple_data)
plt.show()

plt.clf()
plt.figure(figsize=(6,6))
sb.boxplot(x='online_order',y='rate',data=df)
plt.show()

plt.clf()
pivot_table = df.pivot_table(index='listed_in(type)', columns='online_order', aggfunc='size', fill_value=0)
sb.heatmap(pivot_table, annot=True, cmap='YlGnBu', fmt='d')
plt.title('Heatmap')
plt.xlabel('Online Order')
plt.ylabel('Listed In (Type)')
plt.show()