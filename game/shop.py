from game.item import Hppot, Mppot, Grenade, MageSet


class Shop:
    def __init__(self):
        shop_hp_pot, shop_mp_pot, shop_grenade = Hppot(), Mppot(), Grenade()
        item_list = [shop_hp_pot, shop_mp_pot, shop_grenade]

        for item in item_list:
            if str(item) != 'Grenade':
                item.units = 3
            else:
                item.units = 5

        mage_head_t2 = MageSet(body_part='head', item_name='T2 Mage Helm', defence=5, cost=10)
        mage_chest_t2 = MageSet(body_part='chest', item_name='T2 Mage Chest', defence=7, cost=20)
        mage_legs_t2 = MageSet(body_part='legs', item_name='T2 Mage Legs', defence=4, cost=8)
        mage_hands_t2 = MageSet(body_part='hands', item_name='T2 Mage Hands', defence=2, cost=6)

        self.catalogue = {
            'items': (shop_hp_pot, shop_mp_pot, shop_grenade),
            'mage_armor': (mage_head_t2, mage_chest_t2, mage_legs_t2, mage_hands_t2)
        }

    def buy_item(self, player, shop_item):
        player.inventory.append(shop_item)

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