# 1. Create a empty class
#
class Emptyclass:
    pass

obj = Emptyclass()

# 2. Create a new simple class
class Dog:
    #Class Attribute
    type = "mammal"

    #Instance Attributes
    def __init__(self, callname):
        self.name = callname

    def speak(self):
        print(f"Bow Bow !, My name is {self.name}")


dog1 = Dog("tommy")
dog2 = Dog("fluffy")

#Access class attributes
print(dog1.__class__.type)

#Access instance attribute
print(dog1.name)

dog2.speak()



