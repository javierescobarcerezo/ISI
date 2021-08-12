#!/usr/bin/env python3
# -*- coding: iso-8859-1 -*-
"""
@author: Javier Escobar Cerezo
"""

from urllib.request import Request, urlopen

from urllib.error import HTTPError

from urllib.error import URLError

from bs4 import BeautifulSoup

site= "https://www.prestomusic.com/classical/products/8919578--sibelius-luonnotar-tapiola-spring-song"
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
    titulo = res.find("h1",{"class":"c-product-block__title"})
    titulo.span.decompose()
    # titulo.find('Offer').extract()
    titulo = titulo.getText().strip()
    titulo = titulo.replace('Offer,','').strip()
    print("Título: ",titulo)
    matchs = res.find("ul",{"class":"o-list o-columns--1-2-md"})
    matchs = matchs.findAll("li")
    for match in matchs:
        print(match.getText())
    
    sacd = res.find("div",{"class":"c-product-purchase__header"})
    precio_sacd = sacd.find("span",{"class":"u-reduced-new-price"}).getText().strip()
    print("Precio SACD: "+precio_sacd)
    
    precios = res.find("form",{"class":"c-product-purchase__download-options js-add-to-basket"})
    # precios = precios.findAll("div",{"class":"o-form__row"})
    precios.find("div",{"class":"o-form__row c-product-purchase__add-to-basket"}).decompose()
    precios = precios.findAll("div",{"class":"o-form__row"})
    print("Precios descarga: ")
    for p in precios:
        formato = p.find("span",{"class":"c-product-purchase__download-format"})
        # print(formato.getText())
        precio = p.find("span",{"class":"c-product-purchase__price"})
        print("\t-"+formato.getText()+" "+precio.getText())
    # print(precios)
    
    tracklist = res.find("div",{"class":"c-tracklist__initial-works"})
    # tracklist = tracklist.find("div",{"class":"c-tracklist__work js-work"})
    i=1
    print("---------------")
    for track in tracklist:
        print("Pista ",i)
        tr_tit = track.find("p",{"class":"c-track__title"}).getText().strip()
        print("Título: "+tr_tit)
        duracion = track.find("div",{"class":"c-track__duration"})
        duracion.span.decompose()
        print("Duración: "+duracion.getText().strip())
        precio = track.find("div",{"class":"c-track__price"}).getText().strip()
        print("Precio: "+precio)
        artistas = track.find("div",{"class":"c-track__details js-work-details"})
        print("Artistas: ")
        for artista in artistas.findAll("li"):
            print("\t-"+artista.getText().strip())
        
        i=i+1
        print("---------------")
    
    
    # titulo = res.find("div",{"class":"titBlock"}).find("h1").getText().strip()
    # autor = res.find("p",{"class":"autor"}).find("a").getText()
    # precio = res.find("div",{"class":"pvp"}).find("strong")
    # precio.span.decompose()
    # datos = res.find("div",{"class":"datos"})
    # [x.extract() for x in datos.findAll('div',{"class":"materias"})]
    # matchs = datos.findAll("li")
    # print("Autor: ",autor)
    # print("Obra: ",titulo)
    # print("Precio: ",precio.getText())
    # for match in matchs:
    #     # match.strong.decompose()
    #     print(match.getText().strip())
    # descripcion = res.find("div",{"id":"displayA"})
    # descripcion.h2.decompose() # Eliminamos la etiqueta h2 que no necesitamos
    # descripcion = descripcion.getText().strip()
    # print("Resumen: ",descripcion)
    
