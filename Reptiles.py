from hw5.Animal import Animal


class Reptiles(Animal):
    def __init__(self, nick_name, price, power, type="Reptiles"):
        Animal.__init__(self, nick_name, price, power, type)

    def move(self):
        self.power = self.power / 2

    def __ge__(self, other):
        if type(other) != Animal:
            return False

        if self.type == "Reptiles" and other.type == "Reptiles":
            self.move()
            other.move()
            return self >= other
        else:
            return self.power() >= other.__power()
