from abc import ABC, abstractmethod


class Item(ABC):
    def __init__(self, name):
        self.name = name
        self.type = ''

