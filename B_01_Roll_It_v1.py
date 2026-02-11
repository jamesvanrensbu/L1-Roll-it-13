# functions go here
from C_01_yes_no_basic import want_instructions


def yes_no(question):...


def instructions():
    """Prints instructions"""

    print("""
*** Instructions ***
    
Roll the dice and try to win!
     """)


def int_checker():
    """Checks users enter an integer more than / equal to 13"""

    error = "Please enter an integer more than / equal to 13"

    while True:
        try:
            response = int(input("What is the game goal? "))

            if response < 13:
                print(error)
            else:
                return response



        except ValueError:
            print(error)


# ask the user if they want instructions (check they say yes / no)
var = want_instructions == yes_no

# Display the instructions if the user wants to see them...
if want_instructions == "yes":
    instructions()


print()
game_goal = int_checker()
print(game_goal)
