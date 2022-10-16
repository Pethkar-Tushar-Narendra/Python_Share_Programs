import requests
import time
import pandas as pd
from datetime import datetime
import gspread

scopes = ["https://www.googleapis.com/auth/spreadsheets",
          'https://www.googleapis.com/auth/drive']

gc = gspread.service_account(filename='client_secret.json')

sh = gc.open('sharesoft')
# sh = gc.open_by_key("1-1pJ1EjTkES3_Rg4LnynJYiV73cwEV93")

def datetotimestamp(date):
    time_tuple = date.timetuple()
    timestamp = round(time.mktime(time_tuple))
    return timestamp

def timestamptodate(timestamp):
    return datetime.fromtimestamp(timestamp)

worksheet_1_min = sh.worksheet('OPTIONDATA')
# intradata
while 1:
    banknifty = "BANKNIFTY"

    url = "https://www.nseindia.com/api/option-chain-indices?symbol=" + \
    str(banknifty)
    headers = {
        "accept-encoding": "gzip, deflate, br",
           "accept-language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
           "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
           }

    ocdata = []

    data = requests.get(url, headers=headers).json()["records"]["data"]

    for i in data:
        for j, k in i.items():
            if j == "CE" or j == "PE":
                info = k
                info["instrument type"] = j
                ocdata.append(info)

    data_1_min = pd.DataFrame(ocdata)
    worksheet_1_min.update(data_1_min.values.tolist())
    print(3)
    time.sleep(200)
    