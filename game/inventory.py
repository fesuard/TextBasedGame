class Inventory:
    def __init__(self):
        self.item_units = {}
        self.items = []

    def add_item(self, item, quantity):
        if item.name not in self.item_units:
            self.item_units[item.name] = quantity
        else:
            self.item_units[item.name] += quantity

        if item not in self.items:
            self.items.append(item)

    def remove_item(self, item, quantity):
        if item.name in self.items:
            self.items[item.name] -= quantity
            if self.items[item.name] <= 0:
                del self.items[item.name]
        else:
            print(f'{item.name} is not in the inventory.')

    def display_player_inventory(self):
        for item in self.items:
            if self.item_units[item.name] == 0:
                self.items.remove(item)

        if self.items:
            inventory = ['To use an item press:']

            for i in range(len(self.items)):
                inventory.append(f'{i+1}. {self.items[i]} - {self.item_units[self.items[i].name]} units remaining')

            return '\n'.join(inventory)

        else:
            return 'Inventory Empty!'