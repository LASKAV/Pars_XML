from colorama import init, Fore
import pandas
import numpy

from parse__classes.csv_class import Csv
from parse__classes.arguments_class import Arguments
class Price(Csv,Arguments):
    _Praice_new = []
    def Price_swap_new(self):
        print(f"\n{Fore.BLUE}Start new praise")
        data_frame_w = pandas.read_csv(self._csv_pars)
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
        data_frame_w.to_csv(self._csv_pars, index=False)
        print(f"{Fore.BLUE}End new praise")