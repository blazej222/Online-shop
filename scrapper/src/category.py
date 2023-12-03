import pandas as pd
import csv
from directory import *

def getCategories(navigationList):
    parentCategory = navigationList.find('li', class_='parent')
    
    categoryDict = {}
    tmp = []
    while parentCategory != None:
        name = parentCategory.find('span').text.strip()
        tmp.append(name)
        categoryDict[parentCategory.find('span').text] = getCategory(parentCategory, '', tmp)

        parentCategory = parentCategory.findNextSibling()

    #name = webObject.find('span').text.strip()
    #test = getCategory(webObject, '', [name])
    return categoryDict

def getCategory(webObject, prevName, savedCategories):
    categories = {}

    submenu = webObject.find('div', class_="submenu")
    while submenu !=None:
        category =  submenu.find('li', class_='parent')
        while category != None:
            name = category.find('span').text.strip()
            if name != prevName:
                savedCategories.append(name)
                categories[name] = getCategory(category, name, savedCategories)
            category = category.findNextSibling()
        submenu = submenu.findNextSibling()



    for categoryName in webObject.find_all('span'):
        name = categoryName.text.strip()
        if name not in categories and name != prevName and name not in savedCategories:
            categories[categoryName.text.strip()] = None
            savedCategories.append(name)

    
    return categories


def saveCategoriesToCsv(categories):
    headers = ['ID', 'Active (0/1)', 'Name', 'Parent category']
    with open(directory + 'categories.csv', 'w', encoding='UTF-8') as f:
        writer = csv.writer(f, delimiter =';', lineterminator="\n")
        writer.writerow(headers)
        for categoryName in categories:
            writer.writerow(['', '', categoryName.replace("/", "\\"), ''])
            writeRow(writer, categories[categoryName], categoryName.replace("/", "\\"))


def writeRow(writer, category, parent):
    for categoryName in category:
        writer.writerow(['', '', categoryName.replace("/", "\\"), parent])
        if category[categoryName] != None:
            writeRow(writer, category[categoryName], categoryName)
        
