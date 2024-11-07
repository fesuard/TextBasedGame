from abc import ABC, abstractmethod
from game.ability import GoblinAttack, Slash, Maim


class Enemy(ABC):
    def __init__(self, name, health, abilities):
        self.name = name
        self.health = health
        self.abilities = abilities


class Goblin(Enemy):
    def __init__(self):
        super().__init__('Goblin', 50, [])
        normal_attack, slash, maim = GoblinAttack(), Slash(), Maim()
        self.abilities.extend([normal_attack, slash, maim])