import time
import random

x = 3
y = 1
game_ended = "no"

dungeon_layout = {
    (1,1) : "random",
    (2,1) : "a chest",
    (3,1) : "nothing",
    (4,1) : "a slime",
    (5,1) : "a shop",
    (1,2) : "wall",
    (2,2) : "a chest",
    (3,2) : "wall",
    (4,2) : "a shop",
    (5,2) : "a slime",
    (1,3) : "a wartlord",
    (2,3) : "a chest",
    (3,3) : "wall",
    (4,3) : "a shop",
    (5,3) : "random",
    (1,4) : "wall",
    (2,4) : "wall",
    (3,4) : "a shop",
    (4,4) : "wall",
    (5,4) : "wall",
    (1,5) : "a grubular",
    (2,5) : "a grubular",
    (3,5) : "a bananafana",
    (4,5) : "a grubular",
    (5,5) : "a grubular",
}

location = [3,1]
x = 3
y = 1

player_characteristics = {}

enemy_characteristics = {}

slime_characteristics = {
    "health" : 5,
    "attack" : 3,
    "protection" : 0,
}

wartlord_characteristics = {
    "health" : 10,
    "attack" : 4,
    "protection" : 2,
}

grubular_characteristics = {
    "health" : 15,
    "attack" : 5,
    "protection" : 2,
}

bananafana_characteristics = {
    "health" : 20,
    "attack" : 5,
    "protection" : 3,
}

human_characteristics = {
    "health" : 8,
    "attack" : 2,
    "protection" : 1,
}

dwarf_characteristics = {
    "health" : 9,
    "attack" : 2,
    "protection" : 0,
}

wizard_characteristics = {
    "health" : 7,
    "attack" : 2,
    "protection" : 2,
}

elf_characteristics = {
    "health" : 6,
    "attack" : 3,
    "protection" : 2,
}

rizzard_characteristics = {
    "health" : 100,
    "attack" : 67,
    "protection" : 6,
}



def choose_species():
    species = input("What species do you want to be?\nElf\nWizard\nDwarf\nHuman\n\t")
    time.sleep(1)
    if species.title() == 'Human':
        global player_characteristics
        player_characteristics = human_characteristics
        print("You're a Human!")
    elif species.title() == 'Dwarf':
        player_characteristics = dwarf_characteristics
        print("You're a Dwarf!")
    elif species.title() == 'Wizard':
        player_characteristics = wizard_characteristics
        print("You're a Wizard!")
    elif species.title() == 'Elf':
        player_characteristics = elf_characteristics
        print("You're an Elf!")
    elif species.title() == 'Rizzard':
        player_characteristics = rizzard_characteristics
        print("YOU'RE A RIZZARD! You found the easter egg. :)")
    elif species.title == 'Q':
        print("You need to restart the game now.")
    else:
        print("That's not one of the options.")
        choose_species()

choose_species()

time.sleep(2)

print(f"You have {player_characteristics.get('health')} health, your attack is {player_characteristics.get('attack')}, and you have {player_characteristics.get('protection')} protection.")

time.sleep(3)

def move():
    global location
    global x
    global y
    direction = input("Which way would you like to move?\nForwards\nLeft\nRight\nBackwards\n\t")
    if direction.title() and dungeon_layout[x+1,y] != "wall" == "Right":
        x += 1
    elif direction.title() == "Left":
        x -= 1
    elif direction.title() == "Forwards":
        y += 1
    elif direction.title() == "Backwards":
        y -= 1
    else:
        print("That's not one of the options.")
        print(direction)
        move()
    location[0] = x
    location[1] = y
    print(location)
    print(dungeon_layout[x,y])
    move()

def dungeon():
    room_contents = dungeon_layout.get((location[0], location[1]))
    print(f"In this room there is {room_contents}.")
    move()

dungeon()