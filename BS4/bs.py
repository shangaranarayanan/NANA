import requests
from bs4 import BeautifulSoup

web = "https://shop.ramdass.org/collections/books"
request=requests.get(web)

print(request.status_code)

soup = BeautifulSoup(request.text,"html.parser")

names = soup.find_all(class_="product__grid__title")
print(names)

for i in names:
    print(i.text)

name =[i.text.replace("\n","").strip() for i in names]
print(name)

prices = soup.find_all(class_="price")
print(prices)

price =[i.text.replace("\n","").strip() for i in prices]
print(price)
