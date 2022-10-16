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

worksheet_1_min = sh.worksheet('1_min')

while 1:
    end = datetotimestamp(datetime.today())
    if worksheet_1_min.acell('Q2').value == 'SHARE':
        year= worksheet_1_min.acell('M2').value
        month= worksheet_1_min.acell('N2').value
        day= worksheet_1_min.acell('O2').value
        company= worksheet_1_min.acell('L2').value
        time1= worksheet_1_min.acell('P2').value
        start_1_min = datetotimestamp(datetime(int(year), int(month), int(day)))
        url_1_min = 'https://priceapi.moneycontrol.com/techCharts/indianMarket/stock/history?symbol='+(company.upper())+'&resolution='+time1+'&from=' + \
            str(start_1_min)+'&to='+str(end)

        resp_1_min = requests.get(url_1_min).json()
        data_1_min = pd.DataFrame(resp_1_min)

        worksheet_1_min.update([data_1_min.columns.values.tolist()]+data_1_min.values.tolist())
    else:
        year= worksheet_1_min.acell('M2').value
        month= worksheet_1_min.acell('N2').value
        day= worksheet_1_min.acell('O2').value
        time1= worksheet_1_min.acell('P2').value
        number= worksheet_1_min.acell('R2').value
        start_1_min = datetotimestamp(datetime(int(year), int(month), int(day)))
        url_1_min = 'https://priceapi.moneycontrol.com/techCharts/history?symbol='+number+'&resolution='+time1+'&from=' + \
            str(start_1_min)+'&to='+str(end)

        resp_1_min = requests.get(url_1_min).json()
        data_1_min = pd.DataFrame(resp_1_min)

        worksheet_1_min.update([data_1_min.columns.values.tolist()]+data_1_min.values.tolist())
    time.sleep(20)
    