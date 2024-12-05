from game.item import MageSet, WarriorSet


class Inventory:
    def __init__(self):
        self.item_units = {}
        self.items = []
        self.armor = []

    def add_item(self, item, quantity):
        # adding the items and the quantity in the dict
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

    def remove_item(self, item, quantity):
        if item.name in self.items:
            self.items[item.name] -= quantity
            if self.items[item.name] <= 0:
                del self.items[item.name]
        else:
            print(f'{item.name} is not in the inventory.')

    def display_player_usable_items(self):
        for item in self.items:
            if self.item_units[item.name] == 0:
                self.items.remove(item)

        if self.items:
            inventory = ['To use an item press:']

            for i in range(len(self.items)):
                inventory.append(f'{i+1}. {self.items[i]} - {self.item_units[self.items[i].name]} units remaining')

            return '\n'.join(inventory)

        else:
            return 'No usable items!'

    def display_shop_inventory(self):
        shop_print = [f'Welcome to KweZ Shop!\nI am your humble merchant KweZ\nPlease choose from the following:\n']
        shop_print.extend(['Items', 'Armor\n'.rjust(17)])
        shop_print.extend([f'1. {self.items[0].name}', f'2. {self.armor[0].name}\n'.rjust(24)])
        return ''.join(shop_print)

