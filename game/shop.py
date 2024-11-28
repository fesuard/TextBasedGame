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

        mage_head_t2 = MageSet(mage=self, body_part='head', item_name='T1 Mage Helm', defence=5, cost=10)
        mage_chest_t2 = MageSet(mage=self, body_part='chest', item_name='T1 Mage Chest', defence=7, cost=20)
        mage_legs_t2 = MageSet(mage=self, body_part='legs', item_name='T1 Mage Legs', defence=4, cost=8)
        mage_hands_t2 = MageSet(mage=self, body_part='hands', item_name='T1 Mage Hands', defence=2, cost=6)


        self.catalogue = {
            'items': None
        }