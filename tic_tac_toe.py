def print_board(board):
    print("\n")
    for i in range(3):
        print(board[i][0], "|", board[i][1], "|", board[i][2])
        if i < 2:
            print("---------")
    print("\n")


def check_winner(board, player):

    # rows
    for row in board:
        if row.count(player) == 3:
            return True

    # columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True

    # diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True

    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False


def tic_tac_toe():

    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"

    for turn in range(9):

        print_board(board)

        row = int(input("Enter row (0-2): "))
        col = int(input("Enter column (0-2): "))

        if board[row][col] == " ":
            board[row][col] = player
        else:
            print("Cell already taken. Try again.")
            continue

        if check_winner(board, player):
            print_board(board)
            print("Player", player, "wins!")
            return

        player = "O" if player == "X" else "X"

    print_board(board)
    print("It's a Draw!")


tic_tac_toe()