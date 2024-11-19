# Function to print the Tic-Tac-Toe board
def print_board(board):
    print("-------------")
    for i in range(3):
        print("|", board[i][0], "|", board[i][1], "|", board[i][2], "|")
        print("-------------")

# Function to check if a player has won
def check_win(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:  # Check rows
            return True
        if board[0][i] == board[1][i] == board[2][i] == player:  # Check columns
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

# Function to check if the board is full
def is_board_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True

# Main game function
def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]  # Initialize empty board
    current_player = 'X'  

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn")

        # Get player's move
        while True:
            try:
                row, col = map(int, input("Enter row and column (1-3, space separated): ").split())

                # Adjust the input for 1-based index (convert to 0-2 internally)
                if row < 1 or row > 3 or col < 1 or col > 3:
                    print("Invalid position. Please enter values between 1 and 3.")
                elif board[row - 1][col - 1] != ' ':
                    print("This spot is already taken. Please choose another.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter two integers separated by a space.")

        # Make the move
        board[row - 1][col - 1] = current_player

        # Check for a winner
        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        # Check for a draw
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch players
        current_player = 'O' if current_player == 'X' else 'X'

# Run the game
if __name__ == "__main__":
    play_game()
