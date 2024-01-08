import random
import ast

import prestapyt
from config import *
from dataLoader import findCategoryID
from utils import *


def changeStock(element, prestashop, isMax=False):
    id = element['associations']["stock_availables"]["stock_available"]['id']
    stock_availables_schema = prestashop.get(f"stock_availables/{id}", )
    if isMax:
        stock_availables_schema["stock_available"]["quantity"] = 10
    else:
        stock_availables_schema["stock_available"]["quantity"] = random.randint(0, 10)
    prestashop.edit("stock_availables", stock_availables_schema)


def setStocks(verbose=False):
    prestashop = prestapyt.PrestaShopWebServiceDict(api_url, api_key)
    maxed_elements_count = 0

    reserved_categories = []
    reserved_categories.append(findCategoryID('Mysze'))
    reserved_categories.append(findCategoryID('Podkładki pod mysz'))
    reserved_categories.append(findCategoryID('Dyski SSD'))
    reserved_categories.append(findCategoryID('Zestawy mysz + klawiatura'))
    reserved_categories.append(findCategoryID('Płyty główne'))
    reserved_categories.append(findCategoryID('Torby do laptopów'))


    if verbose:
        println("Reserved category ids: " + str(reserved_categories))

    product_list = []
    data_file = open(output_directory + 'product_schema.csv', 'r')

    while True:
        data = data_file.readline()
        if data == "":
            break
        product_dict = ast.literal_eval(data)
        product_list.append(product_dict)
    data_file.close()

    elements = prestashop.get('products', options={'display': 'full'})
    element_no = 0
    for element in elements['products']['product']:
        try:
            if product_list[element_no]['product']['id_category_default'] in reserved_categories:
                isMax = True
                maxed_elements_count += 1
                if verbose:
                    println("Quantity 10 added to: " + product_list[element_no]['product']['name']['language']['value'])
            else:
                isMax = False
        except:
            pass

        changeStock(element, prestashop, isMax)
        element_no += 1

    if verbose:
        println("Maxed elements count: " + str(maxed_elements_count))

setStocks(verbose=True)
