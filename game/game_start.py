from game.player import Mage, Warrior
from game.enemy import Goblin
from game.battle import Battle
from game.story import Story
from game.shop import Shop

class GameStart:
    def __init__(self):
        self.player = None
        self.story = Story()
        self.shop = Shop(self.player)

    def choose_class(self):
        valid_choice = False

        while not valid_choice:
            try:
                print("\nChoose a class: 1) Mage 2) Warrior")
                option = int(input("> "))

                if option in range(1, 3):
                    print("Name your character")
                    name = input("> ")

                    if option == 1:
                        self.player = Mage(name)

                    elif option == 2:
                        self.player = Warrior(name)

                    valid_choice = True

                else:
                    print("Invalid choice, please choose between the available classes")

            except ValueError:
                print("Invalid choice, please choose between the available classes")

        # initialize shop
        self.shop = Shop(self.player)

    def start_game(self):
        # starting the game, choosing the class
        self.story.get_chapter(0)
        self.choose_class()

        # battle 1
        battle1 = Battle(self.player, Goblin())
        battle1.start()

        # post battle 1
        self.story.get_chapter(1)
        self.shop.start_shop()
