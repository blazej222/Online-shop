import requests
from bs4 import BeautifulSoup
import os
from time import sleep

BASE_URL = 'https://foxkomputer.pl'
MAX_RETRIES = 10

class Product:
    name: str
    price: float
    manufacturer: str
    specs: list
    imgURLs: []


    id: int
    category: str
    description: str

    def __init__(self, productURL):
        self.__productURL = productURL
        self.imgURLs = []
        self.manufacturer = ''
        self._initialize()
        

    def _initialize(self):
        self._fetchProductDetails(self.__productURL)

    def _fetchProductDetails(self, productURL):
        productPage = self._getPageResponse(BASE_URL+ productURL)
        soup = BeautifulSoup(productPage.content, 'html.parser')
        mainContainer = soup.find('div', class_='centercol s-grid-12')
        self.name = soup.find('h1', class_='name').text.strip()
        self.id = soup.find('button', class_='availability-notifier-btn btn btn-red')['data-product-id']
        self.category = mainContainer.find('div', id='box_productfull')['data-category']
        self.description =  mainContainer.find('div', itemprop="description").find('p').text.strip()
        self.price = mainContainer.find('div', class_ ='price').find('em', class_='main-price').text.replace(' zł', '').replace(',', '.').replace(' ', '')
        self._fetchProductAttr(mainContainer)
        self._fetchGallery(mainContainer)



    def _fetchProductAttr(self, mainContainer):
        div = mainContainer.find('div', class_='innerbox tab-content product-attributes zebra')
        if div == None:
            print("NO SPECS TABLE!")
            return
        table = div.find('table', class_='table')
        rows = table.find_all('tr')
        productSpecs = []
        for row in rows:
            columns = row.find_all('td')
            rowName = columns[0].text.strip()
            rowValue = columns[1].text.strip()
            if rowName == 'Producent':
                self.manufacturer = rowValue
            attrStruct = {'name': rowName,
                            'value': rowValue}
            productSpecs.append(attrStruct)
        self.specs = productSpecs

    def _fetchGallery(self, mainContainer):
        gallery = mainContainer.find('div', class_='smallgallery row')
        images = gallery.find_all('a', class_='gallery js__gallery-anchor-image')
        if len(images) > 0:
            ind = 0
            for image in images:
                self._saveImg(str(ind), BASE_URL + image['href'])
                thumbnail=image.find('img')
                self._saveImg(f'{ind}-thumbnail', BASE_URL + thumbnail['src'])
                ind+=1
        else:
            self._saveImg('0', BASE_URL+(mainContainer.find('img', class_='js__open-gallery')['src']))

    def _saveImg(self, imgName:str, imgURL:str):
        if not ('thumbnail' in imgName):
            self.imgURLs.append(imgURL)
        #ignore already downloaded imgs
        if os.path.exists(f'../scrapped/img/{self.id}/{imgName}.jpg'): return
        req = self._getPageResponse(imgURL).content
        try:
            req = str(req, 'utf-8')
        except UnicodeDecodeError:
            if not os.path.exists(f'../scrapped/img/{self.id}'):
                os.mkdir(f'../scrapped/img/{self.id}')
            with open(f'../scrapped/img/{self.id}/{imgName}.jpg', 'wb+') as f:
                f.write(req)

    @staticmethod
    def _getPageResponse(URL):
         print(URL)
         retries = 0
         while retries < MAX_RETRIES:
            try:
                return requests.get(URL)
            except:
                retries+=1
                sleep(5)
    
    def writeToCsv(self, writer):
        imgUrls = ""
        for i in range(len(self.imgURLs)):
            if i == 0:
                imgUrls = self.imgURLs[i]
            imgUrls+=', ' + self.imgURLs[i]
        
        features = ""
        for feature in self.specs:
            features+=f"{feature['name']}: {feature['value']},"
        if len(features) > 0:
            features = features[:-1]
        
        if len(self.name) > 128:
            self.name = self.name[:128]

        writer.writerow([self.id, #ID
                          1, #Active
                          self.name, #Name
                          self.category, #Categories
                          self.price, #Price tax excluded
                          '', #Tax rule ID
                          #self.price, #Price tax included
                          self.price, #Cost price
                          0, #On sale (0/1)
                          0, #Discount amount
                          0, #Discount percent
                          '', #Discount from (yyyy-mm-dd)
                          '', #Discount to (yyyy-mm-dd)
                          '', #Reference #
                          '', #Supplier reference #
                          '', #Supplier
                          self.manufacturer, #Brand
                          '', #EAN13
                          '', #UPC
                          '', #MPN
                          '', #Ecotax
                          '', #Width
                          '', #Height
                          '', #Depth
                          '', #Weight
                          '', #Delivery time of in-stock products:
                          '', #Delivery time of out-of-stock products with allowed orders:
                          '', #Quantity
                          '', #Minimal quantity
                          '', #Low stock level
                          '', #Send me an email when the quantity is under this level
                          '', #Visibility
                          '', #Additional shipping cost
                          '', #Unit for base price
                          self.price, #Base price
                          self.price, #Summary
                          self.description, #Description
                          '', #Tags
                          '', #Meta title
                          '', #Meta keywords
                          '', #Meta description
                          '', #Rewritten URL
                          '', #Label when in stock
                          '', #Label when backorder allowed
                          1, #Available for order (0 = No, 1 = Yes)
                          '', #Product availability date
                          '', #Product creation date
                          1, #Show price (0 = No, 1 = Yes)/
                          imgUrls, #Image URLs (x,y,z...)
                          '', #Image alt texts (x,y,z...)
                          1, #Delete existing images (0 = No, 1 = Yes)
                          features, #Feature (Name:Value:Position:Customized)
                          0, #Available online only (0 = No, 1 = Yes)
                          'new', #Condition
                          ])
