# Замер времени
import time

import numpy
import pandas
from bs4 import BeautifulSoup
import requests

# Цвета для вывода в консоль
from colorama import init, Fore

from sys import argv
from functions import push_github_pages

class Arguments:
    _intro = argv
    _End_title = argv
    _y = argv
    _z = argv
    _n = argv
    _Note = argv
    _crm = argv
    def __init__(self):
        super().__init__()
        self._intro = argv
        self._End_title = argv
        self._y = argv
        self._z = argv
        self._n = argv
        self._Note = argv
        self._crm = argv
    def Show_Argv(self):
        print("База = ",self._intro)
        print("Название_позиции = ",self._End_title)
        print("y =  ",self._y)
        print("z = ",self._z)
        print("n = ",self._n)
        print("Личные_заметки = ",self._Note)
        print("crm_data = ",self._crm)
    def Push(self):
        return push_github_pages()
    def Show_Push(self):
        print('https://web-shark.github.io/promxls.github.io/'  + str(self._End_title) + '.xlsx')
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
        super().__init__()
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
class Exel(Parse,Arguments):
    def __init__(self):
        super().__init__()

        self.input = \
            {
            'Код_товара': pandas.Series(self._Product_code,dtype='object'),
            'Название_позиции': pandas.Series(self._Product_title,dtype='object') + " " + str(self._End_title),
            'Название_позиции_укр': pandas.Series(self._Product_title_ukr,dtype='object') + " " + str(self._End_title),
            'Поисковые_запросы': pandas.Series(""),
            'Поисковые_запросы_укр': pandas.Series(""),
            'Описание': pandas.Series(self._Product_description,dtype='object'),
            'Описание_укр': pandas.Series(self._Product_description_ukr,dtype='object'),
            'Тип_товара': pandas.Series(self._Product_Item_type,dtype='object'),
            'Цена': pandas.Series(self._Product_price,dtype='object'),
            'Валюта': pandas.Series(self._Product_currencyId,dtype='object'),
            'Единица_измерения': pandas.Series(self._Product_Unit_measurement,dtype='object'),
            'Минимальный_объем_заказа': pandas.Series(""),
            'Оптовая_цена': pandas.Series(""),
            'Минимальный_заказ_опт': pandas.Series(""),
            'Ссылка_изображения': pandas.Series(self._Product_pictures,dtype='object'),
            'Наличие': pandas.Series(self._Product_availability,dtype='object'),
            'Номер_группы': pandas.Series(""),
            'Название_группы': pandas.Series(""),
            'Адрес_подраздела': pandas.Series(""),
            'Возможность_поставки': pandas.Series(""),
            'Срок_поставки': pandas.Series(""),
            'Способ_упаковки': pandas.Series(""),
            'Способ_упаковки_укр': pandas.Series(""),
            'Уникальный_идентификатор': pandas.Series(self._Product_IP_item,dtype='object'),
            'Идентификатор_товара': pandas.Series(self._Product_IP_item,dtype='object'),
            'Идентификатор_подраздела': pandas.Series(""),
            'Идентификатор_группы': pandas.Series(""),
            'Производитель': pandas.Series(self._Product_vendor,dtype='object'),
            'Страна_производитель': pandas.Series(self._Product_country_of_origin,dtype='object'),
            'Скидка': pandas.Series(""),
            'ID_группы_разновидностей': pandas.Series(""),
            'Личные_заметки': pandas.Series(self._Product_Note,dtype='object') + " " + str(self._Note),
            'Продукт_на_сайте': pandas.Series(""),
            'Cрок действия скидки от': pandas.Series(""),
            'Cрок действия скидки до': pandas.Series(""),
            'Цена от': pandas.Series(""),
            'Ярлык': pandas.Series(""),
            'HTML_заголовок': pandas.Series(""),
            'HTML_заголовок_укр': pandas.Series(""),
            'HTML_описание': pandas.Series(""),
            'HTML_описание_укр': pandas.Series(""),
            'HTML_ключевые_слова': pandas.Series(""),
            'HTML_ключевые_слова_укр': pandas.Series(""),
            'Вес,кг': pandas.Series(""),
            'Ширина,см': pandas.Series(""),
            'Высота,см': pandas.Series(""),
            'Длина,см': pandas.Series(""),
            'Где_находится_товар': pandas.Series(""),
            'Код_маркировки_(GTIN)': pandas.Series(""),
            'Номер_устройства_(MPN)': pandas.Series(""),
            'Название_Характеристики': pandas.Series(""),
            'Измерение_Характеристики': pandas.Series(""),
            'Значение_Характеристики': pandas.Series("")
            }
        self._EXEL_pars = 'data/docs/' + str(self._End_title) + '.xlsx'
        self._EXEL_crm = 'data/docs/' + str(self._crm) + '.xlsx'
        self._Exceptions = "data/exceptions.txt"
        self._Product_except = []
    def Set_EXEL_pars(self,file_name:str):
        self._EXEL_pars = file_name
        print(f"{Fore.RED}New Exel file: {self._EXEL_pars}")
    def Set_Exceptions(self,file_name:str):
        self._Exceptions = file_name
        print(f"{Fore.RED}New Exel file: {self._Exceptions}")
    def Show_File(self):
        print(f"\n{Fore.BLUE}Exel: {self._EXEL_pars}"
              f"\nException: {self._Exceptions}")
    def Exept(self):
        with open(self._Exceptions) as file:
            for line in file:
                self._Product_except.append(line.replace('\n', ''))
    def Show_Exept(self):
        print(f"\n{Fore.MAGENTA}Product_except = {self._Product_except}")
    def Create_table(self):
        data_frame_w = pandas.DataFrame(self.input)
        data_frame_w.loc[(data_frame_w.Наличие == "true"), 'Наличие'] = "+"  # Pandas замена всех значений в таблице.
        data_frame_w.loc[(data_frame_w.Наличие == "false"), 'Наличие'] = "-"
        # Оператор "~" инвертирует булеву маску, т.е. меняет значения True на False и наоборот.
        data_frame_w = data_frame_w[~data_frame_w['Код_товара'].isin(self._Product_except)]
        data_frame_w.to_excel(self._EXEL_pars, index=False)
class Prise(Exel,Arguments):
    _Praise_new = []
    def Price_swap_new(self):
        print(f"\n{Fore.BLUE}Start new praise")
        data_frame_w = pandas.read_excel(self._EXEL_pars)
        data_frame_r = pandas.read_excel(self._EXEL_crm)
        self._Praise_new = numpy.zeros(len(data_frame_w), dtype=int)
        # создаем массив нулей, чтобы сохранять новые цены
        for i_iter, (t, row1) in enumerate(data_frame_w.iterrows()):
            conter_nets = 0
            finded = False
            cond = (data_frame_r['ID товара/услуги'] == str(row1['Код_товара'])) & \
                   (data_frame_r['Себестоимость'] > 0)
            matches = data_frame_r[cond]
            if len(matches) > 0:
                row2 = matches.iloc[0] # берем первое совпадение
                check_to_price = (int(row2['Себестоимость']) + int(self._y)) * float(self._z) + int(self._n)
                if (check_to_price - row1['Цена']) > 0:
                    to_price = check_to_price
                    finded = True
            if finded:
                self._Praise_new[i_iter] = int(to_price)
            else:
                self._Praise_new[i_iter] = int((int(row1['Цена']) + int(self._y)) * float(self._z) + int(self._n))
        data_frame_w['Цена'] = self._Praise_new
        data_frame_w.to_excel(self._EXEL_pars, index=False)
        print(f"{Fore.BLUE}End new praise")

if __name__ == '__main__':
    start_time = time.time()
    #_________________________________________# START
    init(autoreset=True)  # поддерживаться вывод на Windows 10.
    _Arguments = Arguments()
    _Arguments.Show_Argv()
    #_Arguments.Push()
    _URL = URL()
    _URL.Show_URL()
    _Requst = Request()
    _Product = Product()
    _Parse = Parse()
    #_Parse.Show_Parse()
    _Exel = Exel()
    #_Exel.Show_Exept()
    _Exel.Show_File()
    _Exel.Exept()
    _Exel.Create_table()
    _Prise = Prise()
    _Prise.Price_swap_new()
    _Arguments.Push()
    _Arguments.Show_Push()
    #_________________________________________# END
    end_time = time.time()
    elapsed_time = (end_time - start_time) / 60
    print(f"\n{Fore.RED}Time: {float(elapsed_time)}")
    # как итог паринг данный сейчас занимет 5 минуты/сек

