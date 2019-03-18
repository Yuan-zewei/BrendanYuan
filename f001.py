class A:
    __c = '类的属性'

    def __init__(self, a):
        self.a = a

    def set_c(self, b):
        self.__c = b

    @property
    def get_c(self):
        return self.__c


x = A('对象的属性')
x.set_c('新的类的属性')
print(x.get_c)