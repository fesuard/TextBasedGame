

class Battle:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
        self.menu = (f'      THE BATTLE HAS STARTED\n'
                f'    YOU ARE FIGHTING AGAINST THE FEARSOME {self.enemy.name}\n'
                     f'\n To use an ability press:\n'
                     f'{self.player.show_abilities()}')

    def start(self):
        while self.player.current_hp > 0 and self.enemy.current_hp > 0:
            print(self.menu)
            break

