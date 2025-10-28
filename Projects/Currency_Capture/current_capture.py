import requests
import datetime 

# Function to compute and display currency details
def get_usdtoinr():
    try:
        url = "https://open.er-api.com/v6/latest/USD"
        response = requests.get(url).json()
        print(response)
        usd_to_inr = response['rates']['INR']
        print("success")
        return usd_to_inr
    except Exception as e:
        print(e)
        return None

# Driver Code        
if __name__ == "__main__":        
    usdtoinr= get_usdtoinr()
    current_Date_time    = datetime.datetime.now()
    formatted_time = current_Date_time.strftime("%d-%m-%Y %H:%M:%S")
    
    # Insert this data to a csv file
    with open("currency_data.csv", "a") as file:
        file.write(f"{formatted_time},{usdtoinr}\n") 
        
    print(f"Current USD to INR rate as on {formatted_time} is: {usdtoinr}")

    
