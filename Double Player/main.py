class game:

    structure = ["_" for i in range(9)]

    def layout():
        count = 0
        for row in range(3):
            for col in range(3):
                print(game.structure[count],end="")
                count += 1
                if col != 2:
                    print(" | ", end="")
            print("")
        print()

    def user1_input():
        user_choice = int(input("Player 1 (x) Enter your move (1-9) : "))
        if game.structure[user_choice-1] == "_":
            game.structure[user_choice-1] = "X"
            game.layout()
        else:
            print("Invalid move")
            game.user1_input()

    def user2_input():
        pc_choice = int(input("Player 2 (O) Enter your move (1-9) : "))
        if game.structure[pc_choice-1] == "_":
            game.structure[pc_choice-1] = "O"
            game.layout()
        else:
            game.user2_input()

    def check(player):
        if ((game.structure[0] == game.structure[1] == game.structure[2] == player) or 
            (game.structure[3] == game.structure[4] == game.structure[5] == player) or 
            (game.structure[6] == game.structure[7] == game.structure[8] == player) or 
            (game.structure[0] == game.structure[3] == game.structure[6] == player) or 
            (game.structure[1] == game.structure[4] == game.structure[7] == player) or
            (game.structure[2] == game.structure[5] == game.structure[8] == player) or
            (game.structure[0] == game.structure[4] == game.structure[8] == player) or 
            (game.structure[2] == game.structure[4] == game.structure[6] == player)):
            if player == "X":
                print("Player 1 won")
                return True
            else:
                print("Player 2 won")
                return True
        else:
            return False


def main():
    game.layout()
    while True:
        game.user1_input()
        if game.check("X"):
            break

        game.user2_input()
        if game.check("O"):
            break


if __name__ == "__main__":
    main()
