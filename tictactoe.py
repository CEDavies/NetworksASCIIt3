def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def initialize_board():
    return [[" " for _ in range(3)] for _ in range(3)]

def main():
    board = initialize_board()
    print("Welcome to Tic Tac Toe!")
    print_board(board)
    player = "X"

    while True:
        move = input(f"Player {player}, enter your move (1-9): ")
        if move.isdigit() and 1 <= int(move) <= 9:
            row = (int(move) - 1) // 3
            col = (int(move) - 1) % 3
            if board[row][col] == " ":
                board[row][col] = player
                print_board(board)
                # Check for win or tie
                # Implement your win/tie checking logic here
                # For simplicity, I'm not including it in this basic example
                player = "O" if player == "X" else "X"
            else:
                print("That position is already taken. Try again.")
        else:
            print("Invalid input. Please enter a number between 1 and 9.")

if __name__ == "__main__":
    main()
