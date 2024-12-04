from game.item import mage_head_t2, mage_chest_t2, mage_legs_t2, mage_hands_t2, hp_pot, mp_pot, grenade


class Shop:
    def __init__(self):
        self.catalogue = {
            'items': (hp_pot, mp_pot, grenade),
            'mage_armor': (mage_head_t2, mage_chest_t2, mage_legs_t2, mage_hands_t2)
        }

    def sell_item(self, player, shop_item):
        player.inventory.add_item(shop_item)

    def start_shop(self):
        while True:
            print('Welcome to KweZ Shop!\nI am your humble merchant KweZ\nPlease choose from the following:\n')

            # Displaying the inventory
            print('Items', 'Armor'.rjust(17))
            print(f'1. {self.catalogue['items'][0]}', f'4. {self.catalogue['mage_armor'][0]}'.rjust(24))
            print(f'2. {self.catalogue['items'][1]}', f'5. {self.catalogue['mage_armor'][1]}'.rjust(25))
            print(f'3. {self.catalogue['items'][2]}', f'6. {self.catalogue['mage_armor'][2]}'.rjust(22))
            print(f'7. {self.catalogue['mage_armor'][3]}'.rjust(34))

            valid_choice = False
            while not valid_choice:
                try:
                    choice = int(input('> '))
                    if choice in range(1, 4):
                        if choice == 1:
                            if self.catalogue['items'][choice - 1].units > 0:
                                self.catalogue['items'][choice - 1].units -= 1


                except ValueError:
                    print('Invalid input, please input a number corresponding to one one of the shop items')