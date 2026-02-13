#!/usr/bin/python3

def print_board(board):
    """Print the current Tic Tac Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    """Check if the given player has won."""
    # Rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    """Check if the board is full (draw)."""
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    """Main game loop for Tic Tac Toe."""
    board = [[" "]*3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue

        if not (0 <= row < 3 and 0 <= col < 3):
            print("Coordinates out of range. Try again.")
            continue
        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        board[row][col] = player

        if check_winner(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            break
        elif is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch player
        player = "O" if player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()
