class Battle:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def start(self):
        print('YOLOOOOOOOOOOOOOOOOOOOOO')
        print(self.player.stats['death_scream'])
        print(self.enemy.attack())