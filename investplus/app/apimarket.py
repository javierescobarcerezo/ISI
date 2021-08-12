#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Javier Escobar Cerezo
"""

import requests
import json

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

params = {
  'access_key': '*',
  'limit': 1,
  'offset': 0
}


def get_data(api_result):
    api_response = api_result.json()
    d_open = api_response["data"]["eod"][0]["open"]
    d_close = api_response["data"]["eod"][0]["close"]
    d_high = api_response["data"]["eod"][0]["high"]
    d_low = api_response["data"]["eod"][0]["low"]
    d_symbol = api_response["data"]["eod"][0]["symbol"]
    name = api_response["data"]["name"]
    # print(data)
    return [name,d_symbol,d_open,d_close,d_high,d_low]

def request_data():
    
    total_data=[]
    api_result = requests.get('http://api.marketstack.com/v1/tickers/MSFT/eod', params)
    total_data.append(get_data(api_result))
    api_result = requests.get('http://api.marketstack.com/v1/tickers/AAPL/eod', params)
    total_data.append(get_data(api_result))
    api_result = requests.get('http://api.marketstack.com/v1/tickers/SAN/eod', params)
    total_data.append(get_data(api_result))
    api_result = requests.get('http://api.marketstack.com/v1/tickers/ATVI/eod', params)
    total_data.append(get_data(api_result))
    api_result = requests.get('http://api.marketstack.com/v1/tickers/EA/eod', params)
    total_data.append(get_data(api_result))
    print(total_data)
    return total_data
  
# request_data()