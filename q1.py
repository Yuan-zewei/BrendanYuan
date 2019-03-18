class A:
    a = 'a'
    __b = 'b'

    @property
    def hello(self):
        return 'hello world'

    def set_b(self, a):
        self.__b = a

    @staticmethod
    def hello_world():
        return 'Hello'

    @property
    def get_b(self):
        return self.__b

    @classmethod
    def change(cls):
        cls.a = 'A'

a = A()
print(a.hello)
a.set_b('B')
print(a.get_b)
print(a.hello_world())
a.change()
print(A.a)
print(a.a)
b = A()
print(b.get_b)