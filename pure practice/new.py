# let the letters inputed be x and y
# Define a list to represent the game board
board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

# Define a function to print the game board
def print_board():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("---------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---------")
    print(f"{board[6]} | {board[7]} | {board[8]}")

# Define a function to check if there is a winner
def check_win(player):
    if (board[0] == player and board[1] == player and board[2] == player) or \
       (board[3] == player and board[4] == player and board[5] == player) or \
       (board[6] == player and board[7] == player and board[8] == player) or \
       (board[0] == player and board[3] == player and board[6] == player) or \
       (board[1] == player and board[4] == player and board[7] == player) or \
       (board[2] == player and board[5] == player and board[8] == player) or \
       (board[0] == player and board[4] == player and board[8] == player) or \
       (board[2] == player and board[4] == player and board[6] == player):
        return True
    else:
        return False

# Define the main game loop
player = "X"
while True:
    # Print the game board
    print_board()

    # Ask the current player to make a move
    move = int(input(f"{player}, choose a square (1-9): ")) - 1
    while board[move] != " ":
        move = int(input("That square is already taken. Choose another: ")) - 1

    # Update the game board with the player's move
    board[move] = player

    # Check if the game has ended
    if check_win(player):
        print_board()
        print(f"Congratulations {player}! You win!")
        break
    elif " " not in board:
        print_board()
        print("It's a tie!")
        break

    # Switch to the other player
    if player == "X":
        player = "O"
    else:
        player = "X"
