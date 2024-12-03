from abc import ABC, abstractmethod


class Item(ABC):
    def __init__(self):
        self.name = ''
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
        self.name = 'HpPot'
        self.type = 'support'
        self.units = 1
        self.amount = 30
        self.cost = 10
        self.increased_stat = 'hp'

    def __str__(self):
        return 'HpPot'


class Mppot(Item):
    def __init__(self):
        super().__init__()
        self.name = 'MpPot'
        self.type = 'support'
        self.units = 1
        self.amount = 30
        self.cost = 10
        self.increased_stat = 'mp'

    def __str__(self):
        return 'MpPot'


class Grenade(Item):
    def __init__(self):
        super().__init__()
        self.name = 'Grenade'
        self.type = 'damage'
        self.effect = 'bleed'
        self.dot_damage = 10
        self.dot_duration = 3
        self.total_dot_duration = 3
        self.units = 1
        self.amount = 35
        self.cost = 10

    def __str__(self):
        return 'Grenade'


class MageSet:
    def __init__(self, body_part, item_name, defence, cost):
        self.body_part = body_part
        self.item_name = item_name
        self.defence = defence
        self.cost = cost

    def __str__(self):
        return self.item_name

