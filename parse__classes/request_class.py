import requests
from bs4 import BeautifulSoup

from parse__classes.url_class import URL


class Request(URL): # Создание класса Request, который наследует URL
    def __init__(self):
        super().__init__()  #  функции super(), чтобы инициализировать защищенные поля
        self._Requests_data_ru = requests.get(self._url_ru)
        self._Requests_data_ukr = requests.get(self._url_ukr)
        self._Requests_data_avab = requests.get(self._url)
        self._Bs_data_ru = BeautifulSoup(self._Requests_data_ru.content, "xml")
        self._Bs_data_ukr = BeautifulSoup(self._Requests_data_ukr.content, "xml")
        self._Offers_ru = self._Bs_data_ru.find_all('offer')
        self._Offers_ukr = self._Bs_data_ukr.find_all('offer')