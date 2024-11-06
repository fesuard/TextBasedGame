from game.player import Mage, Warrior
from game.enemy import Goblin
from game.battle import Battle
from game.story import Story

class GameStart:
    def __init__(self):
        self.player = None
        self.story = Story()

    def choose_class(self):
        print("Choose a class: 1) Mage 2) Warrior")
        option = input("> ")
        print("Name your character")
        name = input("> ")

        if option == '1':
            self.player = Mage(name)
        elif option == '2':
            self.player = Warrior(name)

    def start_game(self):
        self.story().chapter_0()
        self.choose_class()
        if self.player:
            self.story().chapter_1()
            battle = Battle(self.player, Goblin())
            battle.start()