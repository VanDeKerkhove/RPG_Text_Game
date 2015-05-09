__author__ = 'Austin'
from random import randint
from math import trunc
import RPG_Game_Classes as Rpg_Classes

# TODO: GUI, get potion to work, actual levels, enemy level up, random events.
list_of_names = ["Evil Cat", " Sneaky Mouse", "Mad Rat", "Flying Hat", "Mean Bumblebee", "Slow Slug", "Slimy Snail",
                 "Traffic Cone", "Tall Walrus", "Wiggly Noodles", "Angry Waffle"]
LENGTH_OF_SCREEN = 40
game_state_outer = 2  # 1=fight, 2=main menu, 3=shop, 4=quit


def check_death():
    """Checks if anyone is dead is they are returns the string player or enemy if not returns the string none"""
    if player.health == 0:
        return "player"
    elif enemy.health == 0:
        return "enemy"
    return 'none'


def player_win():
    """Prints out a win screen(when the player defeats an enemy)"""
    spaces_in_between = LENGTH_OF_SCREEN - 2
    spaces_enemy = (spaces_in_between - 5) - len(enemy.name)
    exp = enemy.level
    gold = enemy.level
    spaces_exp_gold = LENGTH_OF_SCREEN - 25 - len(str(exp)) - len(str(gold))
    print("-" * LENGTH_OF_SCREEN)
    print("|" + " " * spaces_in_between + "|")
    print("|" + " " * spaces_in_between + "|")
    print("| You have defeated: " + " " * 18 + "|")
    print("|     " + enemy.name + " " * spaces_enemy + "|")
    print("|" + " " * spaces_in_between + "|")
    print("|     +" + str(exp) + " exp     +" + str(gold) + " gold" + " "*spaces_exp_gold + "  |")
    print("|" + " " * spaces_in_between + "|")
    print("| Press enter to return to main menu.. |")
    print("|" + " " * spaces_in_between + "|")
    print("-" * LENGTH_OF_SCREEN)
    input()


def enemy_win():
    """"Prints out a lose screen (when the player dies)"""
    spaces_in_between = LENGTH_OF_SCREEN - 2
    spaces_enemy = (spaces_in_between - 5) - len(enemy.name)
    print("")
    print("-" * LENGTH_OF_SCREEN)
    print("|" + " " * spaces_in_between + "|")
    print("|" + " " * spaces_in_between + "|")
    print("| You have been beaten by: " + " " * 12 + "|")
    print("|     " + enemy.name + " " * spaces_enemy + "|")
    print("|" + " " * spaces_in_between + "|")
    print("|" + " " * spaces_in_between + "|")
    print("|" + " " * spaces_in_between + "|")
    print("| Press enter to return to main menu.. |")
    print("|" + " " * spaces_in_between + "|")
    print("-" * LENGTH_OF_SCREEN)
    input()


def gain(exp, gold):
    """Used when the player gains experience points or gold. Also checks for a level-up and distributes stat points"""
    try:
        bonus = int(player.items['EXP hat'])
    except KeyError:
        bonus = 0
    player.exp += exp
    player.exp += bonus
    player.gold += gold
    if player.exp >= player.max_exp:
        print("")
        print('Level-UP!')
        player.attack += 1
        player.defense += 1
        player.max_health += 1
        player.exp -= player.max_exp
        player.max_exp *= 2
        player.level += 1


def get_stats():
    """Displays the stat screen for the player"""
    spaces_in_between = LENGTH_OF_SCREEN - 2
    spaces_level = 26 - len(str(player.level)) - len(str(player.exp)) - len(str(player.max_exp))
    spaces_attack = 29 - len(str(player.attack))
    spaces_defense = 28 - len(str(player.defense))
    spaces_health = 28 - len(str(player.health)) - len(str(player.max_health))
    spaces_gold = 31 - len(str(player.gold))
    print("")
    print("-" * LENGTH_OF_SCREEN)
    print("|" + " " * spaces_in_between + "|")
    print("| Player Name: " + player.name + " " * (24-len(player.name)) + "|")
    print("| Level: " + str(player.level) + "   " + str(player.exp) + "/" + str(player.max_exp) + " "*spaces_level+"|")
    print("| Attack: " + str(player.attack) + " " * spaces_attack + "|")
    print("| Defense: " + str(player.defense) + " " * spaces_defense + "|")
    print("| Health: " + str(player.health) + "/" + str(player.max_health) + " " * spaces_health + "|")
    print("| Gold: " + str(player.gold) + " " * spaces_gold + "|")
    print("|" + " " * spaces_in_between + "|")
    print("| Press enter to return to main menu.. |")
    print("-" * LENGTH_OF_SCREEN)
    input()


def attack(first):
    """Does the attacking in the game. first is who is attacking first. Checks for death. Switches game state if necessary.
       Rests player health if he wins and gains exp."""
    global game_state_outer
    if first is enemy:
        enemy.fight(player)
        if check_death() is 'player':
            enemy_win()
            game_state_outer = 2
            player.health = player.max_health
        elif check_death() is 'none':
            player.fight(enemy)
            if check_death() is 'enemy':
                player_win()  # Win Screen
                gain(enemy.level, enemy.level)  # EXP Gain
                game_state_outer = 2
                player.health = player.max_health  # Reset Health
            elif check_death() is 'player':
                enemy_win()
                game_state_outer = 2
                player.health = player.max_health
        elif check_death() is 'enemy':
            player_win()  # Win Screen
            gain(enemy.level, enemy.level)  # EXP Gain
            game_state_outer = 2
            player.health = player.max_health  # Reset Health
    elif first is player:
        player.fight(enemy)
        if check_death() is 'enemy':  # .                        Enemy dies
            player_win()  # Win Screen
            gain(enemy.level, enemy.level)  # EXP Gain
            game_state_outer = 2
            player.health = player.max_health  # Reset Health
        elif check_death() is 'none':  # .                        No one dies
            enemy.fight(player)
            if check_death() is 'player':  # .                             Player dies
                enemy_win()
                game_state_outer = 2
                player.health = player.max_health
            elif check_death() is "enemy":  # .                            Enemy dies
                player_win()  # Win Screen
                gain(enemy.level, enemy.level)  # EXP Gain
                game_state_outer = 2
                player.health = player.max_health  # Reset Health
        elif check_death() is 'player':  # .                      Player dies
            enemy_win()
            game_state_outer = 2
            player.health = player.max_health


def attack_main():
    """Determines who attacks first. Used to call the main attack()"""
    global game_state_outer
    if player.speed > enemy.speed:  # Player is faster
        attack(player)
    elif player.speed < enemy.speed:
        attack(enemy)
    else:
        x = randint(0, 1)
        if x == 0:
            attack(player)
        elif x == 1:
            attack(enemy)


def shop():
    """Controls the shop where the player buys items"""
    global game_state_outer
    options = {"?": "Type a number with a \"?\" after it for more info",
               "1?": "Restores health equal to your level",
               "2?": "Gives you +1 attack", "3?": "Gives you +1 defense",
               "4?": "Gives you +1 health", "5?": "Gives you +1 speed",
               "6?": "Gives you +1 EXP per win", "7?": "Exits the shop",
               "1": [8, "potion"], "2": [10, "sword"], "3": [10, "shield"], "4": [10, "armor"],
               "5": [5, "boots"], "6": [25, "EXP hat"], "7": ""}
    options_str = []
    for thing in options:
        options_str.append(str(thing))
    options_str.sort()
    while game_state_outer == 3:
        not_valid = True
        number_length = len(str(player.gold))
        spaces = 5 - number_length

        print("")
        print("-" * LENGTH_OF_SCREEN)
        print("| For help, type \"?\", Then press enter |")
        print("|         Item        |      Cost      |")
        print("|     1) Potion       |        8       |")
        print("|     2) Sword        |       10       |")
        print("|     3) Shield       |       10       |")
        print("|     4) Armor        |       10       |")
        print("|     5) Boots        |        5       |")
        print("|     6) EXP Hat      |       25       |")
        print("|     7) Leave                         |")
        print("|                  You have {0} gold {1}|".format(str(player.gold), (" "*spaces)))
        print("-" * LENGTH_OF_SCREEN)

        while not_valid:
            choice1 = input()
            if choice1 in options.keys():
                not_valid = False
            if not_valid:
                print('Please enter \"' + ("\", \"".join(options_str)) + "\"")  # list of sorted strings

        if choice1.isnumeric() and choice1 != "7":
            item = options[choice1][1]
            if player.gold >= int(options[choice1][0]):  # Increment if in inventory, set to 1 if not in inventory
                if item == 'sword':  # Increment Stats
                    player.attack += 1
                elif item == 'shield':
                    player.defense += 1
                elif item == 'armor':
                    player.max_health += 1
                    player.health += 1
                elif item == 'boots':
                    player.speed += 1

                if item in player.items:
                    player.items[item] += 1
                else:
                    player.items[item] = 1
                print("You have purchased " + item + "!")
            else:
                print("You do not have enough money to purchase this item.")
        elif not choice1.isnumeric():
            print(options[choice1])
        else:
            game_state_outer = 2


def show_menu(game_state):
    """Used to display the main menu and fight screen as well as takes inputs"""
    while True:
        spaces_in_between = LENGTH_OF_SCREEN - 2
        if game_state == 1:
            num_e_spaces = (14 - len(enemy.name))/2  # enemy
<<<<<<< HEAD
            num_e_spaces2 = num_e_spaces
            if num_e_spaces % 1 != 0:  # odd
=======
            if (len(enemy.name) % 2 != 0): #odd
>>>>>>> origin/master
                num_e_spaces = trunc(num_e_spaces)
                num_e_spaces2 = num_e_spaces + 1
            else:
                num_e_spaces = trunc(num_e_spaces)
                num_e_spaces2 = num_e_spaces
            num_e_spaces = int(num_e_spaces)
            num_e_spaces2 = int(num_e_spaces2)

            num_p_spaces = (14 - len(player.name))/2  # player
<<<<<<< HEAD
            num_p_spaces2 = num_p_spaces
            if num_p_spaces % 1 != 0:  # odd
=======
            if (len(player.name) % 2 != 0): #odd
>>>>>>> origin/master
                num_p_spaces = trunc(num_p_spaces)
                num_p_spaces2 = num_p_spaces + 1
            else:
                num_p_spaces = trunc(num_p_spaces)
                num_p_spaces2 = num_p_spaces
            num_p_spaces = int(num_p_spaces)
            num_p_spaces2 = int(num_p_spaces2)

            p_health = int(round((player.health / player.max_health) * 10))  # Player % Health as a single digit
            e_health = int(round((enemy.health / enemy.max_health) * 10))  # Enemy % Health as a single digit
            p_remaining = 10 - p_health
            e_remaining = 10 - e_health

            p_hp_percent = str(int(round((player.health / player.max_health) * 100)))  # Player % Health as a string
            e_hp_percent = str(int(round((enemy.health / enemy.max_health) * 100)))  # Enemy % Health as a string

            print("")
            print("-" * LENGTH_OF_SCREEN)  # Fight Screen
            print("|" + " " * spaces_in_between + "|")
            print("|  "+" "*num_p_spaces2+str(player.name)+" "*num_p_spaces+"     "+" "*num_e_spaces+str(enemy.name)+" "*num_e_spaces2+"   |")
            print("|     /"+" "*p_remaining+"|"*p_health+"\    /"+"|"*e_health+" "*e_remaining+"\     |")
            if p_hp_percent == '100':
                if e_hp_percent == '100':
                    print("| 100%)"+" "*p_remaining+"|"*p_health+"( vs )"+"|"*e_health+" "*e_remaining+"(100% |")
                else:
                    print("| 100%)"+" "*p_remaining+"|"*p_health+"( vs )"+"|"*e_health+" "*e_remaining+"( "+e_hp_percent+"% |")
            elif e_hp_percent == '100':
                print("| "+p_hp_percent+"% )"+" "*p_remaining+"|"*p_health+"( vs )"+"|"*e_health+" "*e_remaining+"(100% |")
            else:
                print("| "+p_hp_percent+"% )"+" "*p_remaining+"|"*p_health+"( vs )"+"|"*e_health+" "*e_remaining+"( "+e_hp_percent+"% |")
            print("|     \\"+" "*p_remaining+"|"*p_health+"/    \\"+"|"*e_health+" "*e_remaining+"/     |")
            print("|" + " " * spaces_in_between + "|")
            print("| 1) Attack                            |")  # Commands
            print("| 2) Escape                            |")  # Commands
            print("|" + " " * spaces_in_between + "|")
            print("-" * LENGTH_OF_SCREEN)

            while True:
                choice1 = input()
                if (choice1.isnumeric() is True) and (1 <= int(choice1) <= 2):
                    return int(choice1)
                print('Please enter "1" or "2" ')

        elif game_state == 2:
            print("")
            print("-" * LENGTH_OF_SCREEN)
            print("|" + " " * spaces_in_between + "|")
            print("| Type in the number, then press enter |")
            print("| 1) Fight New Enemy                   |")
            print("| 2) Shop                              |")
            print("| 3) Check Stats                       |")
            print("| 4) Quit                              |")
            print("|" + " " * spaces_in_between + "|")  # Commands
            print("|" + " " * spaces_in_between + "|")  # Commands
            print("|" + " " * spaces_in_between + "|")
            print("-" * LENGTH_OF_SCREEN)

            while True:
                choice2 = input()
                if (choice2.isnumeric() is True) and (1 <= int(choice2) <= 4):
                    return int(choice2)
                print("")
                print('Please enter "1", "2", "3", or "4" ')

        elif game_state == 4:
            exit()


#  Main Game
def main():
    """Controls the Beginning of the game and game loop"""
    global game_state_outer, player, enemy
    while True:
        print("")
        print("What's your name?")
        player_name = input("\t")
        if 0 <= len(player_name) <= 15:
            player = Rpg_Classes.Player(player_name)
            break
        print("")
        print("Less than 16 characters please")
    while True:
        option = show_menu(game_state_outer)
        if game_state_outer == 1:  # In a Fight
            if option == 1:  # Attack
                attack_main()
            elif option == 2:  # Escape
                game_state_outer = 2
        elif game_state_outer == 2:  # Menu
            if option == 1:  # Fight
                enemy = Rpg_Classes.Monster(list_of_names[randint(0, (len(list_of_names)-1))], 1)
                game_state_outer = 1
            elif option == 2:  # Shop
                game_state_outer = 3
                shop()
            elif option == 3:  # Stats
                get_stats()
            elif option == 4:
                game_state_outer = 4  # Quit

if __name__ == '__main__':
    main()