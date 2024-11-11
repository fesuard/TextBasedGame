from abc import ABC, abstractmethod
from game.ability import GoblinAttack, Slash, Maim


class Enemy(ABC):
    def __init__(self, name, current_hp, abilities):
        self.name = name
        self.current_hp = current_hp
        self.abilities = []


class Goblin(Enemy):
    def __init__(self):
        super().__init__('Goblin', 50, [])
        normal_attack, slash, maim = GoblinAttack(), Slash(), Maim()
        self.abilities.extend([normal_attack, slash, maim])


    def attack(self):
        if self.abilities[0].amount:
            return self.abilities[0].amount