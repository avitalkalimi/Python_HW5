#This is an abstract class. Talking about a general Animal.

class Animal:
    #The animal constructor, produces a new animal according to the parameters it receives
    #It must accept all parameters, and it has conditions
    def __init__(self, nick_name, price, power, type):
        if price <= 0:
            raise ValueError()
        if not 0 < power <= 100:
            raise ValueError()
        self.nick_name = nick_name
        self.price = float(price)
        self.__power = float(power)
        self.type = type

    #The printing method that works when printing the animal
    def __repr__(self):
        return "Name: " + str(self.nick_name) + ", Price: " + str(float(self.price)) + " NIS, Power: " + str(
            float(self.__power))

    #method that returns what the animal's power is
    def _get__power(self):
        return self.__power

    #method that updates a new power for the animal. manage according to the access permissions!
    def _set__power(self, new_power):
        if 0 < new_power <= 100:
            self.__power = float(new_power)
            return self.__power
        return self.__power

    #method that announces the victory of the animal
    def win(self):
        return self.nick_name + " winner"

    #method that announces the loss of the animal
    def loss(self):
        return self.nick_name + " loser"
    
    #comparison method that checks for greater than or equal to
    def __ge__(self, other):
        if not isinstance(other, Animal):
            return False

        if self.__power >= other.__power:
            return True
        else:
            return False

    #comparison method that tests equality
    def __eq__(self, other):
        if not isinstance(other, Animal):
            return False

        if self.nick_name == other.nick_name:
            return True
        else:
            return False

    #method that returns the type of the animal
    def get_type(self):
        return self.type
