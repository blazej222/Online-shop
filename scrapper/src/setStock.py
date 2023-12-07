import prestapyt
from config import *
import concurrent.futures

def changeStock(element):
    id = element['attrs']['id']
    stock_availables_schema = prestashop.get(f"stock_availables/{id}", )
    stock_availables_schema["stock_available"]["quantity"] = 10
    prestashop.edit("stock_availables", stock_availables_schema)

prestashop = prestapyt.PrestaShopWebServiceDict(api_url, api_key)
elements = prestashop.get('stock_availables')["stock_availables"]["stock_available"]#['stock_availables']

with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
    futures = [executor.submit(changeStock, element) for element in elements]
    concurrent.futures.wait(futures)
