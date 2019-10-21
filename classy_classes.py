# classy_classes

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def info(self):
        return '{}s age is {}'.format(self.name, self.age)
