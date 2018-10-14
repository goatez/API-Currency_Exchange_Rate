import urllib.request, urllib.parse, urllib.error
import json
import pandas as pd
import os

#check directory
os.getcwd()

# change directory to data if necessary
# os.chdir('data')
# check directory again
# os.getcwd()

# create dictionary of currency names: currency codes
df = pd.read_csv("currency.csv") # read csv and save into pandas data frame
# convert data frame to dictionary and save
currency = df.set_index('currency_name').transpose().to_dict(orient='index')
currency = currency['currency_code']
currency

# Currency Exchange Rate
api = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE'  # api
api_key = '&apikey=6DWXECWW9U6OTFRK'  # api key

old = input('Enter from currency in correct form: ')  # enter currency you want converted
new = input('Enter to currency in correct form: ')  # enter currency you want to convert to

if currency.get(old) != None:
    code1 = currency[old]
    print("\n", "******* ", "The currency code for", old, "is", currency[old], " *******")
    from_currency = '&' + urllib.parse.urlencode({'from_currency': code1})

    if currency.get(new) != None:
        code2 = currency[new]
        print("******* ", "The currency code for", new, "is", currency[new], " *******")
        to_currency = '&' + urllib.parse.urlencode({'to_currency': code2})

        url = api + from_currency + to_currency + api_key
        address = urllib.request.urlopen(url)

        data = address.read().decode()
        rate = json.loads(data)

        from_cur = rate["Realtime Currency Exchange Rate"]["2. From_Currency Name"]
        to_cur = rate["Realtime Currency Exchange Rate"]["4. To_Currency Name"]

        exchange_rate = rate["Realtime Currency Exchange Rate"]["5. Exchange Rate"]
        last_refreshed = rate["Realtime Currency Exchange Rate"]["6. Last Refreshed"] \
                         + " " + rate["Realtime Currency Exchange Rate"]["7. Time Zone"]

        print(json.dumps(rate, indent=4))
        print("$$$$$$ ", 'Current exchange rate from', from_cur, "to",
              to_cur, "is",exchange_rate, "as of", last_refreshed, " $$$$$$")

else:
    print("Incorrect currency, please check spelling and try again")
