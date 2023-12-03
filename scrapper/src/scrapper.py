from bs4 import BeautifulSoup
import pandas as pd
import requests
from product import Product
import time
from category import *
import csv

directory = '../scrapped/'
directory = 'C:\\scrapped\\'

def getPageResponse(URL):
         print(URL)
         while True:
            try:
                return requests.get(URL)
            except:
                time.sleep(5)

def saveManufacturers():
    with open(directory + 'manufacturers.csv', 'w', encoding='UTF-8') as f:
        writer = csv.writer(f, delimiter =';', lineterminator="\n")
        for manufacturer in manufacturers:
            writer.writerow([manufacturer])


BASE_URL = "https://foxkomputer.pl"
start = time.time()

page = requests.get(BASE_URL)
soup = BeautifulSoup(page.content, "html.parser")

soup.find('ul', class_='menu-list large standard')

products = []
navigationList = soup.find('ul', class_='menu-list large standard')
parentCategory = navigationList.find('li', class_='parent')
parentCategories = []
manufacturers = []

categoryDict = getCategories(navigationList)
saveCategoriesToCsv(categoryDict)


while parentCategory != None:
    parentCategories.append(parentCategory)
    parentCategory = parentCategory.findNextSibling()
for category in categoryDict: 
        print('---------------------------------------')
        print(category)
        print('--' + str(categoryDict[category]))
with open(directory + 'products.csv', 'w', encoding='UTF-8') as f:
    writer = csv.writer(f, delimiter =';', lineterminator="\n")
    headers = ['Product ID', 'Active', 'Name', 'Categories', 'Price tax excluded', 'Tax rules ID', 'Cost price', 'On sale',
         'Discount amount', 'Discount percent', 'Discount from', 'Discount to', 'References', 'Supplier references',
         'Suppliers', 'Brand', 'EAN13', 'UPC', 'EPN', 'Ecotax', 'Width', 'Height', 'Depth', 'Weight', 'Delivery time of in-stock',
         'Delivery time of out-of-stock', 'Quantity', 'Minimal quantity', 'Low stock level', 'Send me an email', 
         'Visibility', 'Additional shipping cost', 'Unit for base price', 'Base price', 'Summary', 'Description',
         'Tags', 'Meta title', 'Meta keywords', 'Meta decription', 'Rewritten URL', 'Label when in stock',
         'Label when backorder allowed', 'Avaialble for order', 'Product availability date', 'Product creation date',
         'Show price', 'Image URLs', 'Image alt texts', 'Delete existing images', 'features', 'Available online only',
         'Condition']
    writer.writerow(headers)
    for category in parentCategories:#soup.find_all('li', class_='parent'):
        href = category.find('a')['href']
        while True:
            categoryPage = getPageResponse(BASE_URL + href)
            pageContent = BeautifulSoup(categoryPage.content, "html.parser")
            for element in pageContent.find_all("div", class_="product-inner-wrap"):
                prodImage = element.find('a', class_="prodimage f-row")
                productURL = prodImage["href"]
                product = Product(productURL)
                try:
                    product.manufacturer = element.find('a', class_='brand').text.strip()
                except:pass
                if product.manufacturer not in manufacturers:
                    manufacturers.append(product.manufacturer)
                product._saveImg("listing", BASE_URL + prodImage.find('img')['data-src'])
                products.append(product)
                product.writeToCsv(writer)

            
            try:
                paginator = pageContent.find('ul', class_='paginator')
                nextPageButton = paginator.find('li', class_='last')
                href = nextPageButton.find('a')['href']
            except:
                break
        Product.writeFeaturesToCsv()
    saveManufacturers()



for product in products: print(product.name)
print(f'Product scrapped: {len(products)}')

end = time.time()
print(end-start)