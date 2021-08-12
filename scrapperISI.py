#!/usr/bin/env python3
# -*- coding: iso-8859-1 -*-
"""
@author: Javier Escobar Cerezo
"""

from urllib.request import Request, urlopen

from urllib.error import HTTPError

from urllib.error import URLError

from bs4 import BeautifulSoup

site= "https://www.tikbooks.com/libros/don-quijote-de-la-mancha-i/986259/"
hdr = {'User-Agent': 'Mozilla/5.0'}
req = Request(site,headers=hdr)

try:

    html = urlopen(req)
    

except HTTPError as e:

    print(e)
    
except URLError:

    print("Server down or incorrect domain")

else:

    res = BeautifulSoup(html.read(),"html5lib")
    # print(res)
    
    titulo = res.find("div",{"class":"titBlock"}).find("h1").getText().strip()
    autor = res.find("p",{"class":"autor"}).find("a").getText()
    precio = res.find("div",{"class":"pvp"}).find("strong")
    precio.span.decompose()
    datos = res.find("div",{"class":"datos"})
    [x.extract() for x in datos.findAll('div',{"class":"materias"})]
    matchs = datos.findAll("li")
    print("Autor: ",autor)
    print("Obra: ",titulo)
    print("Precio: ",precio.getText())
    for match in matchs:
        # match.strong.decompose()
        print(match.getText().strip())
    descripcion = res.find("div",{"id":"displayA"})
    descripcion.h2.decompose() # Eliminamos la etiqueta h2 que no necesitamos
    descripcion = descripcion.getText().strip()
    print("Resumen: ",descripcion)
    
