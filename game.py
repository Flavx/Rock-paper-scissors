import random

standard = ["paper", "scissors", "rock"]

name = input("Enter your name: ")
print(f"Hello, {name}")

score = 0
# Reads the file to find a score linked to the user name
rating_file = open('rating.txt', 'r')
for line in rating_file:
    if name == line.split()[0]:
        score = int(line.split()[1])
rating_file.close()

# The options used in the game are given by the user,
# if the user skips this by pressing >enter,
# then the standard game is initiated.
user_option = input("> ")
if not user_option:
    game_option = standard
    half_options = 1  # is the number of winning options
else:
    game_option = user_option.split(",")
    half_options = round(int(len(game_option) / 2), None)  # To round down without using math module
print("Okay, let's start")

# Game loop starts
while True:
    player_choice = input("> ")
    computer_choice = random.choice(game_option)

    if player_choice == "!rating":  # checks the user rating
        print(f"Your rating: {score}")

    elif player_choice == "!exit":  # quits the infinite loop
        print("Bye")
        break

    elif player_choice not in game_option:
        if player_choice[0] != "!":
            print("Invalid input")

    elif player_choice == computer_choice:
        print(f"There is a draw ({computer_choice})")
        score += 50

    else:
        doubled_game_option = game_option * 2  # doubles the list to enable counting "half_options" after the -1 word
        index_player_choice = doubled_game_option.index(player_choice) + 1
        loser_list = []
        for item in doubled_game_option[index_player_choice:]:
            loser_list.append(item)
        if computer_choice in loser_list[:half_options]:
            print("Sorry, but computer chose {}".format(computer_choice))
        else:
            print(f"Well done. Computer chose {computer_choice} and failed")
            score += 100
