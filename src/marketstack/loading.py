import os
import requests
import csv

from utils import *
from utils.constants import params
from utils.constants import column_list

def run():

    api_result = requests.get('http://api.marketstack.com/v1/eod', params)
    api_json = api_result.json()


    #print(api_response['data']['symbol'])

    # for stock_data in api_response['data']:
    #     if stock_data in [stock_data['symbol'], stock_data['high'], stock_data['date']]:

    response = [
        stock_data  
        for stock_data in api_json['data']]
    #     print(u'Ticker %s has a day high of  %s on %s' % (
    #     stock_data['symbol'],
    #     stock_data['high'],
    #     stock_data['date']
    #     ))

    with open('response.csv', 'w', newline='') as file:
        response_writer = csv.DictWriter(file, fieldnames=column_list, delimiter=',')
        response_writer.writerows(response)