import random
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

    def user1_input(): #Double player mode user 1
        user1_choice = input("Player 1 (X) Enter your move (1-9) : ")
        if user1_choice.isdigit() and int(user1_choice) in range(1, 10):
            if game.structure[int(user1_choice)-1] == "_":
                game.structure[int(user1_choice)-1] = "X"
                game.layout()
            else:
                print("Invalid move")
                game.user1_input()
        else:
            print("Enter only number between 1 to 9")
            game.user1_input()


    def user2_input(): #Double player mode user 2
        user2_choice = input("Player 2 (O) Enter your move (1-9) : ")
        if user2_choice.isdigit() and int(user2_choice) in range(1, 10):
            if game.structure[int(user2_choice)-1] == "_":
                game.structure[int(user2_choice)-1] = "O"
                game.layout()
            else:
                print("Invalid Move")
                game.user2_input()
        else:
            print("Enter only number between 1 to 9")
            game.user2_input()
    
    def user_input():#Single player mode user 1
        user_choice = input("Enter the number of your choice (1-9) : ")
        if user_choice.isdigit() and int(user_choice) in range(1, 10):
            if game.structure[int(user_choice)-1] == "_":
                game.structure[int(user_choice)-1] = "X"
                game.layout()
            else:
                print("Invalid move")
                game.user_input()
        else:
            print("Enter only number between 1 to 9")
            game.user_input()


    def pc_input():
        pc_choice = random.randint(1,9)
        if game.structure[pc_choice-1] == "_":
            game.structure[pc_choice-1] = "O"
            game.layout()
        else:
            game.pc_input()

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
        
    def draw():
        if "_" not in game.structure:
            return True


def main():
    mode = int(input('''1 - For Single Player
2 - For Double Player
Enter the Mode: '''))
    if mode == 2 :
        print("\nYou Are Playing Double Player Mode \n")
        game.layout()
        while True:
            game.user1_input()
            if game.check("X"):
                break
            if game.draw():
                print("Match Draw")
                break

            game.user2_input()
            if game.check("O"):
                break
            if game.draw():
                print("Match Draw")
                break

    elif mode == 1:
        print(" \nYou Are Playing Single Player Mode\n")
        game.layout()
        while True:
            game.user_input()
            if game.check("X"):
                break
            if game.draw():
                print("Match Draw")
                break

            game.pc_input()
            if game.check("O"):
                break
            if game.draw():
                print("Match Draw")
                break
    else:
        print("Choose mode correctly")
        main()


if __name__ == "__main__":
    main()
