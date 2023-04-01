from sys import argv
from functions import push_github_pages
class Arguments:
    _intro = argv
    _End_title = "End_title_new"
    _y = "40"
    _z = "1.17"
    _n = "300"
    _Note = "NOTE"
    _crm = "2702"
    def __init__(self):
        super().__init__()
        self._intro = argv
        self._End_title = "End_title"
        self._y = "40"
        self._z = "1.17"
        self._n = "300"
        self._Note = "NOTE"
        self._crm = "2702"
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


