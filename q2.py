class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        return f'I\'m a {self.name} , i am {self.age} years old and i am eating now'


class Dog(Animal):
    def __init__(self, name, age, like):
        super().__init__(name, age)
        self.like = like

    def eat(self):
        return super(Dog, self).eat() + f' and i like {self.like}'


a = Animal('Cat', '3')
print(a.eat())
b = Dog('tom', '5', 'money')
print(b.eat())
