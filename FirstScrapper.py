from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.ashlandpump.com/products")
bsObj = BeautifulSoup(html.read(),"html.parser")
productList = bsObj.findAll("li",{"class":"product"})
for product in productList:
    print ("Product Name: " + product.a.get_text() + " | Image: " + product.a.get("href"))
    print("-"*150)
