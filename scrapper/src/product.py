import requests
from bs4 import BeautifulSoup
import os

BASE_URL = "https://foxkomputer.pl"

class Product:
    name: str
    price: float
    manufacturer: str
    specs: list
    imgURL: str

    

    def __init__(self, productURL):
        self.__productURL = productURL
        self._initialize()
        

    def _initialize(self):
        self._fetchProductDetails(self.__productURL)

    def _fetchProductDetails(self, productURL):
        productPage = requests.get(BASE_URL+ productURL)
        soup = BeautifulSoup(productPage.content, "html.parser")
        mainContainer = soup.find('div', class_="centercol s-grid-12")
        print(mainContainer)
        self.name = soup.find('h1', class_='name').text.strip()
        self._fetchProductAttr(mainContainer)
        self._saveImgs(self.name, BASE_URL+(mainContainer.find('img', class_="photo js__open-gallery")["src"]))



    def _fetchProductAttr(self, mainContainer):
        div = mainContainer.find('div', class_="innerbox tab-content product-attributes zebra")
        table = div.find('table', class_='table')
        rows = table.find_all("tr")
        productSpecs = []
        for row in rows:
            columns = row.find_all("td")
            rowName = columns[0].text.strip()
            rowValue = columns[1].text.strip()
            attrStruct = {"name": rowName,
                            "value": rowValue}
            productSpecs.append(attrStruct)
        self.specs = productSpecs

    def _saveImgs(self, imgName, imgURL):
        req = requests.get(imgURL).content
        try:
            req = str(req, "utf-8")
        except UnicodeDecodeError:
            print(os.getcwd())
            with open(f"scrapper\scrapped\img\{imgName}.jpg", "wb+") as f:
                f.write(req)
