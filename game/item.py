from abc import ABC, abstractmethod


class Item(ABC):
    def __init__(self, name):
        self.name = name
        self.type = ''
        self.units = 0
        self.amount = 0
        self.cost = 0


    @abstractmethod
    def use_item(self):
        return


class Hppot(Item):
    def __init__(self, name):
        super().__init__(name)
        self.type = 'support'
        self.units = 1
        self.amount = 30
        self.cost = 10
        self.increased_stat = 'hp'


class Grenade(Item):
    def __init__(self, name):
        super().__init__(name)
        self.type = 'damage'
        self.effect = 'bleed'
        self.duration = 3
        self.dot_damage = 10
        self.units = 1
        self.amount = 35
        self.cost = 10


