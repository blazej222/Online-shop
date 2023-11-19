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
    imgURL: str
    id: int
    category: str

    def __init__(self, productURL):
        self.__productURL = productURL
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
        #ignore already downloaded imgs
        if os.path.exists(f'scrapper\scrapped\img\{self.id}\{imgName}.jpg'): return
        req = self._getPageResponse(imgURL).content
        try:
            req = str(req, 'utf-8')
        except UnicodeDecodeError:
            if not os.path.exists(f'scrapper\scrapped\img\{self.id}'):
                os.mkdir(f'scrapper\scrapped\img\{self.id}')
            with open(f'scrapper\scrapped\img\{self.id}\{imgName}.jpg', 'wb+') as f:
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
