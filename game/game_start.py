from game.player import Mage, Warrior
from game.enemy import Goblin
from game.battle import Battle
from game.story import Story
from game.shop import Shop

class GameStart:
    def __init__(self):
        self.player = None
        self.story = Story()
        self.shop = Shop()

    def choose_class(self):
        print("Choose a class: 1) Mage 2) Warrior")
        option = input("> ")
        print("Name your character")
        name = input("> ")

        if option == '1':
            self.player = Mage(name)
        elif option == '2':
            self.player = Warrior(name)
        else:
            print("Invalid choice, please choose between the available classes")
            self.choose_class()

    def start_game(self):
        self.story.get_chapter(0)
        self.choose_class()

        battle1 = Battle(self.player, Goblin())
        battle1.start()

