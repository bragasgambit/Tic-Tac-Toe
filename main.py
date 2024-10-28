import os
from helpers import init_board, check_turn, check_win, find_best_move

spots = {
    1:"1", 2:"2", 3:"3", 4:"4", 5:"5",
    6:"6", 7:"7", 8:"8", 9:"9"
}

playing = True
complete = False
turn = 0
prev_turn = -1

# Choose game mode: 1 for two players, 2 for player vs AI
game_mode = input("Enter 1 for two players, 2 to play against AI: ")
play_with_ai = game_mode == "2"

while playing:
    # Reset screen
    os.system("cls" if os.name == "nt" else "clear")
    init_board(spots)

    # Show the player his invalid input
    if prev_turn == turn:
        print("Invalid spot, pick another")
    prev_turn = turn


    player = (turn % 2) + 1
    print(f"Player {player}'s turn: Pick a spot or press q to quit")

    # Get choice input from player or AI
    if play_with_ai and player == 2:
        # AI's turn: use Minimax to find the best move
        choice = find_best_move(spots)
        print(f"AI chooses spot {choice}")

    else:
        # Get player's input
        choice = input()

    if choice == "q":
        playing = False
        continue

    # Check for a wrong input - number from 1 - 9
    if str(choice).isdigit() and int(choice) in spots:
        choice = int(choice)
        # Check if the spots are already been taken
        if spots[choice] not in {"X", "O"}: # Check availability of spot
            turn += 1
            spots[choice] = check_turn(turn)
        else:
            prev_turn = turn  # If spot is taken, loop will show an error message
    else:
        prev_turn = turn  # If input is invalid, loop will show an error messag

    # Check if there is a winner
    if check_win(spots):
        playing, complete = False, True
    elif turn > 8:
        playing = False

# Display the final board
os.system("cls" if os.name == "nt" else "clear")
init_board(spots)

# Congratulate the winner or print the draw message
if complete:
    if check_turn(turn) == "X":
        print("Player 1 Wins!")
    else:
        print("Player 2 Wins!" if not play_with_ai else "AI Wins!")
else:
    print("Draw")

print("Thank you for playing!")
