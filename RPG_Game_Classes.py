__author__ = 'Austin'
from random import randint


class Monster():
    """Class for all enemies in the game"""
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
        self.dangerous = True

    def fight(self, target):
        """Controls the actual fighting between enemy and player"""
        damage = self.attack - target.defense
        if target.health - damage < 0:
            print(" The enemy hit you for {} damage".format(target.health))
            target.health = 0
        elif damage >= 0:
            target.health -= damage
            print(" The enemy hit you for {} damage".format(damage))
        else:
            print(" The enemy hit you for 0 damage")


class Player():
    """This is the player is stores the stats"""
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
        self.items = {}
        self.dangerous = True

    def fight(self, target):
        """Controls the actual fighting between player and enemy"""
        damage = self.attack - target.defense
        if target.health - damage < 0:
            print(" You hit the enemy for {} damage".format(target.health))
            target.health = 0
        elif damage >= 0:
            target.health -= damage
            print(" You hit the enemy for {} damage".format(damage))
        else:
            print(" You hit the enemy for 0 damage")


def main():
    """"Shout out to testing"""
    print("hi")


if __name__ == '__main__':
    main()