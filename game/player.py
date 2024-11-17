from abc import ABC, abstractmethod
from game.ability import MageAttack, Frostbolt, Firebolt, Meteor

class Player(ABC):
    def __init__(self, name):
        self.name = name
        self.current_xp = 0
        self.level = 1
        self.abilities = []
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
    def use_ability(self, ability):
        pass

    @abstractmethod
    def show_abilities(self):
        pass

    @abstractmethod
    def use_damage_item(self, item):
        pass

    @abstractmethod
    def use_buff_item(self, item):
        pass


class Mage(Player):
    def __init__(self, name):
        super().__init__(name)
        self.stats = {
            'max_hp': 80,
            'max_mana': 100,
            'max_xp': 100,
            'damage': 23,
            'total_armor': 10,
            'armor_class': 'Cloth',
            'death_scream': "Oh my, seems like I'm in a bit of a conundrum"
        }
        self.current_hp = 80
        self.current_mana = 100
        self.current_xp = 0
        normal_attack, frostbolt = MageAttack(), Frostbolt()
        self.abilities.extend([normal_attack, frostbolt])

    def level_up(self):
        self.level += 1
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
        self.current_mana = self.stats['max_mana']

    def use_ability(self, ability):
        if ability.effect is None:
            return ability.damage

    def show_abilities(self):
        abilities = []
        for i in range(len(self.abilities)):
            abilities.append(f'{i+1}. {self.abilities[i]}')
        return '\n'.join(abilities)

    def use_damage_item(self, item):
        return item.damage

    def use_buff_item(self, item):

        if item.increased_stat == 'hp':
            if item.value + self.current_hp >= self.stats['max_hp']:
                self.current_hp = self.stats['max_hp']
            else:
                self.current_hp += item.value

        if item.increased_stat == 'mana':
            if item.value + self.current_mana >= self.stats['max_mana']:
                self.current_mana = self.stats['max_mana']
            else:
                self.current_mana += item.value

    def death(self):
        print(self.stats['death_scream'])


class Warrior:
    pass




