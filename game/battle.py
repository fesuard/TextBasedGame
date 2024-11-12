

class Battle:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
        self.menu = (f'    YOU ARE FIGHTING AGAINST THE FEARSOME {self.enemy.name}\n'
                     f'\n To use an ability press:\n'
                     f'{self.player.show_abilities()}')

    def show_hp_bar(self, bar_length, total_hp, current_hp):
        pass



    def start(self):
        print('THE BATTLE HAS STARTED !')
        while self.player.current_hp > 0 and self.enemy.current_hp > 0:
            print(self.menu)

            choice = int(input('> '))
            if choice in range(1, len(self.player.abilities) + 1):
                if choice == 1:
                    if self.player.abilities[0].type == 'damage':
                        self.enemy.current_hp -= self.player.abilities[0].amount

            print(self.enemy.current_hp)



