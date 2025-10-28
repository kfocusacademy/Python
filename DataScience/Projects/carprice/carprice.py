import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# loading data to a data frame
df = pd.read_csv(r'C:\Ravi\Python_old\DataScience\Pandas\carprice\carprice.csv')
#print(df.head())

#print(df.isna().any())
#print(df.isnull().sum())

# to convert mpg to l/100km
def mpg_to_l100km(mpg):
    if pd.isna(mpg):
        return None
    else:
        return 235.214583 / mpg
    
# to update mpg to 
#print(df['city-mpg'])

df['city-mpg'] = df['city-mpg'].apply(mpg_to_l100km)
df.rename(columns={'city-mpg':'city-L/100KM'},inplace=True)
# update highway mog to L/100KMs
df['highway-mpg'] = df['highway-mpg'].apply(mpg_to_l100km)
df.rename(columns={'highway-mpg':'highway-L/100KM'},inplace=True)
print(df.dtypes)

# convert price column to integer
df['Price'] = df['Price'].str.replace('?','0')
df['Price']=df['Price'].astype(int)


# Normalizing 
def normalize_column(col):
    col_min = col.min()
    col_max = col.max()
    normalized_col = (col - col_min) / (col_max - col_min)
    return normalized_col

data = df.copy()
data['Price'] = normalize_column(data['Price'])

# binning group values
bins = np.linspace(min(data['Price']), max(data['Price']), 4)
group_names = ['Low', 'Medium', 'High']
data['Price-binned'] = pd.cut(data['Price'], bins, labels=group_names, include_lowest=True)
#print(data[['Price','Price-binned']].head(20))
plt.hist(data['Price-binned'])
plt.show()


# Data Visualization

# Generate a scattered graph between engine size and price
df['engine-size'] = pd.to_numeric(df['engine-size'], errors='coerce')
plt.xlabel("Engine Size")
plt.ylabel("Price")
plt.title("Price by Engine Size")
plt.scatter(df['engine-size'],df['Price'])
plt.grid()
plt.xlim(df['engine-size'].min(), df['engine-size'].max())
plt.show()

# Grouping data by drive wheel,body style and calculating mean price
test = df[['drive-wheels','body-style','Price']]
data_grouping = round(test.groupby(['drive-wheels','body-style'],as_index=False).mean(),2)
#print(data_grouping)

# Create a pivot table & heatmap

data_pivot = data_grouping.pivot(index='drive-wheels',columns='body-style')
print(data_pivot)
plt.pcolor(data_pivot, cmap ='RdBu')
plt.colorbar()
plt.show()
