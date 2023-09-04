import copy
from hw5.Animal import Animal


class Shop:
    def __init__(self, name, balance):
        self.name = name
        self.balance = float(balance)
        self.__animal_list = {}

    def get_name(self):
        return self.name

    def __add__(self, other):
        my_dict = {}
        if type(other) == list:
            animal_optinos = sorted(other, key=lambda i: i.price)
            count = 0
            for i in animal_optinos:
                if i.price <= self.balance:
                    self.balance -= i.price
                    count += 1
                    self.__animal_list[i.nick_name] = i
                else:
                    break
            return count
        if isinstance(other, Animal):
            if self.balance >= other.price:
                self.__animal_list[other.nick_name] = other
                self.balance -= other.price
                return 1
            return 0
        return 0

    def get__animals(self):
        return copy.deepcopy(self.__animal_list)

    def sell(self, nick_name):
        if nick_name in self.__animal_list.keys():
            the_nick_name = self.__animal_list[nick_name]
            self.balance += the_nick_name.price
            self.__animal_list.pop(nick_name)
            return the_nick_name
        return None

    def num_of_animals(self):
        return len(self.__animal_list)

    def play(self, animal_1, animal_2):
        if animal_1 not in self.__animal_list or animal_2 not in self.__animal_list:
            return False
        if self.__animal_list[animal_1] >= self.__animal_list[animal_2]:
            return self.__animal_list[animal_1].win() + "\n" + self.__animal_list[animal_2].loss()
        return self.__animal_list[animal_2].win() + "\n" + self.__animal_list[animal_1].loss()
