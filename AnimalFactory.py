from hw5.Cat import Cat
from hw5.Dog import Dog
from hw5.Parrot import Parrot
from hw5.Reptiles import Reptiles
from hw5.Snake import Snake
from hw5.Turtle import Turtle


class AnimalFactory(object):

    @staticmethod
    def create(type_animal, nick_name, price, power):
        if type_animal == "Dog":
            print("Dog created")
            return Dog(nick_name, price, power)
        if type_animal == "Cat":
            print("Cat created")
            return Cat(nick_name, price, power)
        if type_animal == "Turtle":
            print("Turtle created")
            return Turtle(nick_name, price, power)
        if type_animal == "Snake":
            print("Snake created")
            return Snake(nick_name, price, power)
        if type_animal == "Parrot":
            print("Parrot created")
            return Parrot(nick_name, price, power)
        if type_animal == "Reptiles":
            print("Reptiles created")
            return Reptiles(nick_name, price, power)
        else:
            print("wrong type ")



