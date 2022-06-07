#!/usr/bin/env python3
from operator import contains
from warnings import catch_warnings
from bs4 import BeautifulSoup
import requests
import csv
import re
from links import links

links()

def scrap():

      articulos = []
      precios = []

      with open('links.csv', 'r') as f:
            reader = csv.reader(f)
            for u in reader:
                  p = re.search("(?P<url>https?://[^\s]+)", str(u)).group("url")
                  url = p
                  page = requests.get(url)
                  soup = BeautifulSoup(page.content, 'html.parser')            

                  precio = soup.find_all('span', class_='andes-visually-hidden')
                  articulo = soup.find_all('h1', class_='ui-pdp-title')

                  
                  for w in (articulo):
                        t = re.sub(r'[^\w\s]','',w.text)
                        articulos.append(t)
                        

                  favorito = 0
                  precio_anterior = 0
                 
                  count = 0
                  for y in (precio):
                        x = re.sub(r'[^\w\s]','',y.text)
                        print(x)
                        fil = re.findall("\APrecio anterior", x)
                        num = re.findall("\d", x)
                        if x != "":
                             
                              if len(fil) != 0:
                                    precio_anterior += 1
                                    print("Match findall")
                                          
                              elif x == "Favorito":
                                    favorito += 1 
                                    count += 1  
                              elif favorito == 1 and precio_anterior >= 0:
                                    count += 1
                                    if count == 2:
                                          f=str(num)
                                          h=f.replace(",","") 
                                          z=h.replace(" ","")
                                          o=h.replace("'","")
                                          precios.append(re.sub(" ","",o))
                                          favorito = 0 
                                          precio_anterior = 0
                                          count = 0                      


                  diccionario = dict(zip(articulos, precios))


                  with open('articulos.csv', 'w') as f:
                        writer = csv.writer(f)
                        for k, v in diccionario.items():
                              writer.writerow([k, v])
                  
scrap()