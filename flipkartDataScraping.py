import requests
from bs4 import BeautifulSoup
import pandas as pd

url="https://www.flipkart.com/search?q=mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off"

req=requests.get(url)
content=BeautifulSoup(req.content,'html.parser')
name=content.find_all('div',{'class':'_4rR01T'})
price=content.find_all('div',{'class':'_30jeq3 _1_WHN1'})
rating=content.find_all('div',{'class':'_3LWZlK'})
nm=[]
pr=[]
rt=[]
for i in name:
    nm.append(i.text)
for i in price:
    pr.append(i.text)
for i in range(len(nm)):
    rt.append(rating[i].text)
data={'NAME':nm,'PRICE':pr,'RATING':rt}
df=pd.DataFrame(data)
print(df)