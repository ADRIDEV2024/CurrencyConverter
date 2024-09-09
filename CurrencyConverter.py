import requests as req
from config import apikey


def convert_currency():
    initial_currency = input("Enter your initial currency:\n")
    target_currency = input("Enter your target currency:\n ")
    
    while True:
        
        try:
            amount = float(input("Enter the amount: \n"))
            
        except TypeError as error:
            print("Sorry, the amount needs to be numeric\n", error)
        
        if not amount > 0:
            print("Sorry, the amount needs to be greater than 0")
            continue
        else:
            break
    
    url = "https://api.apilayer.com/fixer/convert?from={from}&from={from}&amount={amount}"
    payload = {}
    header = {"apikey: config.apikey"} 
    response = req.request("GET", url, header=header, data=payload)
    status_code = response.status_code
    
    if status_code != 200:
        response = response.json()
        print("Error response" + str(response))
        quit()
    
    response = response.json()
    print("Convertion result: " + str(response)

if __name__ == "__main__":
    convert_currency()
