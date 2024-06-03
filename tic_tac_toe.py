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

    def check(player):
        combinations = [
        [0, 1, 2], [3, 4, 5],[6, 7, 8],
        [0, 3, 6],[1, 4, 7],[2, 5, 8],
        [0, 4, 8],[2, 4, 6]]

        for possibility in combinations:
            win = True
            for i in possibility:
                if game.structure[i] != player:
                    win = False
                    break
            if win:
                if player == "X":
                    print("Player X won")
                else:
                    print("Player O won")
                return True
                
        return False


    def pc_input():
        combination = [
        [0, 1, 2], [3, 4, 5],[6, 7, 8],
        [0, 3, 6],[1, 4, 7],[2, 5, 8],
        [0, 4, 8],[2, 4, 6]]
        pc_choice = -1

        for possibility in combination:
            count = 0
            temp = -1
            bot_count = 0
            for i in possibility:
                if game.structure[i] == "X":
                    count += 1
                elif game.structure[i] == "O":
                    bot_count += 1
                elif game.structure[i] == "_":
                    temp = i
            if count == 2 and temp != -1:
                pc_choice = temp
                break
            elif bot_count == 2 and temp != -1:
                pc_choice = temp
                break
                    
        if count == 2:
            game.structure[pc_choice] = "O"
            game.layout()

        elif bot_count == 2:
            game.structure[pc_choice] = "O"
            game.layout()

        elif game.structure[4] == "_":
            game.structure[4] = "O"
            game.layout()
        
        else:
            pc_choice = random.randint(1,9)
            if game.structure[pc_choice-1] == "_":
                game.structure[pc_choice-1] = "O"
                game.layout()
            else:
                game.pc_input()

    def draw():
        if "_" not in game.structure:
            return True

def main():
    while True:
        restart = input("Press Y to start the game and N to quit the game : ")
        if restart.upper() == "Y":
            while True:
                mode = input('''1 - For Single Player
2 - For Double Player
Enter the Mode: ''')
                if mode.isdigit() and int(mode) ==  2: 
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
                    game.structure = ["_" for i in range(9)]
                    break


                elif mode.isdigit() and int(mode) ==  1:
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
                    game.structure = ["_" for i in range(9)]
                    break
                else:
                    print("Choose mode correctly")
                
        elif restart.upper() == "N":
            break
        else:
            print("Y or N only allowed")
            main()

if __name__ == "__main__":
    main()
