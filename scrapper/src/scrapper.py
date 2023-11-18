from bs4 import BeautifulSoup
import pandas as pd
import requests
from product import Product

BASE_URL = "https://foxkomputer.pl"
URL = "https://foxkomputer.pl/pl/c/Laptopy/222"

page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

products = []

for element in soup.find_all("div", class_="product-inner-wrap"):
    prodImage = element.find('a', class_="prodimage f-row")
    productURL = prodImage["href"]
    products.append(Product(productURL))

for product in products: print(product.name)