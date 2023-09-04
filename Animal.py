class Animal:
    def __init__(self, nick_name, price, power, type):
        if price <= 0:
            raise ValueError()
        if not 0 < power <= 100:
            raise ValueError()
        self.nick_name = nick_name
        self.price = float(price)
        self.__power = float(power)
        self.type = type

    def __repr__(self):
        return "Name: " + str(self.nick_name) + ", Price: " + str(float(self.price)) + " NIS, Power: " + str(
            float(self.__power))

    def _get__power(self):
        return self.__power

    def _set__power(self, new_power):
        if 0 < new_power <= 100:
            self.__power = float(new_power)
            return self.__power
        return self.__power

    def win(self):
        return self.nick_name + " winner"

    def loss(self):
        return self.nick_name + " loser"

    def __ge__(self, other):
        if not isinstance(other, Animal):
            return False

        if self.__power >= other.__power:
            return True
        else:
            return False

    def __eq__(self, other):
        if not isinstance(other, Animal):
            return False

        if self.nick_name == other.nick_name:
            return True
        else:
            return False

    def get_type(self):
        return self.type
