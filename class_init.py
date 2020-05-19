class Person:
    def __init__(self, name):
        self.name = name
    def sayHi(self):
        print('Дароу! Меня зовут', self.name)

p = Person('Swaroop')
p.sayHi()