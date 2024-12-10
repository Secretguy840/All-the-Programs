import random
import time

# Function to introduce the game and the setting
def intro():
    print("Welcome to Resident Evil: The Escape.")
    time.sleep(1)
    print("You are a survivor trapped in a haunted mansion.")
    time.sleep(1)
    print("Zombies roam the halls, and you need to find a way to escape.")
    time.sleep(1)
    print("You have limited resources, so be careful with your choices!")
    time.sleep(2)

# Function to show the player's inventory
def show_inventory(inventory):
    print("\nYour inventory:")
    if len(inventory) == 0:
        print("You have no items.")
    else:
        for item in inventory:
            print(f"- {item}")

# Function to handle fighting zombies
def fight_zombie():
    print("\nA zombie approaches! You must fight!")
    time.sleep(1)
    action = input("Do you want to [fight] or [run]? ").lower()

    if action == "fight":
        if random.random() > 0.5:  # 50% chance of winning
            print("\nYou defeated the zombie!")
            return True
        else:
            print("\nThe zombie overwhelmed you. You didn't survive.")
            return False
    elif action == "run":
        print("\nYou ran away safely, but you lost some time.")
        return True
    else:
        print("\nInvalid choice! The zombie attacks you!")
        return False

# Main function for the game
def start_game():
    inventory = []
    health = 3  # 3 health points to start
    game_over = False

    intro()

    while not game_over and health > 0:
        print("\nYou are in a dark hallway. There are two doors ahead of you.")
        time.sleep(1)
        print("One leads to a kitchen, and the other to the library.")
        action = input("Do you want to go to the [kitchen] or [library]? ").lower()

        if action == "kitchen":
            print("\nYou enter the kitchen.")
            time.sleep(1)
            print("There are some cans of food on the shelf, and a knife on the counter.")
            action = input("Do you want to take the [food] or [knife]? ").lower()
            
            if action == "food":
                inventory.append("canned food")
                print("\nYou took the food. It might come in handy later.")
            elif action == "knife":
                inventory.append("knife")
                print("\nYou took the knife. It's a good weapon for defense.")
            else:
                print("\nYou decided not to take anything.")
            time.sleep(1)

        elif action == "library":
            print("\nYou enter the library.")
            time.sleep(1)
            print("A zombie appears out of nowhere! You must act fast.")
            health -= 1  # Lose health if the player gets into a fight
            if not fight_zombie():
                health = 0  # If the player loses the fight, game over
            time.sleep(1)

        else:
            print("\nInvalid choice! You must choose a valid door.")
            time.sleep(1)

        show_inventory(inventory)
        print(f"Your health: {health}")

        if health <= 0:
            print("\nGame Over! You were defeated.")
            game_over = True
        else:
            continue_game = input("Do you want to continue exploring? [yes/no] ").lower()
            if continue_game == "no":
                print("\nYou decided to leave the mansion. You survived, but at what cost?")
                game_over = True

    print("\nThank you for playing!")

# Run the game
start_game()
