from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional


# class Item(ABC):
#     def __init__(self):
#         self.name = ''
#         self.type = ''
#         self.amount = 0
#         self.cost = 0
#         self.effect = None
#
#     @abstractmethod
#     def __str__(self):
#         pass
#
#
# class Hppot(Item):
#     def __init__(self):
#         super().__init__()
#         self.name = 'HpPot'
#         self.type = 'support'
#         self.amount = 30
#         self.cost = 10
#         self.increased_stat = 'hp'
#
#     def __str__(self):
#         return 'HpPot'
#
#
# class Mppot(Item):
#     def __init__(self):
#         super().__init__()
#         self.name = 'MpPot'
#         self.type = 'support'
#         self.amount = 30
#         self.cost = 10
#         self.increased_stat = 'mp'
#
#     def __str__(self):
#         return 'MpPot'
#
#
# class Grenade(Item):
#     def __init__(self):
#         super().__init__()
#         self.name = 'Grenade'
#         self.type = 'damage'
#         self.effect = 'bleed'
#         self.dot_damage = 10
#         self.dot_duration = 3
#         self.total_dot_duration = 3
#         self.amount = 35
#         self.cost = 10
#
#     def __str__(self):
#         return 'Grenade'


# class MageSet:
#     def __init__(self, body_part, item_name, defence, cost):
#         self.body_part = body_part
#         self.item_name = item_name
#         self.defence = defence
#         self.cost = cost
#
#     def __str__(self):
#         return self.item_name

@dataclass
class MageSet:
    name: str
    body_part: str
    defence: int
    cost: int


mage_head_t1 = MageSet(name='T1 Mage Helm', body_part='head', defence=3, cost=5)
mage_chest_t1 = MageSet(name='T1 Mage Chest', body_part='chest', defence=5, cost=10)
mage_legs_t1 = MageSet(name='T1 Mage Legs', body_part='legs', defence=2, cost=4)
mage_hands_t1 = MageSet(name='T1 Mage Hands', body_part='hands', defence=1, cost=3)

mage_head_t2 = MageSet(name='T2 Mage Helm', body_part='head', defence=5, cost=10)
mage_chest_t2 = MageSet(name='T2 Mage Chest', body_part='chest', defence=7, cost=20)
mage_legs_t2 = MageSet(name='T2 Mage Legs', body_part='legs', defence=4, cost=8)
mage_hands_t2 = MageSet(name='T1 Mage Hands', body_part='hands', defence=2, cost=6)

@dataclass
class UsableItem:
    name: str
    type: str
    amount: int
    cost: int
    effect: Optional[str] = None
    increased_stat: Optional[str] = None
    dot_damage: Optional[int] = None
    dot_duration: Optional[int] = None
    total_dot_duration: Optional[int] = None


hp_pot = UsableItem(name='HpPot', type='support', increased_stat='hp', amount=30, cost=10)
mp_pot = UsableItem(name='MpPot', type='support', increased_stat='mp', amount=30, cost=10)
grenade = UsableItem(name='Grenade', type='damage', effect='bleed', dot_damage=10, dot_duration=3,
                     total_dot_duration=3, amount=30, cost=10)
