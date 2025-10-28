import pandas as pd 

df = pd.read_excel(r'C:\Ravi\Python\Projects\Auto_Email_Sending\customer_details.xlsx')
for index, row in df.iterrows():
    print(row)
    