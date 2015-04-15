__author__ = 'Austin'
from random import randint
from math import trunc
import RPG_Game_Classes as Rpg_Classes

list_of_names = ["Evil Cat", " Sneaky Mouse", "Mad Rat", "Flying Hat", "Mean Bumblebee", "Slow Slug", "Slimy Snail",
                 "Traffic Cone", "Tall Walrus", "Wiggly Noodles", "Angry Waffle"]
LENGTH_OF_SCREEN = 40
game_state_outer = 2


def check_death():
    if player.health == 0:
        return "player"
    elif enemy.health == 0:
        return "enemy"
    return 'none'


def player_win():
    spaces_in_between = LENGTH_OF_SCREEN - 2
    spaces_enemy = (spaces_in_between - 5) - len(enemy.name)
    print("-" * LENGTH_OF_SCREEN)
    print("|" + " " * spaces_in_between + "|")
    print("|" + " " * spaces_in_between + "|")
    print("| You have defeated: " + " " * 18 + "|")
    print("|     " + enemy.name + " " * spaces_enemy + "|")
    print("|" + " " * spaces_in_between + "|")
    print("|" + " " * spaces_in_between + "|")
    print("|" + " " * spaces_in_between + "|")
    print("| Press enter to return to main menu.. |")
    print("|" + " " * spaces_in_between + "|")
    print("-" * LENGTH_OF_SCREEN)
    input()


def enemy_win():
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


def gain_exp(amount):
    player.exp += amount
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


def attack_p_1():
    global game_state_outer
    player.attack_enemy(enemy)
    if check_death() is 'enemy':  # .                        Enemy dies
        player_win()  # Win Screen
        gain_exp(enemy.level)  # EXP Gain
        game_state_outer = 2
        player.health = player.max_health  # Reset Health
    elif check_death() is 'none':  # .                        No one dies
        enemy.attack_player(player)
        if check_death() is 'player':  # .                             Player dies
            enemy_win()
            game_state_outer = 2
            player.health = player.max_health
        elif check_death() is "enemy":  # .                            Enemy dies
            player_win()  # Win Screen
            gain_exp(enemy.level)  # EXP Gain
            game_state_outer = 2
            player.health = player.max_health  # Reset Health
    elif check_death() is 'player':  # .                      Player dies
        enemy_win()
        game_state_outer = 2
        player.health = player.max_health


def attack_e_1():
    global game_state_outer
    enemy.attack_player(player)
    if check_death() is 'player':
        enemy_win()
        game_state_outer = 2
        player.health = player.max_health
    elif check_death() is 'none':
        player.attack_enemy(enemy)
        if check_death() is 'enemy':
            player_win()  # Win Screen
            gain_exp(enemy.level)  # EXP Gain
            game_state_outer = 2
            player.health = player.max_health  # Reset Health
        elif check_death() is 'player':
            enemy_win()
            game_state_outer = 2
            player.health = player.max_health
    elif check_death() is 'enemy':
        player_win()  # Win Screen
        gain_exp(enemy.level)  # EXP Gain
        game_state_outer = 2
        player.health = player.max_health  # Reset Health


def attack_main():
    global game_state_outer
    if player.speed > enemy.speed:  # Player is faster
        attack_p_1()
    elif player.speed < enemy.speed:
        attack_e_1()
    else:
        x = randint(0, 1)
        if x == 0:
            attack_p_1()
        elif x == 1:
            attack_e_1()


def show_menu(game_state):
    while True:
        spaces_in_between = LENGTH_OF_SCREEN - 2
        if game_state == 1:
            num_e_spaces = (14 - len(enemy.name))/2  # enemy
            num_e_spaces2 = num_e_spaces
            if (len(enemy.name) % 2) != 0:  # odd  and (num_e_spaces != 0)
                trunc(num_e_spaces)
                num_e_spaces2 = num_e_spaces + 1
            num_e_spaces = int(num_e_spaces)
            num_e_spaces2 = int(num_e_spaces2)

            num_p_spaces = (15 - len(player.name))/2  # player
            num_p_spaces2 = num_p_spaces
            if (len(player.name) % 2) != 0:  # odd
                trunc(num_p_spaces)
                num_p_spaces2 = num_p_spaces + 1
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
            print("| 2) Check Stats                       |")
            print("| 3) Quit                              |")
            print("|" + " " * spaces_in_between + "|")
            print("|" + " " * spaces_in_between + "|")  # Commands
            print("|" + " " * spaces_in_between + "|")  # Commands
            print("|" + " " * spaces_in_between + "|")
            print("-" * LENGTH_OF_SCREEN)

            while True:
                choice2 = input()
                if (choice2.isnumeric() is True) and (1 <= int(choice2) <= 3):
                    return int(choice2)
                print("")
                print('Please enter "1", "2", or "3" ')

        elif game_state == 3:
            exit()


#  Main Game
def main():
    global game_state_outer, player, enemy
    while True:
        print("")
        print("What's your name?")
        player_name = input("\t")
        if len(player_name) <= 15:
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
            elif option == 2:  # Stats
                get_stats()
            elif option == 3:
                game_state_outer = 3  # Quit

if __name__ == '__main__':
    main()