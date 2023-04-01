from colorama import init, Fore
import pandas

from parse__classes.parse_class import Parse
from parse__classes.arguments_class import Arguments
class Csv(Parse,Arguments):
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
        self._csv_pars = 'data/docs/' + str(self._End_title) + '.csv'
        self._EXEL_crm = 'data/docs/' + str(self._crm) + '.xlsx'
        self._Exceptions = "data/exceptions.txt"
        self._Product_except = []
    def Set_csv_pars(self,file_name:str):
        self._EXEL_pars = file_name
        print(f"{Fore.RED}New Exel file: {self._EXEL_pars}")
    def Set_Exceptions(self,file_name:str):
        self._Exceptions = file_name
        print(f"{Fore.RED}New Exel file: {self._Exceptions}")
    def Show_File(self):
        print(f"\n{Fore.BLUE}Exel: {self._csv_pars}"
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
        data_frame_w.to_csv(self._csv_pars, index=False)