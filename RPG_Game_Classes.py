__author__ = 'Austin'
from random import randint


class Monster():
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.attack = level + randint(0, level)
        self.defense = level + randint(0, level)
        self.health = level + randint(0, level)
        self.max_health = self.health
        self.speed = level + randint(0, level)
        self.exp = level + randint(0, level)
        self.gold = level + randint(0, level)

    def attack_player(self, target):
        damage = self.attack - target.defense
        if target.health - damage < 0:
            print(" The enemy hit you for {} damage".format(target.health))
            target.health = 0
        elif damage >= 0:
            target.health -= damage
            print(" The enemy hit you for {} damage".format(damage))


class Player():
    def __init__(self, name, level=1):
        self.name = name
        self.level = level
        self.attack = level + 1
        self.defense = level + 1
        self.health = level + 1
        self.max_health = self.health
        self.speed = level + 1
        self.exp = 0
        self.gold = 0
        self.max_exp = level

    def attack_enemy(self, target):
        damage = self.attack - target.defense
        if target.health - damage < 0:
            print(" You hit the enemy for {} damage".format(target.health))
            target.health = 0
        elif damage >= 0:
            target.health -= damage
            print(" You hit the enemy for {} damage".format(damage))
        '''elif damage < 0:
            print('attack=' + str(player.attack))
            print('enemy defense=' + str(enemy.defense))
            print('enemy level=' + str(enemy.level))
            print('player level=' + str(player.level))'''


def main():
    print("hi")


if __name__ == '__main__':
    main()