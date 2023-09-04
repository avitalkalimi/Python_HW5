from hw5.Reptiles import Reptiles

class Snake(Reptiles):
    def __init__(self, nick_name, price, power, type="Snake"):
        Reptiles.__init__(self, nick_name, price, power, type="Snake")

    def move(self):
        if self.power * 2.5 > 100:
            return self.power
        return self.power * 2.5




