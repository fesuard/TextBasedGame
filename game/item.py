from abc import ABC, abstractmethod


class Item(ABC):
    def __init__(self):
        self.type = ''
        self.units = 0
        self.amount = 0
        self.cost = 0
        self.effect = None

    @abstractmethod
    def __str__(self):
        pass


class Hppot(Item):
    def __init__(self):
        super().__init__()
        self.type = 'support'
        self.units = 1
        self.amount = 30
        self.cost = 10
        self.increased_stat = 'hp'

    def __str__(self):
        return 'HpPot'

class Grenade(Item):
    def __init__(self):
        super().__init__()
        self.type = 'damage'
        self.effect = 'bleed'
        self.dot_damage = 10
        self.dot_duration = 3
        self.units = 1
        self.amount = 35
        self.cost = 10

    def __str__(self):
        return 'Grenade'

