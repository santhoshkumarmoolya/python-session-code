# class is a blueprint
# object is an instance of the class
# methods are functions inside a class
class Dog:

    def __init__(self, n, a, c):
        self.name = n
        self.age = a
        self.color = c

    def eat(self):
        print("dog is eating")

    def make_noise(self):
        print("bark")


d = Dog("tom", 5, "black") # create an object of the class
d.make_noise()
print(d.name)
print(d.age)

d1 = Dog("jerry", 8, "grey")
d1.eat()
print(d1.name)
print(d1.age)







