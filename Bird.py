from hw5.Animal import Animal


class Bird(Animal):
    def __init__(self, nick_name, price, power, type):
        Animal.__init__(self, nick_name, price, power, type)
        self.fly = False

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
