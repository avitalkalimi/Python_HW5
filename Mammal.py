#We will import the Animal class.
#we will use some of the methods that already exist in it, to avoid code duplication, because a Mammal is a type of animal.
#Some of the methods will be overridden and implemented here according to the entity's need.
from hw5.Animal import Animal

#This is an abstract class. Talking about a general Mammal.
class Mammal(Animal):
    #The Mammal constructor, produces a new Mammal according to the parameters it receives
    #It must accept all parameters, and it has conditions
    #For some of the parameters we will use the constructor of an animal.
    #unique features will be realized here
    def __init__(self, nick_name, price, power, type):
        Animal.__init__(self, nick_name, price, power, type)

    #A method that declares a speaking mammal
    def speak(self):
        return self.nick_name + " says"


