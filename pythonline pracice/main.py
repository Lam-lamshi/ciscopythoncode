
# input
import random

# ---------items of truth or dare--------

truth_items = ['What is your worst habit?', 'Do you sing in the shower?', 'Are you scared of the dark?']
dare_items = ['dance in the street like crazy.', 'Bark like a dog loudly.', 'take your shirt off spin it.']

# ---------------------------------------
times = input("how many times are you going to be playing?")
no_of_players = int(input("Enter the number of people that are going to play:"))
list_of_players = []
answer = "yes"
for i in range(no_of_players):
    players_name = input("enter your name: ")
    list_of_players.append(players_name)

while answer == "yes" or answer == "y":

    player = random.choice(list_of_players)
    print("its <<", player, ">> turn")
    Truth_dare = input("Enter truth or dare :")

    if Truth_dare == "truth":
        print(random.choice(truth_items))

    else :
        print(random.choice(dare_items))

    answer = input("do you want to continue the game?")