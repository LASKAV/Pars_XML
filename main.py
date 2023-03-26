# Замер времени
import time

import numpy
import pandas
from bs4 import BeautifulSoup
import requests

# Цвета для вывода в консоль
from colorama import init, Fore

class URL:
    # Поля protected
    _url_ru = None  # None это NULL (C++)
    _url_ukr = None
    _url = None
    def __init__(self):
        self._url_ru = "https://aveon.net.ua/products_feed.xml?hash_tag=7b71fadcc4a12f03cf26a304da032fba&sales_notes=&product_ids=&label_ids=&exclude_fields=&html_description=1&yandex_cpa=&process_presence_sure=&languages=ru&group_ids="
        self._url_ukr = "https://aveon.net.ua/products_feed.xml?hash_tag=7b71fadcc4a12f03cf26a304da032fba&sales_notes=&product_ids=&label_ids=&exclude_fields=&html_description=1&yandex_cpa=&process_presence_sure=&languages=uk&group_ids="
        self._url = "https://aveon.net.ua/google_merchant_center.xml?hash_tag=6d58bc5c0f96eae8b69854ec4c543e6d&product_ids=&label_ids=&export_lang=ru&group_ids="
    def Set_Url_ru(self,URL_RU:str):
        self._url_ru = URL_RU
    def Set_Url_ukr(self,URL_UKR:str):
        self._url_ukr = URL_UKR
    def Set_Url(self,URL:str):
        self._url = URL
    def Show_URL(self):
        init(autoreset=True)  # поддерживаться вывод на Windows 10.
        print(f"\n{Fore.RED}URL_RU: {self._url_ru}"
              f"\nURL_UKR: {self._url_ukr}"
              f"\nURL: {self._url}")
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
class Product:
    _Product_code = []
    _Product_title = []
    _Product_title_ukr = []
    _Product_description = []
    _Product_description_ukr = []
    _Product_pictures = []
    _Product_price = []
    _Product_availability = []
    _Product_IP_item = []
    _Product_currencyId = []
    _Product_Unit_measurement = []
    _Product_country_of_origin = []
    _Product_vendor = []
    _Product_Item_type = []
    _Product_price_file = []
    _Product_Note = []
    _Pics = []
    _Product_pic_str = []
    def __init__(self):
        self._Product_code = []
        self._Product_title = []
        self._Product_title_ukr = []
        self._Product_description = []
        self._Product_description_ukr = []
        self._Product_pictures = []
        self._Product_price = []
        self._Product_availability = []
        self._Product_IP_item = []
        self._Product_currencyId = []
        self._Product_Unit_measurement = []
        self._Product_country_of_origin = []
        self._Product_vendor = []
        self._Product_Item_type = []
        self._Product_price_file = []
        self._Product_Note = []
        self._Pics = []
        self._Product_pic_str = []
class Parse(Request,Product): # class абстрактный Parse
    def __init__(self):
        super().__init__()
        for offer in self._Offers_ukr:
            self._Product_title_ukr.append(offer.find('name').text)
            self._Product_description_ukr.append(offer.find('description').text)
        for offer in self._Offers_ru:
            self._Product_title.append(offer.find('name').text)
            self._Product_description.append(offer.find('description').text)
            self._Pics = offer.find_all('picture')
            self._Product_pic_str = ", ".join(str(pic.text) for pic in self._Pics)
            self._Product_pictures.append(self._Product_pic_str)
            self._Product_price.append(offer.find('price').text)
            self._Product_availability.append(offer['available'])
            self._Product_IP_item.append(offer['id'])
            self._Product_currencyId.append(offer.find('currencyId').text)
            self._Product_Unit_measurement.append("шт.")
            self._Product_Item_type.append("r")
            self._Product_Note.append(" ")
            self._Product_country_of_origin.append(getattr(offer.find('country_of_origin'), 'text', None))
            self._Product_vendor.append(getattr(offer.find('vendor'), 'text', None))
            self._Product_code.append(getattr(offer.find('vendorCode'), 'text', None))
    def Show_Parse(self):
        print("Product Code: ", self._Product_code)
        print("Product Title: ", self._Product_title)
        print("Product Title (ukr): ", self._Product_title_ukr)
        print("Product Description: ", self._Product_description)
        print("Product Description (ukr): ", self._Product_description_ukr)
        print("Product Pictures: ", self._Product_pictures)
        print("Product Price: ", self._Product_price)
        print("Product Availability: ", self._Product_availability)
        print("Product IP Item: ", self._Product_IP_item)
        print("Product Currency ID: ", self._Product_currencyId)
        print("Product Unit Measurement: ", self._Product_Unit_measurement)
        print("Product Country of Origin: ", self._Product_country_of_origin)
        print("Product Vendor: ", self._Product_vendor)
        print("Product Item Type: ", self._Product_Item_type)
        print("Product Price File: ", self._Product_price_file)
        print("Product Note: ", self._Product_Note)

if __name__ == '__main__':
    start_time = time.time()
    _URL = URL()
    _URL.Show_URL()
    _Requst = Request()
    _Product = Product()
    _Parse = Parse()
    _Parse.Show_Parse()
    end_time = time.time()
    elapsed_time = (end_time - start_time) / 60
    # Сделать класс для Exel таблицы
    #input = {
    #     'Код_товара': pandas.Series(Product_code),
    #     'Название_позиции': pandas.Series(Product_title) + " " + End_title,
    #     'Название_позиции_укр': pandas.Series(Product_title_ukr) + " " + End_title,
    #     'Поисковые_запросы': pandas.Series(""),
    #     'Поисковые_запросы_укр': pandas.Series(""),
    #     'Описание': pandas.Series(Product_description),
    #     'Описание_укр': pandas.Series(Product_description_ukr),
    #     'Тип_товара': pandas.Series(Product_Item_type),
    #     'Цена': pandas.Series(Product_price),
    #     'Валюта': pandas.Series(Product_currencyId),
    #     'Единица_измерения': pandas.Series(Product_Unit_measurement),
    #     'Минимальный_объем_заказа': pandas.Series(""),
    #     'Оптовая_цена': pandas.Series(""),
    #     'Минимальный_заказ_опт': pandas.Series(""),
    #     'Ссылка_изображения': pandas.Series(Product_pictures),
    #     'Наличие': pandas.Series(Product_availability),
    #     'Номер_группы': pandas.Series(""),
    #     'Название_группы': pandas.Series(""),
    #     'Адрес_подраздела': pandas.Series(""),
    #     'Возможность_поставки': pandas.Series(""),
    #     'Срок_поставки': pandas.Series(""),
    #     'Способ_упаковки': pandas.Series(""),
    #     'Способ_упаковки_укр': pandas.Series(""),
    #     'Уникальный_идентификатор': pandas.Series(Product_IP_item),
    #     'Идентификатор_товара': pandas.Series(Product_IP_item),
    #     'Идентификатор_подраздела': pandas.Series(""),
    #     'Идентификатор_группы': pandas.Series(""),
    #     'Производитель': pandas.Series(Product_vendor),
    #     'Страна_производитель': pandas.Series(Product_country_of_origin),
    #     'Скидка': pandas.Series(""),
    #     'ID_группы_разновидностей': pandas.Series(""),
    #     'Личные_заметки': pandas.Series(Product_Note) + " " + Note,
    #     'Продукт_на_сайте': pandas.Series(""),
    #     'Cрок действия скидки от': pandas.Series(""),
    #     'Cрок действия скидки до': pandas.Series(""),
    #     'Цена от': pandas.Series(""),
    #     'Ярлык': pandas.Series(""),
    #     'HTML_заголовок': pandas.Series(""),
    #     'HTML_заголовок_укр': pandas.Series(""),
    #     'HTML_описание': pandas.Series(""),
    #     'HTML_описание_укр': pandas.Series(""),
    #     'HTML_ключевые_слова': pandas.Series(""),
    #     'HTML_ключевые_слова_укр': pandas.Series(""),
    #     'Вес,кг': pandas.Series(""),
    #     'Ширина,см': pandas.Series(""),
    #     'Высота,см': pandas.Series(""),
    #     'Длина,см': pandas.Series(""),
    #     'Где_находится_товар': pandas.Series(""),
    #     'Код_маркировки_(GTIN)': pandas.Series(""),
    #     'Номер_устройства_(MPN)': pandas.Series(""),
    #     'Название_Характеристики': pandas.Series(""),
    #     'Измерение_Характеристики': pandas.Series(""),
    #     'Значение_Характеристики': pandas.Series("")
    #     }
    #data_frame_w = pandas.DataFrame(input)
    #data_frame_w.loc[(data_frame_w.Наличие == "true"), 'Наличие'] = "+"  # Pandas замена всех значений в таблице.
    #data_frame_w.loc[(data_frame_w.Наличие == "false"), 'Наличие'] = "-"
    #
    #exel_file_W = 'data/docs/' + "Test_title" + '.xlsx'
    #exel_file_R = 'data/docs/' + "Test_crm" + '.xlsx'
    #file_excep_R = 'data/exceptions.txt'
    #
    #data_frame_w.to_excel(exel_file_W, index=False)
    #data_frame_w = pandas.read_excel(exel_file_W)
    #data_frame_r = pandas.read_excel(exel_file_R)

    print(f"\n{Fore.RED}Time: {float(elapsed_time)}")
    # как итог паринг данный сейчас занимет 1.6 минуты/сек (нужна оптимизация numpy)

