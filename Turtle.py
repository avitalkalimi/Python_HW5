from hw5.Reptiles import Reptiles

class Turtle(Reptiles):
    def __init__(self, nick_name, price, power, type="Turtle"):
        Reptiles.__init__(self, nick_name, price, power, type="Turtle")

    def loss(self):
        return self.nick_name + " loser I always lose"


