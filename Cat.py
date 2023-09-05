#We will import the Mammal class, which inheritor the Animal class.
#we will use some of the methods that already exist in it, to avoid code duplication, because a Cat is a type of Mammal.
#Some of the methods will be overridden and implemented here according to the entity's need.
from hw5.Mammal import Mammal

class Cat(Mammal):
    #The Cat constructor, produces a new Cat according to the parameters it receives
    #It must accept all parameters, and it has conditions
    #For some of the parameters we will use the constructor of an Mammal.
    #unique features will be realized here
    def __init__(self, nick_name, price, power, type="Cat"):
        Mammal.__init__(self, nick_name, price, power, type="Cat")

    #This method overrides the speak method of mammals, and implements it according to the cat's voice
    def speak(self):
        return Mammal.speak(self) + " meow"


