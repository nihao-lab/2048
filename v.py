"""

"""
from c import C
class V:
    def __init__(self):
        self.c=C()
    def __show(self):
        for itme in self.c.map:
            for s in itme:
                print(s,end='\t')
            print()
    def __select(self):
        n=input('1键左移，2键右移，3键上移，4键下移:')
        if n=='1':
            self.c.left()
        elif n=='2':
            self.c.right()
        elif n=='3':
            self.c.up()
        elif n=='4':
            self.c.down()
    def main(self):
        while True:
            self.__show()
            self.__select()