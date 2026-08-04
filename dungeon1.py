import time
import random
import sys

brown = "\033[38;5;94m"
black = "\033[30"
red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
blue = "\033[34m"
magenta = "\033[35m"
cyan = "\033[36m"
white = "\033[37m"

bold = "\033[1m"
underline = "\033[4m"

clear = "\033[0m"

x = 3
y = 1

dungeon_layout = {
    (1,1) : "random",
    (2,1) : "wall",
    (3,1) : "nothing",
    (4,1) : "a slime",
    (5,1) : "a shop",
    (1,2) : "wall",
    (2,2) : "a chest",
    (3,2) : "wall",
    (4,2) : "a shop",
    (5,2) : "a slime",
    (1,3) : "a witch",
    (2,3) : "a chest",
    (3,3) : "wall",
    (4,3) : "a shop",
    (5,3) : "random",
    (1,4) : "wall",
    (2,4) : "wall",
    (3,4) : "a shop",
    (4,4) : "wall",
    (5,4) : "wall",
    (1,5) : "a goblin",
    (2,5) : "a goblin",
    (3,5) : "a dragon",
    (4,5) : "a goblin",
    (5,5) : "a goblin",
}

location = [3,1]
x = 3
y = 1

enemy_characteristics = {}

prize = {}

slime_characteristics = {
    "health" : 5,
    "attack" : 1,
    "armor" : 0,
}

witch_characteristics = {
    "health" : 8,
    "attack" : 2,
    "armor" : 2,
}

goblin_characteristics = {
    "health" : 11,
    "attack" : 3,
    "armor" : 2,
}

dragon_characteristics = {
    "health" : 20,
    "attack" : 5,
    "armor" : 3,
}


player_characteristics = {}

human_characteristics = {
    "health" : 8,
    "attack" : 2,
    "armor" : 1,
}

dwarf_characteristics = {
    "health" : 9,
    "attack" : 2,
    "armor" : 0,
}

wizard_characteristics = {
    "health" : 7,
    "attack" : 2,
    "armor" : 2,
}

elf_characteristics = {
    "health" : 6,
    "attack" : 3,
    "armor" : 2,
}

rizzard_characteristics = {
    "health" : 100,
    "attack" : 67,
    "armor" : 41,
}



def choose_species():
    species = input(f"\n{bold}{cyan}What species would you like to be?{clear}\n\nHuman\nDwarf\nWizard\nElf\n\t").lower()
    time.sleep(1)

    if species != "human" and species != "dwarf" and species != "wizard" and species != "elf" and species != "rizzard":
        print(f"\n{bold}{red}That's not one of the options.{clear}")
        time.sleep(1)
        choose_species()
    else:
        print(f"\nYou are a {bold}{yellow}{species.title()}{clear}!")
        if species == "human":
            global human_characteristics
            global player_characteristics
            player_characteristics = human_characteristics.copy()
        elif species == "dwarf":
            global dwarf_characteristics
            player_characteristics = dwarf_characteristics.copy()
        elif species == "wizard":
            global wizard_characteristics
            player_characteristics = wizard_characteristics.copy()
        elif species == "elf":
            global elf_characteristics
            player_characteristics = elf_characteristics.copy()
        time.sleep(1)
        print(f"You have {bold}{green}{player_characteristics["health"]} health, {red}{player_characteristics["attack"]} attack{white}{clear} and {bold}{blue}{player_characteristics["armor"]} armor{clear}.")


def fight(enemy):
    if enemy == "a slime":
        global enemy_characteristics
        global slime_characteristics
        global prize
        enemy_characteristics = slime_characteristics.copy()
        prize = slime_characteristics.copy()
        enemy = "slime"
    elif enemy == "a witch":
        global witch_characteristics
        enemy_characteristics = witch_characteristics.copy()
        prize = witch_characteristics.copy()
        enemy = "witch"
    elif enemy == "a goblin":
        global goblin_characteristics
        enemy_characteristics = goblin_characteristics.copy()
        prize = goblin_characteristics.copy()
        enemy = "goblin"
    elif enemy == "a dragon":
        global dragon_characteristics
        enemy_characteristics = dragon_characteristics.copy()
        prize = dragon_characteristics.copy()
        enemy = "dragon"
    print(f"\nYou are fighting a {bold}{yellow}{enemy}{clear}!")
    time.sleep(1)
    print(f"\nThe {bold}{yellow}{enemy}{clear} has {bold}{green}{enemy_characteristics["health"]} health{clear}, does {red}{bold}{enemy_characteristics["attack"]} damage{clear} and has {blue}{bold}{enemy_characteristics["armor"]} armor{clear}.")
    while enemy_characteristics["health"] > 0 and player_characteristics["health"] > 0:
        time.sleep(2)
        player_damage = random.randint(-1, 1) + player_characteristics["attack"] - enemy_characteristics["armor"]
        if player_damage < 0:
            player_damage = 0
        enemy_characteristics["health"] -= player_damage
        if enemy_characteristics["health"] < 0:
            enemy_characteristics["health"] = 0
        print(f"\nYou {bold}{red}attacked{clear} the {bold}{yellow}{enemy}{clear} and dealt {bold}{red}{player_damage} damage{clear}.\nIts {bold}{blue}armor{clear} stopped {bold}{red}{enemy_characteristics['armor']} damage{clear}.\nIt has {bold}{green}{enemy_characteristics['health']} health{clear} left.")
        if enemy_characteristics["health"] > 0:
            enemy_damage = random.randint(-1, 1) + enemy_characteristics["attack"] - player_characteristics["armor"]
            if enemy_damage < 0:
                enemy_damage = 0
            time.sleep(2)
            player_characteristics["health"] -= enemy_damage
            if player_characteristics["health"] < 0:
                player_characteristics["health"] = 0
            print(f"\nThe {bold}{yellow}{enemy} {red}attacked{clear} you and dealt {bold}{red}{enemy_damage} damage{clear}.\nYour {bold}{blue}armor{clear} stopped {bold}{red}{player_characteristics['armor']} damage{clear}.\nYou have {bold}{green}{player_characteristics['health']} health{clear} left.")
    time.sleep(2)
    if player_characteristics["health"] == 0:
        print(f"{bold}{red}\n\nYou died.\n\n")
        time.sleep(2)
        print(r"""  ____    _    __  __ _____    _____     _______ ____  
 / ___|  / \  |  \/  | ____|  / _ \ \   / / ____|  _ \ 
| |  _  / _ \ | |\/| |  _|   | | | \ \ / /|  _| | |_) |
| |_| |/ ___ \| |  | | |___  | |_| |\ V / | |___|  _ < 
 \____/_/   \_\_|  |_|_____|  \___/  \_/  |_____|_| \_\ """)
        print("\n\n")
        sys.exit()
    else:
        print(f"\n{bold}{yellow}You defeated the {enemy}!{clear}")
        time.sleep(1)
        print(f"\nYou gained {bold}{green}{prize["health"]} health{clear}, {bold}{red}{prize["attack"]} attack damage{clear} and {bold}{blue}{prize["armor"]} armor{clear}.")
        player_characteristics["health"] += prize["health"]
        player_characteristics["attack"] += prize["attack"]
        player_characteristics["armor"] += prize["armor"]
        time.sleep(1)
        print(f"\nYou now have {bold}{green}{player_characteristics["health"]} health, {red}{player_characteristics["attack"]} attack{white}{clear} and {bold}{blue}{player_characteristics["armor"]} armor{clear}.")



def fight_or_not(current_room):
    time.sleep(1)
    choice = input(f"\n{bold}{cyan}Do you want to {red}fight it{cyan} or {blue}run{clear}?\n\nFight\nRun\n\t")
    if choice.lower() == "fight":
        fight(current_room)
    elif choice.lower() != "run":
        time.sleep(1)
        print(f"\n{bold}{red}That's not one of the options.{clear}")
        fight_or_not(current_room)

def read_room():
    global x
    global y
    current_room = dungeon_layout[x,y]
    time.sleep(1)
    print(f"\nIn this room there is {bold}{yellow}{current_room}{clear}.")
    if current_room == "a slime" or current_room == "a witch" or current_room == "a goblin" or current_room == "a dragon":
        fight_or_not(current_room)
    time.sleep(1)
    direction = input(f"\n{bold}{cyan}Which way would you like to go?{clear}\n\nLeft\nRight\nBackwards\nForwards\n\t")
    direction = direction.lower()
    if direction == "left":
        x -= 1
        if (x,y) in dungeon_layout.keys():
            if dungeon_layout[x,y] == "wall":
                x += 1
                print(f"{bold}{red}\nYou cannot go that way. There is a wall.{clear}")
        if (x,y) not in dungeon_layout.keys():
            x += 1
            print(f"{bold}{red}\nYou cannot go that way. There is a wall.{clear}")
    if direction == "right":
        x += 1
        if (x,y) in dungeon_layout.keys():
            if dungeon_layout[x,y] == "wall":
                x -= 1
                print(f"{bold}{red}\nYou cannot go that way. There is a wall.{clear}")
        if (x,y) not in dungeon_layout.keys():
            x -= 1
            print(f"{bold}{red}\nYou cannot go that way. There is a wall.{clear}")
    if direction == "forwards":
        y += 1
        if (x,y) in dungeon_layout.keys():
            if dungeon_layout[x,y] == "wall":
                y -= 1
                print(f"{bold}{red}\nYou cannot go that way. There is a wall.{clear}")
        if (x,y) not in dungeon_layout.keys():
            y -= 1
            print(f"{bold}{red}\nYou cannot go that way. There is a wall.{clear}")
    if direction == "backwards":
        y -= 1
        if (x,y) in dungeon_layout.keys():
            if dungeon_layout[x,y] == "wall":
                y += 1
                print(f"{bold}{red}\nYou cannot go that way. There is a wall.{clear}")
        if (x,y) not in dungeon_layout.keys():
            y += 1
            print(f"{bold}{red}\nYou cannot go that way. There is a wall.{clear}")
    elif direction != "backwards" and direction != "forwards" and direction != "right" and direction != "left":
        print(f"{bold}{red}That's not one of the options.{clear}")
    read_room()



print(f"{brown}{bold}")
print(r""" ____  _   _ _   _  ____ _____ ___  _   _       
|  _ \| | | | \ | |/ ___| ____/ _ \| \ | |      
| | | | | | |  \| | |  _|  _|| | | |  \| |      
| |_| | |_| | |\  | |_| | |__| |_| | |\  |      
|____/ \___/|_| \_|\____|_____\___/|_|_\_|____  
 / ___|  _ \    / \ \      / / |   | ____|  _ \ 
| |   | |_) |  / _ \ \ /\ / /| |   |  _| | |_) |
| |___|  _ <  / ___ \ V  V / | |___| |___|  _ < 
 \____|_| \_\/_/   \_\_/\_/  |_____|_____|_| \_\ """)

time.sleep(3)

choose_species()
read_room()
