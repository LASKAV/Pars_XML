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
    def Set_Url_ru(self,url_ru:str):
        self._url_ru = url_ru
    def Set_Url_ukr(self,url_ukr:str):
        self._url_ukr = url_ukr
    def Set_Url(self,url:str):
        self._url = url
    def Show_URL(self):

        print(f"\n{Fore.RED}URL_RU: {self._url_ru}"
              f"\nURL_UKR: {self._url_ukr}"
              f"\nURL: {self._url}")