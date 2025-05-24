import time

inventory = []

print("""\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nInstructions:
      
      You will recieve a list of actions.
      Enter the action you want to use.
      You have to write the action the exact way it is given to you.
      If you write it incorrectly, you will have to restart.
      """)
time.sleep(14)
print("""         _______________
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
        print("\n\nIt's dark and damp inside. A slimey key is sitting at the back. You pick it up.")
        time.sleep(1)
        print("\nYou got the cabin key!")
        inventory.append("cabin key")
        outside_the_house()
    elif action == "Go to house":
        if "cabin key" not in inventory:
            print("Up close, the logs of the cabin seem old, and they crumble slightly under you hand. The tarnished doorhandle doesn't budge. It's locked. You decide to \ngo back.")
            time.sleep(10)
            outside_the_house()
        else:
            print("The door is locked. You try the key that you found in the mailbox. Luckily, it works.")
            time.sleep(5)
            inside_the_house()
def inside_the_house():
    print("\nA musty smell tickles your nose. The cabin isn't very large. You see a kitchen on your left, a bedroom on your right, and a closed door in front of you.")
    time.sleep(13)
    print("\nA loud BANG brings you to your senses. The door just slammed behind you. It's locked. The key is on the outside...")
    time.sleep(6)
    print("\nYou need to get out.")
    time.sleep(1)
    print("\nActions:\nEnter kitchen\nGo through the door\nEnter the bedroom")
    action = input("\nWhat will you do? ")
outside_the_house()