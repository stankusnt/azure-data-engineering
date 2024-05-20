# Register this blueprint by adding the following line of code 
# to your entry point file.  
# app.register_functions(blueprint) 
# 
# Please refer to https://aka.ms/azure-functions-python-blueprints

import os
import sys
import requests
import csv

sys.path.append('/Users/stankusnt/azure-local')
from utils import *

import azure.functions as func
import logging

blueprint = func.Blueprint()


@blueprint.timer_trigger(schedule="0 * * * 1 *", arg_name="myTimer", run_on_startup=True,
              use_monitor=False) 
def timer_trigger(myTimer: func.TimerRequest) -> None:
    if myTimer.past_due:
        logging.info('The timer is past due!')

    run()
    logging.info('Python timer trigger function executed.')

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