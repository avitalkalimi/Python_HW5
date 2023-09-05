#We will import the Animal class.
#we will use some of the methods that already exist in it, to avoid code duplication, because a bird is a type of animal.
#Some of the methods will be overridden and implemented here according to the entity's need.
#This is an abstract class. Talking about a general product.
from hw5.Animal import Animal


class Bird(Animal):
    #The Bird constructor, produces a new Bird according to the parameters it receives
    #It must accept all parameters, and it has conditions
    #For some of the parameters we will use the constructor of an animal.
    #unique features will be realized here
    def __init__(self, nick_name, price, power, type):
        Animal.__init__(self, nick_name, price, power, type)
        self.fly = False

    #comparison method for birds
     def __ge__(self, other):
         if not isinstance(other, Animal):
             return False
    
         if type(other) != Bird:
             if self.fly:
                 return True
             else:
                 return self >= other
    
         if not other.fly:
             return True
    
         return self >= other
