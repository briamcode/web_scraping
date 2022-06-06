#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests
import csv
import re

def links():
      url = 'https://celulares.mercadolibre.com.co/#CATEGORY_ID=MCO1055&S=hc_celulares-y-telefonos&c_id=undefined&c_element_order=undefined&c_campaign=CELULARES-Y-SMARTPHONES&c_uid=7e196070-e2d0-11ec-98dd-8d5fc424b34b'
      page = requests.get(url)
      soup = BeautifulSoup(page.content, 'html.parser')

      #Scrap file
      scrap = soup.find_all('a', class_='ui-search-item__group__element ui-search-link')

      links = list()

      count = 0

      for i in (scrap):
            links.append(i)
            count += 1


      with open('links.csv', 'w') as f:
            writer = csv.writer(f)
            for k in links:
                  x = re.search("(?P<url>https?://[^\s]+)", str(k)).group("url")
                  writer.writerow([x])

