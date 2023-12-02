import prestapyt
import pandas as pd
from directory import *

categoriesDir = {}
featuresIDs = {}
featureValuesIDs = {}
manufacturerIDs = {}

def deleteAllCategories():
    ids = []
    for category in prestashop.get("categories")["categories"]["category"]:
        if int(category["attrs"]["id"]) not in [1, 2]:
            ids.append(int(category["attrs"]["id"]))
    if ids:
        prestashop.delete("categories", resource_ids=ids)
        print("Categories deleted")

def addCategories():
    data = pd.read_csv(directory+'categories.csv',sep=';', header=0)
    for index, row in data.iterrows():
        if pd.isnull(row['Parent category']):
            parentID = 2
        else:
            ID = findCategoryID(row['Parent category'])
            if ID is not None:
                parentID = ID
        addCategory(row['Name'], parentID)
    pass

def findCategoryID(name):
    categories = prestashop.get("categories")["categories"]['category']
    if name in categoriesDir:
        return categoriesDir[name]
    for element in categories:
        category = prestashop.get(f"categories/{element['attrs']['id']}")
        if category["category"]["name"]["language"]["value"] == name:
            ID = element['attrs']['id']
            categoriesDir[name] = ID
            return ID
    return None


def addCategory(name, parentID):
    category_schema["category"]["name"]["language"]["value"] = name
    category_schema["category"]["is_root_category"] = 0
    category_schema["category"]["id_parent"] = parentID
    category_schema["category"]["active"] = 1
    #category_schema["category"]["link_rewrite"]["language"][0]["value"] = "TEST-CAT"
    category_schema["category"]["description"] = "Lorem ipsum"
    prestashop.add("categories", category_schema)

def addProducts():
    data = pd.read_csv(directory+'products.csv',sep=';', header=0)
    for index, row in data.iterrows():
        print(row['Product ID'])
        #product_schema['product']['id'] = row['Product ID']
        product_schema['product']['active'] = 1
        product_schema['product']['associations']['categories']['category']['id'] = findCategoryID(str(data['Categories']))
        product_schema["product"]["link_rewrite"]["language"]["value"] = data['Name'].replace('/', '-').replace(' ', '-')
        product_schema["product"]["price"] = data['Base price']
        product_schema["product"]["active"] = 1
        product_schema["product"]["state"] = 1
        product_schema["product"]["available_for_order"] = 1
        product_schema["product"]["minimal_quantity"] = 1
        product_schema["product"]["show_price"] = 1
        product_schema["product"]["name"]["language"]["value"] = data['Name']
        product_schema["product"]["id_category_default"] = 2
        product_schema["product"]["meta_title"]["language"]["value"] = 'FILL IN'
        product_schema["product"]["associations"]["product_features"]["product_feature"] = ''
        prestashop.add("products", product_schema)

def addManufacturers():
    data = pd.read_csv(directory+'manufacturers.csv', sep = ';', header=None)
    for index, row in data.iterrows():
        manufacturer_schema['manufacturer']['active'] = 1
        manufacturer_schema['manufacturer']['name'] = row[0]
        manufacturerIDs[row[0]] = prestashop.add('manufacturers', manufacturer_schema)

def addFeatures():
    data = pd.read_csv(directory+'features.csv', sep = ';', header=0)
    for index, row in data.iterrows():
        if featuresIDs.get(row['Feature name']) is None:
            product_features_schema['product_feature']['name'] = row['Feature name']
            featuresIDs[row['Feature name']] = prestashop.add('product_features', product_features_schema)
        if featureValuesIDs.get(row['Feature value']) is None:
            product_features_values_schema['product_feature_value']['value']['language'] = row['Feature value']
            product_features_values_schema['product_feature_value']['id_feature'] = featuresIDs[row['Feature name']] 
            featureValuesIDs[row['Feature value']] = prestashop.add('product_feature_values')



api_url = 'http://localhost:8080/api'
api_key = 'DHXYIV2PNQSPGC173MECU45Q4GJB9GGM'


prestashop = prestapyt.PrestaShopWebServiceDict(
    api_url, api_key)
category_schema = prestashop.get("categories", options={"schema": "blank"})
product_schema = prestashop.get("products", options={"schema": "blank"})
manufacturer_schema = prestashop.get("manufacturers", options={"schema": "blank"})
product_features_schema = prestashop.get("product_features", options={"schema": "blank"})
product_features_values_schema = prestashop.get("product_feature_values", options={"schema": "blank"})


# deleteAllCategories()
# addCategories()
addManufacturers()
addFeatures()
#addProducts()

