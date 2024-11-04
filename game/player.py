from abc import ABC, abstractmethod

class Player(ABC):
    def __init__(self, name, player_class):
        self.name = name
        self.player_class = player_class
        self.xp = 0
        self.level = 1
        self.stats = {
            'hp': 0,
            'damage': 0,
            'total_armor': 0,
            'armor_class': '',
            'death_scream': ''
        }

    @abstractmethod
    def death(self):
        pass

    @abstractmethod
    def level_up(self):
        pass

    @abstractmethod
    def use_ability(self, ability):
        pass

    @abstractmethod
    def use_item(self, item):
        pass


class Mage(Player):
    def __init__(self, name):
        super().__init__(name, player_class='Mage')
        self.stats = {
            'hp': 80,
            'damage': 23,
            'total_armor': 10,
            'armor_class': 'Cloth',
            'death_scream': "Oh my, seems like I'm in a bit of a conundrum"
        }
        self.mana = 100
        self.abilities = {
            'frostbolt': 30
        }

    def death(self):
        print(self.stats['death_scream'])




