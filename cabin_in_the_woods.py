#This is my first python game. 
#It is about escaping from an abandoned cabin in the woods.
#The idea is completely (un)original.

import time
def game():
    inventory = []
    entered = []
    print("""\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nInstructions:
        
        You will recieve a list of actions.
        Enter the action you want to use.
        You have to write the action the exact way it is given to you.
        If you write it incorrectly, you will have to restart.
        All actions begin with a capital letter.
        """)
    time.sleep(1)
    print("""             _______________
            |-STARTING GAME-|
             ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾""")
    time.sleep(2)
    def outside_the_house():
        print("\n\nYou are standing outside a log cabin. It is dark inside the house. A rusty mailbox is standing next to you.")
        time.sleep(2)
        print("\nActions:\nGo to house\nOpen mailbox")
        time.sleep(2)
        action = input("\nWhat will you do? ")
        time.sleep(2)
        if action == "Open mailbox":
            if "cabin key" not in inventory:
                print("\nIt's dark and damp inside. A slimy key is sitting at the back. You pick it up.")
                time.sleep(2)
                print("\nYou got the cabin key!")
                inventory.append("cabin key")
                time.sleep(2)
                outside_the_house()
            else:
                print("\nYou've already checked here! There's nothing in the mailbox.")
                time.sleep(2)
                outside_the_house()
        elif action == "Go to house":
            if "cabin key" not in inventory:
                print("\nUp close, the logs of the cabin seem old, and they crumble slightly under you hand. The tarnished doorhandle doesn't budge. It's locked. You decide to \ngo back.")
                time.sleep(2)
                outside_the_house()
            else:
                print("\nThe door is locked. You try the key that you found in the mailbox. Luckily, it works.")
                time.sleep(2)
                inside_the_house()
    def inside_the_house():
        print("\nA musty odour tickles your nose. The cabin isn't very large. You see a kitchen on your left, a bedroom on your right, and a closed door in front of you.")
        time.sleep(2)
        if "entered" not in entered:
            time.sleep(5)
            print("\nA loud BANG brings you to your senses. The door just slammed behind you. It's locked. The key is on the outside...")
            time.sleep(1)
            print("\nYou need to get out.")
            entered.append("entered")
        print("\nActions:\nEnter kitchen\nGo through door\nEnter bedroom")
        time.sleep(2)
        action = input("\nWhat will you do? ")
        time.sleep(2)
        if action == "Enter kitchen":
            the_kitchen()
        if action == "Go through door":
            the_door()
        if action == "Enter bedroom":
            the_bedroom()
    def the_kitchen():
        print("\nAn ancient kerosene stove is gathering dust in the corner. A large cabinet towers next to a polished wood bench. An open box on the bench contains a \nsmall piece of cheese. A mouse sits next to it, gingerly nibbling on an end.")
        time.sleep(2)
        print("\nActions:\nTurn on stove\nOpen the cabinet\nGo back")
        time.sleep(2)
        action = input("\nWhat will you do? ")
        time.sleep(2)
        if action == "Turn on stove":
            print("\nYou twist a knob labeled \"TURN ON\". The stove clicks, and then flames leap from the stove. You realise that using a stove in a cabin made of wood \nisn't a very good idea. In an act of deparation, you try to smash the windows to get out, but they are harder that stone. You are a goner.")
            time.sleep(2)
            print("\nIf you go back to the kitchen, then all of your progress will be saved.")
            time.sleep(2)
            print("\nActions:\nRestart\nGo back to the kitchen")
            time.sleep(2)
            action = input("\nWhat will you do? ")
            time.sleep(2)
            if action == "Restart":
                game()
            elif action == "Go back to the kitchen":
                the_kitchen()
        elif action == "Open the cabinet":
            print("\nThe rusty metal hinges squeal as you ease open the cabinet. Inside, you find a magnifying glass. The magnifying glass seems \nto make everything turn upside down.")
            time.sleep(2)
            print("\nYou got the magnifying glass!")
            inventory.append("magnifying glass")
            time.sleep(2)
            the_kitchen()
        elif action == "Go back":
            inside_the_house()
    def the_door():
        if "skull shaped key" in inventory:
            print("\nYour skull key fits perfectly, and the door swings open. You step forward and into the next room.")
            time.sleep(2)
            through_the_door()
        elif "skull shaped key" not in inventory:
            print("\nIt appears that this door is locked too. You peer down at the keyhole and notice that it is shaped like a skull. You decide to go back.")
            time.sleep(2)
            inside_the_house()
    def the_bedroom():
        print("\nA layer of dust thicker than the blankets coats the bed. A bedside table has an (also dusty) reading light and a built in drawer. There appears to be a \nloose floorboard as well.")
        time.sleep(2)
        print("\nActions:\nLook in drawer\nLook under loose floorboard\nGo back")
        time.sleep(2)
        action = input("\nWhat will you do? ")
        time.sleep(2)
        if action == "Look under loose floorboard":
            if "flat head screwdriver" not in inventory:
                print("\nThe floorboard is moving, but you can't get your fingernails underneath it. If only you had something to lever it up...")
                time.sleep(2)
                the_bedroom()
            else:
                if "skull shaped key" not in inventory:
                    print("\nYou use your handy screwdriver to lever the floorboard up, and underneath, you find a skull shaped key.")
                    time.sleep(2)
                    print("\nYou found the skull shaped key!")
                    inventory.append("skull shaped key")
                    time.sleep(2)
                    the_bedroom()
                else:
                    print("\nWhy did you check here again? There's nothing to find.")
                    time.sleep(2)
                    the_bedroom()
        elif action == "Look in drawer":
            if "flat head screwdriver" not in inventory:
                print("\nYou peer into the drawer and find a flat head screwdriver.")
                time.sleep(2)
                print("\nYou got the flat head screwdriver!")
                inventory.append("flat head screwdriver")
                time.sleep(2)
                the_bedroom()
            else:
                print("\nWhy did you check here again? There's nothing to find.")
        elif action == "Go back":
            inside_the_house()
    def through_the_door():
        print("\nYou see a study. On the desk, there are some papers with writing on them. You can't quite make it out. There is a door with a key pad on it in the \ncorner.")
        time.sleep(2)
        print("\nActions:\nLook at the papers\nGo to the door\nGo back")
        time.sleep(2)
        action = input("\nWhat will you do? ")
        time.sleep(2)
        if action == "Look at the papers":
            if "magnifying glass" not in inventory:
                print("\nYou squint your eyes at the text, but it's so small that you can't make it out.")
                time.sleep(2)
                through_the_door()
            else:
                print("\nYou use your magnifying glass that turns things upside down to look at the text, and you see: ⅃⅃30. I wonder what that means...")
                time.sleep(2)
                through_the_door()
        elif action == "Go to the door":
            keypad()
        elif action == "Go back":
            inside_the_house()
    def keypad():
        print("\nThe keypad says that it needs a four digit code.")
        time.sleep(2)
        print("\nActions:\nEnter a code\nGo back")
        time.sleep(2)
        action = input("\nWhat will you do? ")
        time.sleep(2)
        if action == "Enter a code":
            code = input("\nWhat will you enter?")
            if code == "7730":
                escape()
            else:
                print("\nThe code was incorrect")
                keypad()
        if action == "Go back":
            through_the_door()
    def escape():
        print("\nThe lock clicks and the door swings open. A cool breeze brushes your face and the trees outside sway. You step out and leave the house for good.")
    outside_the_house()
game()