# The function will take as argument a dictionary from spots
def init_board(spots):
    board = (f"|{spots[1]}|{spots[2]}|{spots[3]}|\n"
             f"|{spots[4]}|{spots[5]}|{spots[6]}|\n"
             f"|{spots[7]}|{spots[8]}|{spots[9]}|")
    print(board)

def check_turn(turn):
    """Return 'X' or 'O' based on the turn number."""
    return "X" if turn % 2 == 1 else "O"

def check_win(spots):
    """Check for a winning combination."""
    winning_combinations = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],  # Rows
        [1, 4, 7], [2, 5, 8], [3, 6, 9],  # Columns
        [1, 5, 9], [3, 5, 7]              # Diagonals
    ]
    for combo in winning_combinations:
        if spots[combo[0]] == spots[combo[1]] == spots[combo[2]] and spots[combo[0]] in {"X", "O"}:
            return True
    return False

def minimax(board, depth, is_maximizing):
    """Implement Minimax algorithm to find the best move for the AI."""
    # Check if the current board state is a win for 'X' or 'O'
    if check_win(board):
        return 1 if not is_maximizing else -1
    # Check if all spots are filled (draw)
    elif all(board[key] in {"X", "O"} for key in board):
        return 0

    if is_maximizing:
        best_score = -float("inf")
        for key in board:
            # Check if the spot is available
            if board[key] not in {"X", "O"}:
                # Simulate placing 'O' (AI's move)
                board[key] = "O"
                score = minimax(board, depth + 1, False)
                # Undo the move
                board[key] = str(key)
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for key in board:
            # Check if the spot is available
            if board[key] not in {"X", "O"}:
                # Simulate placing 'X' (player's move)
                board[key] = "X"
                score = minimax(board, depth + 1, True)
                # Undo the move
                board[key] = str(key)
                best_score = min(score, best_score)
        return best_score

def find_best_move(board):
    """Determine the best move for the AI using Minimax."""
    best_score = -float("inf")
    best_move = None
    for key in board:
        if board[key] not in {"X", "O"}:
            # Simulate the AI's move
            board[key] = "O"
            score = minimax(board, 0, False)
            # Undo the move
            board[key] = str(key)
            # Select the move with the highest score
            if score > best_score:
                best_score = score
                best_move = key
    return best_move
