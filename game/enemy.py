from abc import ABC, abstractmethod
from game.ability import GoblinAttack, Slash, Maim


class Enemy(ABC):
    def __init__(self, name, total_hp):
        self.name = name
        self.total_hp = total_hp
        self.current_hp = total_hp
        self.abilities = []
        self.xp_for_player = 0

    @abstractmethod
    def __str__(self):
        pass


class Goblin(Enemy):
    def __init__(self):
        super().__init__('goblin', 250)
        self.xp_for_player = 100
        normal_attack, slash, maim = GoblinAttack(), Slash(), Maim()
        self.abilities.extend([normal_attack, slash, maim])

    def get_ability(self):
        if self.abilities[2].current_cd == 0:
            return self.abilities[2]

        if self.abilities[1].current_cd == 0:
            return self.abilities[1]

        return self.abilities[0]

    def __str__(self):
        return 'Fearsome Goblin'