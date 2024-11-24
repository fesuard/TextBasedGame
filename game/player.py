from abc import ABC, abstractmethod
from game.ability import MageAttack, Frostbolt, Firebolt, Meteor
from game.item import Hppot, Grenade


class Player(ABC):
    def __init__(self, name):
        self.name = name
        self.current_xp = 0
        self.level = 1
        self.abilities = []
        self.inventory = []
        self.gold = 0
        self.equipment = {
            'head': 'empty',
            'chest': 'empty',
            'legs': 'empty',
            'hands': 'empty',
            'weapon': 'empty'
        }
        self.stats = {
            'max_hp': 0,
            'max_xp': 0,
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
    def show_abilities(self):
        pass

    @abstractmethod
    def show_inventory(self):
        pass

    @abstractmethod
    def use_buff_item(self, item):
        pass


class Mage(Player):
    def __init__(self, name):
        super().__init__(name)
        self.stats = {
            'max_hp': 80,
            'max_mp': 100,
            'max_xp': 100,
            'damage': 23,
            'total_armor': 10,
            'armor_class': 'Cloth',
            'death_scream': "Oh my, seems like I'm in a bit of a conundrum"
        }
        self.current_hp = 80
        self.current_mana = 100
        self.current_xp = 0
        self.gold = 50
        normal_attack, frostbolt = MageAttack(), Frostbolt()
        hp_pot, grenade = Hppot(), Grenade()
        self.abilities.extend([normal_attack, frostbolt])
        self.inventory.extend([hp_pot, grenade])

    def level_up(self):
        self.level += 1

        for ability in self.abilities:
            ability.level_up()

        if self.level == 2:
            self.stats['max_hp'] += self.stats['max_hp'] * 0.15
            self.stats['damage'] += self.stats['damage'] * 0.10
            self.stats['max_xp'] += self.stats['max_xp'] * 0.20

        if self.level == 3:
            self.stats['max_hp'] += self.stats['max_hp'] * 0.15
            self.stats['damage'] += self.stats['damage'] * 0.10
            self.stats['max_xp'] += self.stats['max_xp'] * 0.20
            firebolt = Firebolt()
            self.abilities.append(firebolt)

        if self.level == 4:
            self.stats['max_hp'] +=self.stats['max_hp'] * 0.15
            self.stats['damage'] += self.stats['damage'] * 0.10
            self.stats['max_xp'] += self.stats['max_xp'] * 0.20

        if self.level == 5:
            self.stats['max_hp'] += self.stats['max_hp'] * 0.15
            self.stats['damage'] += self.stats['damage'] * 0.10
            self.stats['max_xp'] += self.stats['max_xp'] * 0.20
            meteor = Meteor()
            self.abilities.append(meteor)

        self.current_hp = self.stats['max_hp']
        self.current_mana = self.stats['max_mp']

    def show_abilities(self):
        abilities = []
        for i in range(len(self.abilities)):
            abilities.append(f'{i+1}. {self.abilities[i]}')
        return '\n'.join(abilities)

    def show_inventory(self):
        items = ['To use an item press:']
        for i in range(len(self.inventory)):
            items.append(f'{i+1}. {self.inventory[i]} - {self.inventory[i].units} uses remaining')
        return '\n'.join(items)

    def use_buff_item(self, item):

        if item.increased_stat == 'hp':
            if item.amount + self.current_hp >= self.stats['max_hp']:
                self.current_hp = self.stats['max_hp']
            else:
                self.current_hp += item.amount

        if item.increased_stat == 'mana':
            if item.value + self.current_mana >= self.stats['max_mana']:
                self.current_mana = self.stats['max_mana']
            else:
                self.current_mana += item.value

    def death(self):
        print(self.stats['death_scream'])


class Warrior:
    pass




