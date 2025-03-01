def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    
    return False

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    board = [[" "] * 3 for _ in range(3)]
    players = ["X", "O"]
    
    print("Tic-Tac-Toe Game")
    print_board(board)
    
    for turn in range(9):
        player = players[turn % 2]
        print(f"Player {player}'s turn")
        
        while True:
            try:
                row, col = map(int, input("Enter row and column (0-2) separated by space: ").split())
                if board[row][col] == " ":
                    board[row][col] = player
                    break
                else:
                    print("Cell already occupied. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Enter row and column numbers between 0 and 2.")
        
        print_board(board)
        
        if check_winner(board, player):
            print(f"Player {player} wins!")
            return
    
    print("It's a draw!")

tic_tac_toe()
