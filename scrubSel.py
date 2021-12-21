from bs4 import BeautifulSoup
import requests


url='http://allselenium.info/python-selenium-commands-cheat-sheet-frequently-used/'
resp=requests.get(url)
#print(resp)
webpage=BeautifulSoup(resp.text,'html.parser')
title=webpage.select('.post-content-inner')
with open('/home/meetdprakash/python/work/WebScraping/selenium.txt','a') as cheatsheet:
    for title_name in title:
        #print(title_name.getText())
        cheatsheet.write(f'\n{title_name.getText()}')
