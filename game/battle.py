

class Battle:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
        self.menu = (f'    YOU ARE FIGHTING AGAINST THE FEARSOME {self.enemy}\n'
                     f'\n To use an ability press:\n'
                     f'{self.player.show_abilities()}')
        self.used_enemy_abilities = []

    def show_hp_bar(self, bar_length, total_hp, current_hp):
        hp_ratio = current_hp / total_hp
        filled_length = int(bar_length * hp_ratio)

        bar = '#' * filled_length + '-' * (bar_length - filled_length)
        return f'[{bar}] {current_hp} / {total_hp} HP'



    def start(self):
        print('THE BATTLE HAS STARTED !')
        print(f'{self.enemy} {self.show_hp_bar(25, self.enemy.total_hp, self.enemy.current_hp)}')
        print('\n\n')
        print(f'Your HP {self.show_hp_bar(25, self.player.stats['max_hp'], self.player.current_hp)}')
        while self.player.current_hp > 0 and self.enemy.current_hp > 0:
            print(self.menu)

            # Player round:
            while True:
                choice = int(input('> '))
                if choice in range(1, len(self.player.abilities) + 1):
                    if choice == 1:
                        if self.player.abilities[0].type == 'damage':
                            self.enemy.current_hp -= self.player.abilities[0].amount
                            break
                else:
                    print(f"No ability found with this input: {choice}, try again")

            if self.enemy.current_hp > 0:
                print(f'{self.enemy} {self.show_hp_bar(25, self.enemy.total_hp, self.enemy.current_hp)}')
                print('\n\n')

            # Enemy round:
            self.player.current_hp -= self.enemy.get_ability().amount

            if self.enemy.get_ability() not in self.used_enemy_abilities:
                self.used_enemy_abilities.append(self.enemy.get_ability())

            print(f'GOBLIN USED {self.enemy.get_ability()}')
            self.enemy.get_ability().current_cd = self.enemy.get_ability().total_cd

            for ability in self.used_enemy_abilities:
                if ability.total_cd:
                    if ability.current_cd > 0:
                        ability.current_cd -= 1
                        print(f'ABILITY {ability} CD IS: {ability.current_cd}')

            if self.player.current_hp > 0:
                print(f'Your HP {self.show_hp_bar(25, self.player.stats['max_hp'], self.player.current_hp)}')

        # handling winning scenarios
        if self.enemy.current_hp <= 0:
            print(f'Congrats, you have slain the {self.enemy}\n')
            if self.enemy.xp_for_player + self.player.current_xp >= self.player.stats['max_xp']:
                leftover_xp = self.enemy.xp_for_player + self.player.current_xp - self.player.stats['max_xp']
                self.player.level_up()
                self.player.current_xp += leftover_xp
                print("YOU LEVELED UP")





