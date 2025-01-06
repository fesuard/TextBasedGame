from game.inventory import Inventory
from game.item import mage_head_t2, mage_chest_t2, mage_legs_t2, mage_hands_t2, hp_pot, mp_pot, grenade


class Shop:
    def __init__(self, player):
        self.player = player
        self.inventory = Inventory()
        self.initialize_shop_inventory()


    def initialize_shop_inventory(self):
        item_list = [hp_pot, mp_pot, grenade]
        armor_set = [mage_head_t2, mage_chest_t2, mage_legs_t2, mage_hands_t2, ]

        for item in item_list:
            self.inventory.add_item(item, 4)

        for item in armor_set:
            self.inventory.add_item(item, 1)

    def sell_item(self, player, item, quantity):
        total_cost = item.cost * quantity

        if player.gold < total_cost:
            print(f'Not enough gold {player.gold}/{total_cost}')
            print('Press any key to continue')
            input('> ')

        elif self.inventory.item_units[item.name] < quantity:
            print(f'Not enough inventory{self.inventory.item_units[item.name]}/{quantity}')
            print('Press any key to continue')
            input('> ')

        else:
            print(f'You have bought {quantity} x {item.name} for {total_cost} gold')
            player.gold -= total_cost
            self.inventory.item_units[item.name] -= quantity
            self.player.inventory.add_item(item, quantity)

    def start_shop(self):
        while True:
            valid_choice = False
            while not valid_choice:
                try:
                    len_items = len(self.inventory.items)
                    len_armor = len(self.inventory.armor)
                    len_total = len_items + len_armor
                    self.inventory.display_shop_inventory()
                    item_choice = int(input('> '))

                    # checking if it's a valid choice overall
                    if item_choice in range(0, 10):

                        # checking if it's an item choice
                        if item_choice in range(len_total + 1):
                            print('How many?')
                            quantity_choice = int(input('> '))

                            # for usable items
                            if item_choice in range(1, len_items + 1):
                                shop_item = self.inventory.items[item_choice - 1]
                                self.sell_item(self.player, shop_item, quantity_choice)

                            # for armor
                            elif item_choice in range(len_items + 1, len_total + 1):
                                shop_item = self.inventory.armor[item_choice - len_items - 1]
                                self.sell_item(self.player, shop_item, quantity_choice)

                        # to go to player inventory
                        elif item_choice == 9:
                            valid_choice2 = False
                            while not valid_choice2:
                                try:
                                    self.player.inventory.display_player_inventory()
                                    print('\nIf you want to equip an armor piece, press 1\n')
                                    print('If you want to sell an item, press 2\n')
                                    print('If you want to return to the shop, press 0\n')
                                    print('Currently equipped items:\n')

                                    # displaying the currently equipped items
                                    self.player.display_player_current_equipped_items()
                                    inventory_choice = int(input('> '))

                                    # to equip/unequip armor
                                    if inventory_choice == 1:
                                        valid_choice3 = False
                                        while not valid_choice3:
                                            try:
                                                self.player.inventory.display_player_equipable_items()
                                                if self.player.inventory.armor:
                                                    armor_choice = int(input('> '))

                                                    if armor_choice in range(1, len(self.player.inventory.armor) + 1):
                                                        armor_piece = self.player.inventory.armor[armor_choice - 1]
                                                        body_part = armor_piece.body_part
                                                        removed_armor = self.player.equipment[body_part]

                                                        self.player.unequip_item(removed_armor)

                                                        self.player.equip_item(armor_piece)

                                                        valid_choice3 = True

                                                    else:
                                                        print('Please enter a valid input')

                                                else:
                                                    print('Press any key to continue')
                                                    input('> ')
                                                    valid_choice3 = True

                                            except ValueError:
                                                print('Please enter a valid input')

                                    # to sell items
                                    elif inventory_choice == 2:
                                        valid_choice4 = False
                                        while not valid_choice4:
                                            try:
                                                print('What do you want to sell?\n')
                                                print('To return to inventory, press 0\n')
                                                self.player.display_player_inventory()
                                                sell_choice = int(input('> '))
                                                sell_item = 0

                                                if sell_choice in range(1, len(self.player.inventory.items) + len(self.player.inventory.armor) + 1):
                                                    if sell_choice in range(1, len(self.player.inventory.items)):
                                                        sell_item = self.player.inventory.items[sell_choice - 1]
                                                    elif sell_choice in range(len(self.player.inventory.items), len(self.player.inventory.items) + len(self.player.inventory.armor) + 1):
                                                        sell_item = self.player.inventory.armor[sell_choice - len(self.player.inventory.items) - 1]
                                                    sell_price = sell_item.cost - (sell_item.cost * 0.25)
                                                    print(f'You will be selling the item for less than its worth\n'
                                                          f'Are you sure you want to sell {sell_item.name} for {sell_price}?\n'
                                                          f'Press y to confirm or n to return to your inventory\n')

                                                    # validation for sell_confirmation
                                                    while True:
                                                        sell_confirmation = input('> ').lower()
                                                        if sell_confirmation == 'y' or sell_confirmation == 'n':
                                                            break
                                                        else:
                                                            print('Please enter valid input')

                                                    if sell_confirmation == 'y':
                                                        pass





                                            except ValueError:
                                                print("Please enter valid input")

                                    elif inventory_choice == 0:
                                        valid_choice2 = True

                                except ValueError:
                                    print('Invalid input')

                        # shop exit
                        elif item_choice == 0:
                            valid_choice = True

                    else:
                        print('Invalid input, please input a number corresponding to one one of the shop items')

                except ValueError:
                    print('Invalid input, please input a number corresponding to one one of the shop items')


