

class Battle:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
        self.menu = (f'\n    YOU ARE FIGHTING AGAINST THE FEARSOME {self.enemy}\n'
                     f'\n To use an ability press:\n'
                     f'{self.player.show_abilities()}\n'
                     f'0. To go to your inventory\n')

        self.used_enemy_abilities = []
        self.used_player_abilities = []
        self.enemy_dots = []
        self.player_dots = []
        self.outcome = ''

    def show_progress_bar(self, bar_length, total_stat, current_stat):
        hp_ratio = current_stat / total_stat
        filled_length = int(bar_length * hp_ratio)

        bar = '#' * filled_length + '-' * (bar_length - filled_length)
        return f'[{bar}] {current_stat} / {total_stat} HP'

    def use_damage_item(self, item):
        if item.effect:
            item.dot_duration = item.total_dot_duration
            if item not in self.player_dots:
                self.player_dots.append(item)
        self.enemy.current_hp -= item.amount

    def use_support_item(self, item):
        if str(item) == 'HpPot':
            self.player.current_hp = min(self.player.stats['max_hp'], self.player.current_hp + item.amount)

        if str(item) == 'MpPot':
            self.player.current_mana = min(self.player.stats['max_mp'], self.player.current_hp + item.amount)

    def start(self):
        print('THE BATTLE HAS STARTED !')
        print(f'{self.enemy} {self.show_progress_bar(25, self.enemy.total_hp, self.enemy.current_hp)}')
        print('\n\n')
        print(f'Your HP {self.show_progress_bar(25, self.player.stats['max_hp'], self.player.current_hp)}')
        print(f'Your MP {self.show_progress_bar(25, self.player.stats['max_mp'], self.player.current_mana)}')
        while self.player.current_hp > 0 and self.enemy.current_hp > 0:
            # Player round:

            # Cooldown management
            if self.used_player_abilities:
                for ability in self.used_player_abilities:
                    if ability.total_cd > 0:
                        if ability.current_cd > 0:
                            ability.current_cd -= 1
                            if ability.current_cd == 0:
                                print(f'{ability} just went off cooldown')
                            else:
                                print(f'PLAYER ABILITY {ability} CD IS: {ability.current_cd}')

            # Player dot management
            if self.player_dots:
                for dot in self.player_dots:
                    if dot.dot_duration > 0:
                        dot.dot_duration -= 1
                        self.enemy.current_hp -= dot.dot_damage
                        print(f"You hit {self.enemy} with {dot.dot_damage} dot damage")

            # Ability choice
            valid_choice = False
            while not valid_choice:
                try:
                    print(self.menu)
                    choice = int(input('> '))
                    if choice in range(1, len(self.player.abilities) + 1):
                        player_ability = self.player.abilities[choice - 1]
                        if player_ability not in self.used_player_abilities:
                            self.used_player_abilities.append(player_ability)

                        if player_ability.current_cd > 0:
                            print(f"Can't use {player_ability}\n"
                                  f"Remaining cooldown: {player_ability.current_cd}")

                        elif player_ability.mana_cost > self.player.current_mana:
                            print('Not enough mana')

                        else:
                            if player_ability.type == 'dot':
                                player_ability.dot_duration = player_ability.total_dot_duration
                                print(f'You have applied a {player_ability.effect} on {self.enemy}')
                                if player_ability not in self.player_dots:
                                    self.player_dots.append(player_ability)

                            if self.player.current_mana - player_ability.mana_cost > 0:
                                self.player.current_mana -= player_ability.mana_cost
                            else:
                                self.player.current_mana = 0

                            self.enemy.current_hp -= player_ability.amount
                            player_ability.current_cd = player_ability.total_cd

                            valid_choice = True

                    # Inventory choice
                    elif choice == 0:
                        valid_choice1 = False
                        while not valid_choice1:
                            try:
                                self.player.inventory.display_player_usable_items()
                                print("0. Go back to abilities")
                                choice1 = int(input('> '))

                                # choosing between usable items
                                if choice1 in range(1, len(self.player.inventory.items) + 1):
                                    player_item = self.player.inventory.items[choice1 - 1]
                                    if self.player.inventory.item_units[player_item.name] < 1:
                                        print(f'You are out of uses for {player_item}')
                                    else:
                                        if player_item.type == 'damage':
                                            self.use_damage_item(player_item)
                                            if player_item.effect:
                                                print(f'You have applied {player_item.effect} on {self.enemy}')
                                        elif player_item.type == 'support':
                                            self.use_support_item(player_item)
                                            print(f'{player_item.increased_stat} + {player_item.amount}')

                                        self.player.inventory.item_units[player_item.name] -= 1

                                        valid_choice1 = True
                                        valid_choice = True

                                # return to ability menu
                                elif choice1 == 0:
                                    valid_choice1 = True

                                else:
                                    print("Invalid choice, please chose between the available number of items")

                            except ValueError:
                                print("Invalid input, please input a number corresponding to one of your items.")

                    else:
                        print(f"No ability found with this input: {choice}, try again")

                except ValueError:
                    print("Invalid input, please input a number corresponding to one of your abilities.")

            if self.enemy.current_hp > 0:
                print(f'{self.enemy} {self.show_progress_bar(25, self.enemy.total_hp, self.enemy.current_hp)}')
                print('\n\n')

            # if enemy hp is below or equal to 0, we skip his turn and go to the winning scenario
            else:
                break

            # Enemy round:

            # Cooldown management
            if self.used_enemy_abilities:
                for ability in self.used_enemy_abilities:
                    if ability.total_cd > 0:
                        if ability.current_cd > 0:
                            ability.current_cd -= 1
                            print(f' ENEMY ABILITY {ability} CD IS: {ability.current_cd}')

            # Enemy dot management
            if self.enemy_dots:
                for dot in self.enemy_dots:
                    if dot.dot_duration > 0:
                        dot.dot_duration -= 1
                        self.player.current_hp -= dot.dot_damage
                        print(f"You got hit with {dot.dot_damage} dot damage")

            enemy_ability = self.enemy.get_ability()
            self.player.current_hp -= enemy_ability.amount
            if enemy_ability.type == 'dot':
                enemy_ability.dot_duration = enemy_ability.total_dot_duration
                if enemy_ability not in self.enemy_dots:
                    self.enemy_dots.append(enemy_ability)

            if enemy_ability not in self.used_enemy_abilities:
                self.used_enemy_abilities.append(enemy_ability)

            print(f'{self.enemy} USED {enemy_ability} for {enemy_ability.amount} damage')
            if enemy_ability.type == 'dot':
                print(f"{self.enemy} applied a {enemy_ability.effect} on you")
            enemy_ability.current_cd = enemy_ability.total_cd

            if self.player.current_hp > 0:
                print(f'Your HP {self.show_progress_bar(25, self.player.stats['max_hp'], self.player.current_hp)}')
                print(f'Your MP {self.show_progress_bar(25, self.player.stats['max_mp'], self.player.current_mana)}')

        # handling winning scenarios
        if self.enemy.current_hp <= 0:
            print(f'Congrats, you have slain the {self.enemy}\n')
            self.outcome = 'win'

            if self.enemy.xp_for_player + self.player.current_xp >= self.player.stats['max_xp']:
                leftover_xp = self.enemy.xp_for_player + self.player.current_xp - self.player.stats['max_xp']
                self.player.level_up()
                self.player.current_xp += leftover_xp
                print("YOU LEVELED UP")
                print(self.player.stats)
                print(self.player.current_xp, self.player.current_mana)

        # handling losing scenario
        elif self.player.current_hp <= 0:
            print(f"You've Lost to {self.enemy}")
            self.outcome = 'loss'
            input("Press any key to exit")








