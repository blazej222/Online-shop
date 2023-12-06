import prestapyt
import pandas as pd
from config import *
import os
import io
import concurrent.futures
import cv2
from PIL import Image
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
                    prestashop.delete(plural, resource_ids=ids[i:i+100])
                except: pass
            print(f"{plural} deleted")
    except:
        #no features present
        pass

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
    category_schema["category"]["link_rewrite"]["language"]["value"] = name.replace(' ', '-')
    category_schema["category"]["description"] = ""
    prestashop.add("categories", category_schema)

def addProducts():
    data = pd.read_csv(directory+'products.csv',sep=';', header=0)
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        futures = [executor.submit(addProduct, row) for index, row in data.iterrows()]
        concurrent.futures.wait(futures)
    
       

def addProduct(row):
    print(row['Product ID'])
    product_schema['product']['id_manufacturer'] = manufacturerIDs[row['Brand']]
    product_schema["product"]["link_rewrite"]["language"]["value"] = row['Name'].replace('/', '-').replace(' ', '-')
    product_schema["product"]["price"] = round(float(row['Base price'])/1.23, 2)
    product_schema["product"]["id_tax_rules_group"] = 1
    product_schema["product"]["active"] = 1
    # product_schema["product"]["id_shop_default"] = 1
    product_schema["product"]["state"] = 1
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
    features = row['features'].split('|')
    productFeatures = []
    for feature in features:
        featureName = feature.split(': ')[0]
        featureValue = feature[feature.find(': ')+2:]
        # featureValue = feature.split(': ')[1]
        productFeatures.append({
            "id": featuresIDs[featureName],
            "id_feature_value": featureValuesIDs[featureValue]
        })
    product_schema["product"]["associations"]["product_features"]["product_feature"] = productFeatures  
    product_schema["product"]["description"]["language"]["value"] = row['Description']
    prodID = prestashop.add("products", product_schema)["prestashop"]["product"]["id"]
    addImages(f"{directory}img/{row['Product ID']}", prodID)    
def addManufacturers():
    data = pd.read_csv(directory+'manufacturers.csv', sep = ';', header=None)
    for index, row in data.iterrows():
        manufacturer_schema['manufacturer']['active'] = 1
        manufacturer_schema['manufacturer']['name'] = row[0]
        manufacturerIDs[row[0]] = prestashop.add('manufacturers', manufacturer_schema)["prestashop"]["manufacturer"]["id"]

def addFeatures():
    data = pd.read_csv(directory+'features.csv', sep = ';', header=0)
    for index, row in data.iterrows():
        try:
            row['Feature value'] = row['Feature value'].replace('->', '-').replace('=', ' ').replace('<', 'poniżej').replace('>', 'powyżej').replace('{', '(').replace('}', ')')
        except: pass
        if featuresIDs.get(row['Feature name']) is None:
            product_features_schema['product_feature']['name']['language']['value'] = row['Feature name']
            featuresIDs[row['Feature name']] = prestashop.add('product_features', product_features_schema)["prestashop"]["product_feature"]["id"]
        if featureValuesIDs.get(row['Feature value']) is None:
            product_features_values_schema['product_feature_value']['value']['language']['value'] = row['Feature value']
            product_features_values_schema['product_feature_value']['id_feature'] = featuresIDs[row['Feature name']] 
            featureValuesIDs[row['Feature value']] = prestashop.add('product_feature_values', product_features_values_schema)["prestashop"]["product_feature_value"]["id"]

def addImages(path, productID):
    imgs = os.listdir(path)
    fd = io.open(path+'/listing.png', "rb")
    content = fd.read()
    fd.close()
    addImage("listing.png",path, productID)
    # try:
    #     prestashop.add(f'/images/products/{productID}', files=[('image', 'cover.png', content)])
    # except:
    #     print("upload failed listing " + path)

    for img in imgs:
        addImage(img, path, productID)
        # if 'thumbnail' in img or 'listing' in img: continue
        # fd = io.open(path+'/'+img, "rb")
        # content = fd.read()
        # fd.close()
        # try:
        #     prestashop.add(f'/images/products/{productID}', files=[('image', img, content)])
        # except Exception as e:
        #     print(e)
        #     print("upload failed " + path+'\\'+img)


def addImage(name, path, productID, secondTry = False):
    fd = io.open(path+'/'+name, "rb")
    content = fd.read()
    fd.close()
    try:
        prestashop.add(f'/images/products/{productID}', files=[('image', name, content)])
    except Exception as e:
        print(f"{path}/{name} " + e)
        # if secondTry:
        #     print("still doesn't work")
        #     return
        # img = cv2.imread(f"{path}/{name}")
        # cv2.imwrite(f"{path}/{name}", img, [cv2.IMWRITE_PNG_COMPRESSION, 9])
        # im = Image.open(f"{path}/{name}").convert("RGB")
        # im.save(f"{path}/{name}", "png")
        # print(f"Image saved {path}/{name}")
        # addImage(f"{name}", path, productID, True)


api_url = 'http://localhost:8080/api'
prestashop = prestapyt.PrestaShopWebServiceDict(api_url, api_key)
category_schema = prestashop.get("categories", options={"schema": "blank"})
product_schema = prestashop.get("products", options={"schema": "blank"})
manufacturer_schema = prestashop.get("manufacturers", options={"schema": "blank"})
product_features_schema = prestashop.get("product_features", options={"schema": "blank"})
product_features_values_schema = prestashop.get("product_feature_values", options={"schema": "blank"})
del product_schema["product"]["position_in_category"]
del product_schema["product"]["associations"]["combinations"]

deleteAll('product', 'products')
deleteAll('product_feature', 'product_features')
deleteAll('manufacturer', 'manufacturers')
deleteAllCategories()
addCategories()
addManufacturers()
addFeatures()
addProducts()

