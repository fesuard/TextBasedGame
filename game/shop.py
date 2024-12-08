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
            print(f'Not enough gold {total_cost}/{player.gold}')

        elif self.inventory.item_units[item.name] < quantity:
            print(f'Not enough inventory{self.inventory.item_units[item.name]}/{quantity}')

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
                    quantity_choice = 0

                    if item_choice in range(1, len_items + len_armor + 1):
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
                        self.player.inventory.display_player_inventory()

                    # shop exit
                    elif item_choice == 0:
                        valid_choice = True

                except ValueError:
                    print('Invalid input, please input a number corresponding to one one of the shop items')


