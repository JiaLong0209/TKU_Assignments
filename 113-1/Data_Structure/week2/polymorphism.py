class Animal:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def say(self):
        print("Hello, world")
        

class Cat(Animal):
    def __init__(self, name, age, sound):
        super().__init__(name, age)
        self.sound = sound
    
    def say(self):
        print(self.sound)


class Dog(Animal):
    def __init__(self, name, age, sound):
        super().__init__(name, age)
        self.sound = sound
    
    def say(self):
        print(self.sound)


animals = [ Cat("c1", 10, "Nya"), Animal("a1", 0), Dog("D1", 100, "Boffu!"),]

for i in animals:
    i.say()


