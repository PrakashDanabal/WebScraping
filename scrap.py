from typing import Text
import requests
from bs4 import BeautifulSoup


def sorthn(hnlist):
    return(sorted(hnlist,key=lambda k:k['hnvote'],reverse=True))



def create_custom_hn(souptitle,soupsubtext):
    hn=[]
    for idx,item in enumerate(souptitle):
        hntitle=item.getText()
        hnlink=item.get('href')
        hnvote=soupsubtext[idx].select('.score')
        
        if len(hnvote):
            vote=int(hnvote[0].getText().replace(' points',''))
            if vote>99:
                hn.append({'title':hntitle,'href':hnlink,'hnvote':vote})
        
    return(sorthn(hn))

        
    

url='https://news.ycombinator.com/'
res=requests.get(url)
soup=BeautifulSoup(res.text,'html.parser')
souptitle=soup.select('.titlelink')
soupsubtext=soup.select('.subtext')

print(create_custom_hn(souptitle,soupsubtext))
