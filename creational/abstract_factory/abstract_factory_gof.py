import random

#-- LEVEL 1


class SillySoldier():
    def action(self):
        print("SillySoldier in action")


class SillyMonster():
    def action(self):
        print("SillyMonster in action")


class SillySuperMonster():
    def action(self):
        print("SillySuperMonster in action")


#-- LEVEL 2

class BadSoldier():
    def action(self):
        print("BadSoldier in action")


class BadMonster():
    def action(self):
        print("BadMonster in action")


class BadSuperMonster():
    def action(self):
        print("BadSuperMonster in action")


class EasyLevelEnemyFactory:

    def create_soldier(self):
        return SillySoldier()

    def create_monster(self):
        return SillyMonster()

    def create_super_monster(self):
        return SillySuperMonster()


class DieHardLevelEnemyFactory:

    def create_soldier(self):
        return BadSoldier()

    def create_monster(self):
        return BadMonster()

    def create_super_monster(self):
        return BadSuperMonster()


class Game:

    def __init__(self):
        self.enemies = []

    def set_level(self, level):
        if level == 1:
            self.enemy_factory = EasyLevelEnemyFactory()
        elif level == 2:
            self.enemy_factory = DieHardLevelEnemyFactory()

    def play(self):
        enemies = []

        for i in range(10):
            rnd = random.randint(0, 2)

            if rnd == 0:
                enemies.append(self.enemy_factory.create_soldier())
            elif rnd == 1:
                enemies.append(self.enemy_factory.create_monster())
            else:
                enemies.append(self.enemy_factory.create_super_monster())


        for enemy in enemies:
            enemy.action()


if __name__ == '__main__':
    game = Game()

    game.set_level(1)
    game.play()

    print("-"*60)

    game.set_level(2)
    game.play()

