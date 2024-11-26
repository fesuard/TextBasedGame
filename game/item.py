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
        self.total_dot_duration = 3
        self.units = 1
        self.amount = 35
        self.cost = 10

    def __str__(self):
        return 'Grenade'


class MageArmor:
    def __init__(self, player, body_part, name, defence):
        self.player = player
        self.body_part = body_part
        self.name = name
        self.defence = defence

    def equip(self):
        self.player.equipment[self.body_part] = self.name
        self.player.armor += self.defence

    def __str__(self):
        return self.name

