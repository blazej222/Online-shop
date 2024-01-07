import copy

import prestapyt
import pandas as pd
from config import *
import os
import io
import concurrent.futures
import cv2
from PIL import Image
from utils import *
import csv

categoriesDir = {}
featuresIDs = {}
featureValuesIDs = {}
manufacturerIDs = {}


def deleteAll(singular, plural):
    ids = []
    try:
        for feature in prestashop.get(plural)[plural][singular]:
            ids.append(int(feature["attrs"]["id"]))
        if ids:
            for i in range(0, len(ids), 100):
                try:
                    prestashop.delete(plural, resource_ids=ids[i:i + 100])
                except:
                    pass
            println(f"{plural} deleted")
    except:
        # no features present
        pass


def deleteAllCategories():
    ids = []
    for category in prestashop.get("categories")["categories"]["category"]:
        if int(category["attrs"]["id"]) not in [1, 2]:
            ids.append(int(category["attrs"]["id"]))
    if ids:
        prestashop.delete("categories", resource_ids=ids)
        println("Categories deleted")


def addCategories():
    data = pd.read_csv(output_directory + 'categories.csv', sep=';', header=0)
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
    prestashop = prestapyt.PrestaShopWebServiceDict(api_url, api_key)

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
    category_schema["category"]["link_rewrite"]["language"]["value"] = name.replace(' ', '-')
    category_schema["category"]["description"] = ""
    prestashop.add("categories", category_schema)
    println(f"Added category: {name}")


def addProducts():
    data = pd.read_csv(output_directory + 'products.csv', sep=';', header=0)
    data.to_csv(output_directory + 'dataframe.csv', sep="\t")
    product_schema_file = open(output_directory + 'product_schema.csv', 'w')
    # replace " characters in names
    # for index, row in data.iterrows():
    #    row['Name'] = row['Name'].replace('"', '').replace('™', '')

    # with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
    # futures = [executor.submit(addProduct, row) for index, row in data.iterrows()]
    # oncurrent.futures.wait(futures)

    for index, row in data.iterrows():
        addProduct(row, product_schema_file)

    product_schema_file.close()
    println("Added products")


def addProduct(row, schema_file):
    product_schema['product']['id_manufacturer'] = manufacturerIDs[row['Brand']]
    product_schema["product"]["link_rewrite"]["language"]["value"] = row['Name'].replace('/', '-').replace(' ', '-')
    product_schema["product"]["price"] = round(float(row['Base price']) / 1.23, 2)
    product_schema["product"]["id_tax_rules_group"] = 1
    product_schema["product"]["active"] = 1
    # product_schema["product"]["id_shop_default"] = 1
    product_schema["product"]["statde"] = 1
    product_schema["product"]["available_for_order"] = 1
    product_schema["product"]["minimal_quantity"] = 0
    product_schema["product"]["show_price"] = 1
    product_schema["product"]["name"]["language"]["value"] = row['Name']
    product_schema["product"]["id_category_default"] = findCategoryID(row['Categories'])
    product_schema["product"]["associations"]["categories"]['category']['id'] = findCategoryID(row['Categories'])
    # {
    #     "category": [
    #         {"id": categoriesDir[findCategoryID(row['Categories'])]}
    #     ],
    # }
    if pd.isnull(row['features']):
        product_schema["product"]["associations"]["product_features"]["product_feature"] = []
    else:
        features = str(row['features']).split('|')
        productFeatures = []
        for feature in features:
            featureName = feature.split(': ')[0]
            featureValue = feature[feature.find(': ') + 2:]
            # featureValue = feature.split(': ')[1]
            if featureName != '' and featureValue != '':
                productFeatures.append({
                    "id": featuresIDs[featureName],
                    "id_feature_value": featureValuesIDs[
                        featureValue.replace('->', '-').replace('=', ' ')
                        .replace('{', '(').replace('}', ')')
                        .replace('<', 'poniżej ').replace('>', 'powyżej ')
                    ]
                })
        product_schema["product"]["associations"]["product_features"]["product_feature"] = productFeatures
    if pd.isnull(row['Description']):
        product_schema["product"]["description"]["language"]["value"] = ""
    else:
        product_schema["product"]["description"]["language"]["value"] = row['Description']
    prodID = prestashop.add("products", product_schema)["prestashop"]["product"]["id"]

    addImages(f"{output_directory}img/{row['Product ID']}", prodID)

    product_schema_dto = copy.deepcopy(product_schema)
    product_schema_dto['product']['id'] = prodID
    schema_file.write(str(product_schema_dto) + '\n')
    println(f"Added product {row['Product ID']}")


def addManufacturers():
    data = pd.read_csv(output_directory + 'manufacturers.csv', sep=';', header=None)
    for index, row in data.iterrows():
        manufacturer_schema['manufacturer']['active'] = 1
        manufacturer_schema['manufacturer']['name'] = row[0]
        manufacturerIDs[row[0]] = \
            prestashop.add('manufacturers', manufacturer_schema)["prestashop"]["manufacturer"]["id"]
        println(f"Added manufacturer: {row[0]}")


def addFeatures():
    feature_dict = open(output_directory + "feature_dict.csv", 'w')
    data = pd.read_csv(output_directory + 'features.csv', sep=';', header=0)
    for index, row in data.iterrows():
        try:
            row['Feature value'] = (row['Feature value'].replace('->', '-')
                                    .replace('=', ' ').replace('{', '(').replace('}', ')')
                                    .replace('<', 'poniżej ').replace('>', 'powyżej ')
                                    )
        except:
            pass
        if featuresIDs.get(row['Feature name']) is None:
            product_features_schema['product_feature']['name']['language']['value'] = row['Feature name']
            featuresIDs[row['Feature name']] = \
                prestashop.add('product_features', product_features_schema)["prestashop"]["product_feature"]["id"]
        if featureValuesIDs.get(row['Feature value']) is None:
            product_features_values_schema['product_feature_value']['value']['language']['value'] = row['Feature value']
            product_features_values_schema['product_feature_value']['id_feature'] = featuresIDs[row['Feature name']]
            featureValuesIDs[row['Feature value']] = \
                prestashop.add('product_feature_values', product_features_values_schema)["prestashop"][
                    "product_feature_value"]["id"]

    feature_dict.write(str(featuresIDs))
    feature_dict.write('\n')
    feature_dict.write(str(featureValuesIDs))
    feature_dict.close()
    
    println("Added features")


def addImages(path, productID):
    imgs = os.listdir(path)

    # FIXME: is this necessary?
    fd = io.open(path + '/listing.png', "rb")
    content = fd.read()
    fd.close()

    addImage("listing.png", path, productID)
    for img in imgs:
        if img != "listing.png":
            addImage(img, path, productID)
        # if 'thumbnail' in img or 'listing' in img: continue
        # fd = io.open(path+'/'+img, "rb")
        # content = fd.read()
        # fd.close()
        # try:
        #     prestashop.add(f'/images/products/{productID}', files=[('image', img, content)])
        # except Exception as e:
        #     println(e)
        #     println("upload failed " + path+'\\'+img)

    println(f"Added images for {path}")


def addImage(name, path, productID):
    fd = io.open(path + '/' + name, "rb")
    content = fd.read()
    fd.close()
    try:
        prestashop.add(f'/images/products/{productID}', files=[('image', name, content)])
        # println(f"Added image {path}/{name}")
    except Exception as e:
        println(f"EXCEPTION: {path}/{name} " + e)

def main():
    deleteAll('product', 'products')
    deleteAll('product_feature', 'product_features')
    deleteAll('manufacturer', 'manufacturers')
    deleteAllCategories()
    addCategories()
    addManufacturers()
    addFeatures()
    addProducts()


if __name__ == '__main__':
    prestashop = prestapyt.PrestaShopWebServiceDict(api_url, api_key)
    category_schema = prestashop.get("categories", options={"schema": "blank"})
    product_schema = prestashop.get("products", options={"schema": "blank"})
    manufacturer_schema = prestashop.get("manufacturers", options={"schema": "blank"})
    product_features_schema = prestashop.get("product_features", options={"schema": "blank"})
    product_features_values_schema = prestashop.get("product_feature_values", options={"schema": "blank"})
    del product_schema["product"]["position_in_category"]
    del product_schema["product"]["associations"]["combinations"]
    main()
