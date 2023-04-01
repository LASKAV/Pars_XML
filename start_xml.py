# Замер времени
import time
# Цвета для вывода в консоль
from colorama import init, Fore
from parse__classes.arguments_class import Arguments
from parse__classes.url_class import URL
from parse__classes.request_class import Request
from parse__classes.product_class import Product
from parse__classes.parse_class import Parse
from parse__classes.csv_class import Csv
from parse__classes.price_class import Price



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
    _Exel = Csv()
    #_Exel.Show_Exept()
    _Exel.Show_File()
    _Exel.Exept()
    _Exel.Create_table()
    _Prise = Price()
    _Prise.Price_swap_new()
    _Arguments.Push()
    _Arguments.Show_Push()
    #_________________________________________# END
    end_time = time.time()
    elapsed_time = (end_time - start_time) / 60
    print(f"\n{Fore.RED}Time: {float(elapsed_time)}")
    # как итог паринг данный сейчас занимет 4.6 минуты/сек

