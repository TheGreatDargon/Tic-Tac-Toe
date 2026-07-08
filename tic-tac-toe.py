def select_piece():
    piece = ""
    while piece not in [r"A-Z", r"a-z"]:
        piece = input("Please choose your piece (X or O): ")
        if len(piece) < 2:
            break
        else:
            print("Please choose a single character.")
 
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


def main():
    print("Welcome to my Tic Tac Toe game!")
    print("Choose which game mode you want to play:")
    print("1. One Player (vs Computer)\n2. Two Players (vs Friend)\n3. Change Dimensions\n4. Exit")
    choice = int(input())
    match choice:
        case 1:
            game(1)
        case 2:
            game()
        case 3:
            change_dimensions()
        case 4:
            print("Thanks for playing!")
            exit()  
    

main()