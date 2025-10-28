import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objs as go
import plotly.io as pio
import plotly.express as px
import plotly.offline as py

# import dataset1 
dataset1 = pd.read_csv(r'C:\Ravi\Python_old\DataScience\Pandas\Covid\covid.csv')
print(dataset1.head())
print(dataset1.info())

# import dataset2 
dataset2 = pd.read_csv(r'C:\Ravi\Python_old\DataScience\Pandas\Covid\covid_grouped.csv')
print(dataset2.head())
print(dataset2.info())


# Data Cleaning - Observation1 
# In Dataset1 - we have columns Newcases/newdeaths/newrecovered with null values
dataset1.drop(['NewCases','NewDeaths','NewRecovered'],axis=1,inplace=True)
print(dataset1.info())

# Creating table using 
from plotly.figure_factory import create_table
table = create_table(dataset1.head(15))
#py.iplot(table)

# buiding bar graph to compare covid infected countries total case/death/recovered 
px.bar(dataset1.head(15),x='Country/Region',y='TotalCases', color = 'TotalCases',hover_data=['Country/Region','Continent'])
