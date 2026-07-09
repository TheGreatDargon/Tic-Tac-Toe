import numpy as np

col = 3
row = 3
the_board = np.zeros((row, col), dtype=str)

def print_board(the_board):
    print("    \t  1\t\t  2\t\t  3")
    print("-------------------------------------------------")
    row_num = 1
    for row in the_board:
        print(f"{row_num}", end="")
        for space in row:
            print(f"  |\t{space}\t", end="")
        print("|")
        print("-------------------------------------------------")
        row_num += 1

def make_move(the_board, move, piece):
    try:
        move = list(map(int, move))
        if move[0]-1 > row or move[0]-1 < 0 or move[1]-1 > col or move[1]-1 < 0:
            return False
        if len(move) == 2 and move.count('') == 0:
            if the_board[move[0]-1][move[1]-1] != '':
                print("Spot full, try again.")
                return False
            the_board[move[0]-1][move[1]-1] = piece
            print_board(the_board)
            return True
    except:
        return False

    return False

def is_winner(the_board, piece):
    # Winner for rows
    if any(np.all(the_board == piece, axis=1)):
        return True
    # Winner for cols
    if any(np.all(the_board == piece, axis=0)):
        return True
    # Winner for Diagonals
    if np.all(np.diagonal(the_board) == piece):
        return True
    if np.all(np.diagonal(np.fliplr(the_board)) == piece):
        return True
    return False



def select_piece():
    piece = ""
    piece = input("Please choose your piece (X or O): ")
    while len(piece) != 1:
        print("Please enter a single character.")
        piece = input("Please choose your piece (X or O): ")

 
    return piece

def game(comp = 0):

    print("You have chosen to play against a friend.")
    print("Player 1 ", end="")
    player1 = select_piece()
    print("Player 2 ", end="")
    player2 = select_piece()

    while player2 == player1:
        print("Player 2 cannot choose the same piece as Player 1.")
        player2 = select_piece()

    while True:
        print_board(the_board)

        move = input("Player 1 turn: please enter a row and column number (row, column) to place your piece: ")
        while not make_move(the_board, move.split(","), player1):
            move = input("Please enter a valid move in the format (row, column): ")

        if is_winner(the_board, player1):
            print(f"Player 1 ({player1}) wins!")
            break

        move = input("Player 2 turn: please enter a row and column number (row, column) to place your piece: ")
        while not make_move(the_board, move.split(","), player2):
            move = input("Please enter a valid move in the format (row, column): ")

        if is_winner(the_board, player2):
            print(f"Player 2 ({player2}) wins!")
            break

    


def main():
    print("Welcome to my Tic Tac Toe game!")
    print("Choose which game mode you want to play:")
    print("1. One Player (vs Computer)\n2. Two Players (vs Friend)\n3. Change Dimensions\n4. Exit")
    try:
        choice = int(input())
    except:
        choice = int(input("Incorrect input\n1. One Player (vs Computer)\n2. Two Players (vs Friend)\n3. Change Dimensions\n4. Exit"))
    match choice:
        case 1:
            game(1)
        case 2:
            game()
        case 3:
            change_dimensions()
        case _:
            print("Thanks for playing!")
            exit()  
    

main()