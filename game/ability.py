from abc import ABC, abstractmethod


class Ability(ABC):
    def __init__(self):
        self.total_cd = 0
        self.current_cd = 0
        self.type = 'damage'
        self.amount = 0

    @abstractmethod
    def __str__(self):
        pass


class MageAttack(Ability):
    def __init__(self):
        super().__init__()
        self.amount = 23

    def level_up(self):
        self.amount += self.amount * 0.15

    def __str__(self):
        return "Basic Attack"


class Frostbolt(Ability):
    def __init__(self):
        super().__init__()
        self.total_cd = 3
        self.current_cd = 0
        self.amount = 30

    def level_up(self):
        self.amount += self.amount * 0.15

    def __str__(self):
        return "Frostbolt"


class Firebolt(Ability):
    def __init__(self):
        super().__init__()
        self.total_cd = 5
        self.current_cd = 0
        self.amount = 35

    def level_up(self):
        self.amount += self.amount * 0.15

    def __str__(self):
        return "Firebolt"


class Meteor(Ability):
    def __init__(self):
        super().__init__()
        self.total_cd = 7
        self.current_cd = 0
        self.amount = 50

    def level_up(self):
        pass

    def __str__(self):
        return "Meteor"


class GoblinAttack(Ability):
    def __init__(self):
        super().__init__()
        self.total_cd = 0
        self.current_cd = 0
        self.amount = 2

    def __str__(self):
        return "Basic Attack"


class Slash(Ability):
    def __init__(self):
        super().__init__()
        self.total_cd = 3
        self.current_cd = 0
        self.amount = 3

    def __str__(self):
        return "Slash"


class Maim(Ability):
    def __init__(self):
        super().__init__()
        self.total_cd = 5
        self.current_cd = 0
        self.amount = 5

    def __str__(self):
        return "Maim"