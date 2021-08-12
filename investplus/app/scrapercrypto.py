#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Javier Escobar Cerezo
"""

from urllib.request import Request, urlopen

from urllib.error import HTTPError

from urllib.error import URLError

from bs4 import BeautifulSoup


site= "https://es.investing.com/crypto/"
hdr = {'User-Agent': 'Mozilla/5.0'}
req = Request(site,headers=hdr)

def request_data():
    try:

        html = urlopen(req)


    except HTTPError as e:

        print(e)

    except URLError:

        print("Server down or incorrect domain")

    else:

        res = BeautifulSoup(html.read(),"html5lib")

        matchs = res.findAll("tr")
        i=0
        total_data=[]
        for match in matchs:
            data=[]
            print("Match ",i)
            print(match.getText())
            td = match.findAll("td")
            for m in td:
                data.append(m.getText())
            if len(data) > 0:
                data.pop(0)
            print(data)
            print("-------------------------")
            i=i+1
            total_data.append(data)

        total_data.pop(0)
        print(total_data)
        return total_data

request_data()