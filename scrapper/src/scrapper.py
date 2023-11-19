from bs4 import BeautifulSoup
import pandas as pd
import requests
from product import Product
import time

def getPageResponse(URL):
         print(URL)
         while True:
            try:
                return requests.get(URL)
            except:
                time.sleep(5)

BASE_URL = "https://foxkomputer.pl"
URL = "https://foxkomputer.pl/pl/c/Laptopy/222"
start = time.time()

page = requests.get(BASE_URL)
soup = BeautifulSoup(page.content, "html.parser")

soup.find('ul', class_='menu-list large standard')

products = []
for category in soup.find_all('li', class_='parent'):
    href = category.find('a')['href']
    while True:
        categoryPage = getPageResponse(BASE_URL + href)
        pageContent = BeautifulSoup(categoryPage.content, "html.parser")
        for element in pageContent.find_all("div", class_="product-inner-wrap"):
            prodImage = element.find('a', class_="prodimage f-row")
            productURL = prodImage["href"]
            product = Product(productURL)
            product._saveImg("listing", BASE_URL + prodImage.find('img')['data-src'])
            products.append(product)
        
        try:
            paginator = pageContent.find('ul', class_='paginator')
            nextPageButton = paginator.find('li', class_='last')
            href = nextPageButton.find('a')['href']
        except:
             break
        


for product in products: print(product.name)
print(f'Product scrapped: {len(products)}')

end = time.time()
print(end-start)