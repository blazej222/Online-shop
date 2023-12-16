import prestapyt
from config import *
import concurrent.futures
import random


def changeWeight(element):
    productID = element['attrs']['id']
    product_schema = prestashop.get(f"products", productID)
    product_schema["product"]["weight"] = str(float(random.randint(1, 10)))
    del product_schema["product"]["position_in_category"]
    del product_schema["product"]["associations"]["combinations"]
    del product_schema["product"]["manufacturer_name"]
    del product_schema["product"]["quantity"]
    prestashop.edit(f"products/{productID}", product_schema)


prestashop = prestapyt.PrestaShopWebServiceDict(api_url, api_key)
elements = prestashop.get('products')["products"]["product"]  # ['stock_availables']

with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
    futures = [executor.submit(changeWeight, element) for element in elements]
    concurrent.futures.wait(futures)
