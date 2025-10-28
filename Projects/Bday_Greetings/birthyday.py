import pandas as pd
import datetime
import smtplib
import requests


def sendSMS(contact,message):
    url = "https://www.fast2sms.com/dev/bulk"

# read the excel 
df = pd.read_excel("C:\Ravi\Python\Projects\Bday_Greetings\employees.xlsx")

# today date & year
today = datetime.datetime.now().strftime("%d-%m")  
year = datetime.datetime.now().strftime("%Y")   

for index, item in df.iterrows():
    bday = item['DOB'].strftime("%d-%m")
    if today == bday and year not in (str(item["DOB"].strftime("%Y"))):
        name = item['Name']
        age = int(year) - int(item['DOB'].strftime("%Y"))
        msg = "Happy Birthday {name} , you are {age} years old"
        
        sendsms (item['CONTACT'],msg,name)     
