class Pet:
    def __init__(self, n, a, c):
        self.name = n
        self.age = a
        self.color = c

    def show(self):
        print(f'{self.name} {self.age} {self.color}')


class Dog(Pet):

    def make_noise(self):
        print("bark")


class Cat(Pet):
    def make_noise(self):
        print("meow")


d = Dog("tom", 8, "white")
d.show()
d.make_noise()

c = Cat("jerry", 4, "yellow")
c.show()
c.make_noise()


#variables
#data types - int, float, str, boolean, list, tuple, set, dictionary
#loops and conditional statements - if else, while, for loop, range, break, continue
#pass
#functions - pass parameters, return keyword
#classes and objects - inheritance, self, _init__ method, method


#exception handling try except
#modules and packages
#in built modules - random, collections
# external python packages - selenium
# file reading and writing - csv

