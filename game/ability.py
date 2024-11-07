from abc import ABC, abstractmethod


class Ability(ABC):
    def __init__(self):
        self.total_cd = 0
        self.current_cd = 0
        self.type = 'damage'
        self.amount = 0


class MageAttack(Ability):
    def __init__(self):
        super().__init__()
        self.amount = 23

    def level_up(self):
        self.amount += self.amount * 0.15


class Frostbolt(Ability):
    def __init__(self):
        super().__init__()
        self.total_cd = 3
        self.current_cd = 0
        self.amount = 30

    def level_up(self):
        self.amount += self.amount * 0.15


class Firebolt(Ability):
    def __init__(self):
        super().__init__()
        self.total_cd = 5
        self.current_cd = 0
        self.amount = 35

    def level_up(self):
        self.amount += self.amount * 0.15


class Meteor(Ability):
    def __init__(self):
        super().__init__()
        self.total_cd = 7
        self.current_cd = 0
        self.amount = 50

    def level_up(self):
        pass


class GoblinAttack(Ability):
    def __init__(self):
        super().__init__()
        self.total_cd = 0
        self.current_cd = 0
        self.amount = 2


class Slash(Ability):
    def __init__(self):
        super().__init__()
        self.total_cd = 3
        self.current_cd = 0
        self.amount = 3


class Maim(Ability):
    def __init__(self):
        super().__init__()
        self.total_cd = 5
        self.current_cd = 0
        self.amount = 5