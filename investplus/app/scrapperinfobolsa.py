#!/usr/bin/env python3
# -*- coding: iso-8859-1 -*-
"""
@author: Javier Escobar Cerezo
"""

from urllib.request import Request, urlopen

from urllib.error import HTTPError

from urllib.error import URLError

from bs4 import BeautifulSoup

site= "https://www.infobolsa.es/divisas"
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

        matchs = res.findAll("div", {"class": "currencyCont01"})
        i=0
        total_data=[]
        for match in matchs:
            data=[]
            print("Match ",i)
            # print(match.getText())
            moneda = match.find("li", {"class": "titCurren01"}).getText().strip()
            # print(moneda)
            data.append(moneda)
            valores = match.find("div", {"class": "currenLeftBox03 right"})
            valores = valores.findAll("li")
            for m in valores:
                # print(m.getText().strip())
                data.append(m.getText().strip())
            print(data)
            print("-------------------------")
            i=i+1
            total_data.append(data)

        print(total_data)
        return total_data
