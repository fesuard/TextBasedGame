class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item, quantity):
        if item.name not in self.items:
            self.items[item.name] = quantity
        else:
            self.items[item.name] += quantity

    def remove_item(self, item, quantity):
        if item.name in self.items:
            self.items[item.name] -= quantity
            if self.items[item.name] <= 0:
                del self.items[item.name]
        else:
            print(f'{item.name} is not in the inventory.')

    def display_player_inventory(self):
        if self.items:
            keys = [key for key in self.items.keys()]
            inventory = ['To use an item press:']

            for i in range(len(keys)):
                inventory.append(f'{i+1}. {keys[i]} - {self.items[keys[i]]} units remaining')

            return '\n'.join(inventory)

        else:
            return 'Inventory Empty!'