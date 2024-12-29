import time
import random


def print_pause(message):
    print(message)
    time.sleep(2)


# field options
def field():
    print_pause("You find yourself standing in an open field, "
                "filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a wicked fairy is somewhere around here, "
                "and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your "
                "trusty (but not very effective) dagger.")

    while True:
        choice = input(
            "Enter 1 to knock on the door of the house.\n"
            "Enter 2 to peer into the cave.\n"
            "What would you like to do? (Please enter 1 or 2): "
        )
        if choice == "1":
            house()
            break
        elif choice == "2":
            cave()
            break
        else:
            print_pause("Input can only be 1 or 2.")


# house options
def house():
    print_pause("You walk up to the door of the house and knock.")
    print_pause("A grumpy old man opens the door. "
                "He tells you there is nothing inside but cobwebs.")

    while True:
        choice = input(
            "Enter 1 to leave the house and go back to the field.\n"
            "Enter 2 to search the house for treasures.\n"
            "What would you like to do? (Please enter 1 or 2): "
        )
        if choice == "1":
            field()
            break
        elif choice == "2":
            if random.choice([True, False]):
                print_pause("You find a small chest")
                print_pause("Inside, you find a magical sword! "
                            "You are now ready to face any enemy!")
                win()
            else:
                print_pause("You search the house but find nothing useful. "
                            "The man laughs at your wasted time.")
                print_pause("You leave the house and return to the field.")
                field()
            break
        else:
            print_pause("Input can only be 1 or 2.")


# cave options
def cave():
    print_pause("You enter the cave and it's dark and cold.")
    print_pause("You hear strange noises echoing through the walls.")
    print_pause("Suddenly, a goblin appears in front of you!")

    while True:
        choice = input(
            "Enter 1 to fight the goblin.\n"
            "Enter 2 to flee back to the field.\n"
            "What would you like to do? (Please enter 1 or 2): "
        )
        if choice == "1":
            fight("dagger")
            break
        elif choice == "2":
            print_pause("You quickly flee back to the field.")
            field()
            break
        else:
            print_pause("Input can only be 1 or 2.")


# fight options
def fight(player_weapon):
    player_health = 100
    goblin_health = 50
    weapon_power = 25 if player_weapon == "dagger" else 50

    print_pause("You are fighting a goblin!")
    print_pause(f"You have {player_health} health and are armed with a "
                f"{player_weapon}.")
    print_pause(f"The goblin has {goblin_health} health.")

    while player_health > 0 and goblin_health > 0:
        action = input("Enter 1 to attack or 2 to flee: ").strip()
        if action == "1":
            damage = random.randint(10, weapon_power)
            goblin_health -= damage
            print_pause(f"You strike the goblin and deal {damage} damage!")
            if goblin_health <= 0:
                print_pause("You defeated the goblin!")
                win()
                return
            enemy_damage = random.randint(10, 30)
            player_health -= enemy_damage
            print_pause(f"The goblin attacks you back, dealing {enemy_damage} "
                        "damage.")
            if player_health <= 0:
                print_pause("You have been defeated!")
                game_over()
                return
        elif action == "2":
            print_pause("You flee back to the field.")
            field()
            return
        else:
            print_pause("Invalid input! Please enter 1 or 2.")


# win options
def win():
    print_pause("You aced the game, CONGRATS!")
    play_again()


# lose options
def game_over():
    print_pause("Better luck next time!")
    play_again()


# play again options
def play_again():
    while True:
        choice = input("Wanna replay?? (y/n): ").lower()
        if choice == "y":
            print_pause("Here we go again!")
            field()
            break
        elif choice == "n":
            print_pause("See you next time!")
            break
        else:
            print_pause("Input can only be y or n.")


field()
