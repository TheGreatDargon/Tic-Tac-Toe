def main():
    print("Welcome to my Tic Tac Toe game!")
    print("Choose which game mode you want to play:")
    print("1. One Player (vs Computer)\n2. Two Players (vs Friend)\n3. Change Dimensions\n4. Exit")
    choice = int(input())
    match choice:
        case 1:
            one_player()
        case 2:
            two_player()
        case 3:
            change_dimensions()
        case 4:
            print("Thanks for playing!")
            exit()  
    

main()