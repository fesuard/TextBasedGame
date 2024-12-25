from game.item import MageSet, WarriorSet


class Inventory:
    def __init__(self):
        self.item_units = {}
        self.items = []
        self.armor = []

    def add_item(self, item, quantity):
        # adding the item names and the quantity in the dict
        if item.name not in self.item_units:
            self.item_units[item.name] = quantity
        else:
            self.item_units[item.name] += quantity

        # adding the objects in either items(for usable items) or armor(for the equipable/unequipable armor)
        if isinstance(item, (MageSet, WarriorSet)):
            if item not in self.armor:
                self.armor.append(item)
        else:
            if item not in self.items:
                self.items.append(item)

    # def remove_item(self, item, quantity):
    #     if item.name in self.items:
    #         self.items[item.name] -= quantity
    #         if self.items[item.name] <= 0:
    #             del self.items[item.name]
    #     else:
    #         print(f'{item.name} is not in the inventory.')

    def display_player_usable_items(self):
        for item in self.items:
            if self.item_units[item.name] == 0:
                self.items.remove(item)

        if self.items:
            item_inventory = ['To use an item press:']

            for i in range(len(self.items)):
                item_inventory.append(f'{i + 1}. {self.items[i].name} - {self.item_units[self.items[i].name]} units remaining')

            print('\n'.join(item_inventory))

        else:
            print('No usable items!')

    def display_player_equipable_items(self):
        for armor in self.armor:
            if self.item_units[armor.name] == 0:
                self.armor.remove(armor)

        if self.armor:
            armor_inventory = ['To equip an armor piece press:']

            for i in range(len(self.armor)):
                armor_inventory.append(f'{i + 1}. {self.armor[i].name} - {self.armor[i].defence} defence')

            print('\n'.join(armor_inventory))

        else:
            print('No armor in inventory')

    def display_player_inventory(self):
        # displaying usable items
        print('Usable Items')
        if self.items:
            for item in self.items:
                print(f'{item.name} - {self.item_units[item.name]}')
        else:
            print('No usable items')

        print('Armor')
        if self.armor:
            for i in range(len(self.armor)):
                print(f'{self.armor[i].name} - {self.item_units[self.armor[i].name]}')
        else:
            print('No armor\n')

    def display_shop_inventory(self):
        shop_print = [f'Welcome to KweZ Shop!\nI am your humble merchant KweZ\nPlease choose from the following:\n']
        shop_print.extend(['\nItems', 'Armor\n'.rjust(19)])
        shop_print.extend([f'1. {self.items[0].name} - {self.item_units[self.items[0].name]}',
                           f'4. {self.armor[0].name} - {self.item_units[self.armor[0].name]}\n'.rjust(26)])
        shop_print.extend([f'2. {self.items[1].name} - {self.item_units[self.items[1].name]}',
                           f'5. {self.armor[1].name} - {self.item_units[self.armor[1].name]}\n'.rjust(27)])
        shop_print.extend([f'3. {self.items[2].name} - {self.item_units[self.items[2].name]}',
                           f'6. {self.armor[2].name} - {self.item_units[self.armor[2].name]}\n'.rjust(24)])
        shop_print.append(f'7. {self.armor[3].name} - {self.item_units[self.armor[3].name]}\n\n'.rjust(40))
        shop_print.append('9. Go to your inventory\n')
        shop_print.append('0. EXIT shop\n')
        print(''.join(shop_print))
