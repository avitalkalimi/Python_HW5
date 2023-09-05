#We will import the Mammal class, which inheritor the Animal class.
#we will use some of the methods that already exist in it, to avoid code duplication, because a Dog is a type of Mammal.
#Some of the methods will be overridden and implemented here according to the entity's need.
from hw5.Mammal import Mammal


class Dog(Mammal):
    #The Dog constructor, produces a new Dog according to the parameters it receives
    #It must accept all parameters, and it has conditions
    #For some of the parameters we will use the constructor of an Mammal.
    #unique features will be realized here
    def __init__(self, nick_name, price, power, type="Dog"):
        Mammal.__init__(self, nick_name, price, power, type)

    #This method overrides the speak method of mammals, and implements it according to the Dog's voice
    def speak(self):
        return Mammal.speak(self) + " woof woof"

    #The victory declaration method uses an existing method of the department in addition to the method we inherited from the mammal department.
    def win(self):
        return self.speak(self) + " " + Mammal.win(self)


