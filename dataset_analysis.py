from read_csv import load_clean_data
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file = 'flats.csv'

df = load_clean_data(file)[3]

# print(df.dtypes)
# print(df.groupby(['location'])['price_per_sq'].mean().sort_values(ascending=False))
# print(df.groupby(['building_type'])['price_per_sq'].mean().sort_values(ascending=False))

sns.set(style='ticks')

# g = sns.FacetGrid(df, col='building_type', hue='seller')
# g.map(plt.scatter, 'price_per_sq', 'rooms')
# g.add_legend()

g = sns.FacetGrid(df)
# g.map(plt.hist, 'location')

sns.distplot(df['price_per_sq'], bins=20, kde=False, rug=True)

plt.show()