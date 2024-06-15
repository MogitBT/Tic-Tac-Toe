import random
import os
import pickle
class game:

    structure = ["_" for i in range(9)]
    current_mode = None

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
        user1_choice = input("Player 1 (X) Enter your move (1-9) or S to save game and R to refresh : ")

        if user1_choice.upper() == "S":
            game.save()
            main()
        elif user1_choice.upper() == "R":
            second_player = input("Second player enter R to refresh and N to deny : ")
            if second_player.upper() == "R":
                game.refresh()
                print("Game refreshed")
                game.layout()    
                game.user1_input()
            elif second_player.upper() == "N":
                print("Player 2 doesn't want to refresh")
                game.user1_input()
            else:
                print("Denied")
                game.user1_input()

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
        user2_choice = input("Player 2 (O) Enter your move (1-9) or S to save gameand R to refresh : ")

        if user2_choice.upper() == "S":
            game.save()
            main()
        elif user2_choice.upper() == "R":
            first_player = input("First player enter R to refresh and N to deny : ")
            if first_player.upper() == "R":
                game.refresh()
                print("Game refreshed")
                game.layout()    
                game.user1_input()
            elif first_player.upper() == "N":
                print("Player 1 doesn't want to refresh")
                game.user2_input()
            else:
                print("Denied")
                game.user2_input()

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
        user_choice = input("Enter the number of your choice (1-9) or S to save game and R to refresh : ")

        if user_choice.upper() == "S":
            game.save()
            main()
        elif user_choice.upper() == "R":
            game.refresh()
            print("The Game has been refreshed")
            game.layout()
            game.user1_input()

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
    
    def save():
        filename = input("Enter the file name to save : ")
        filename += ".pkl"
        with open(filename,'wb') as f:
            pickle.dump((game.structure,game.current_mode), f)
        print("Game saved Successfully")

    def load():
        filename = input("Enter the name of the file to be loaded : ")
        filename += ".pkl"

        if os.path.exists(filename):
            with open(filename,'rb') as f:
                game.structure, game.current_mode = pickle.load(f)
            print("Game Loaded Successfully")
            game.layout()
        else:
            print("No game data exist")


    def pc_input():
        combination = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8], 
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  
            [0, 4, 8], [2, 4, 6]             
        ]
        pc_choice = -1

        for possibility in combination:
            bot_count = 0
            bot_temp = -1
            for i in possibility:
                if game.structure[i] == "O":
                    bot_count += 1
                elif game.structure[i] == "_":
                    bot_temp = i

            if bot_count == 2 and bot_temp != -1:
                pc_choice = bot_temp
                break

        
        if pc_choice == -1:
            for possibility in combination:
                count = 0
                temp = -1
                for i in possibility:
                    if game.structure[i] == "X":
                        count += 1
                    elif game.structure[i] == "_":
                        temp = i

                if count == 2 and temp != -1:
                    pc_choice = temp
                    break    

        if pc_choice == -1 and game.structure[4] == "_":
            pc_choice = 4

        if pc_choice == -1:
            empty_positions = [i for i in range(9) if game.structure[i] == "_"]
            if empty_positions:
                pc_choice = random.choice(empty_positions)

        game.structure[pc_choice] = "O"
        game.layout()
    
    def tutorial():
        combination = [
                        [0, 1, 2], [3, 4, 5], [6, 7, 8], 
                        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
                        [0, 4, 8], [2, 4, 6]             
                    ]
        bot_combination = [
                        [6, 4, 8], [1, 8, 6], [0, 4, 2],
                        [2, 4, 8], [0, 2, 8], [0, 4, 6],
                        [1, 6, 4], [1, 3, 7]
                    ]
        level_count = 1  
        val = 0         
        for combo in combination:
            bot_combo = bot_combination[val]
            val += 1
            bot_val = 0
            for i in combo:
                game.structure[i] = "√"
                game.layout()
                while True:
                    try :
                        tut_choice = int(input("Enter the Position where the symbol is '√' : "))
                        if tut_choice -1 == i:
                            game.structure[tut_choice-1] = "X"
                            game.layout()
                            tut_bot = bot_combo[bot_val]
                            bot_val += 1
                            game.structure[tut_bot] = "O"
                            break
                        else:
                            print("Enter the position number correctly")
                            game.layout()
                            hint = input("Do you need hint?. Enter 'Y' for hint and 'N' to try again : ")
                            if hint.upper() == "Y":
                                print("The position where the '√' is placed is {position}".format(position = i+1))
                            game.layout()
                    except ValueError:
                        print("Enter the Correct position")
                        
            print("Congratulations Successfully Completed Level {lvl}".format(lvl = level_count))
            level_count += 1
            game.refresh()
        print("You have finished the tutorial successfully. You are ready to play")

    def draw():
        if "_" not in game.structure:
            return True
        
    def refresh():
        game.structure = ["_" for i in range(9)]


def main():
    while True:
        restart = input("Press Y to start the game, N to quit the game And L to load game: ")
        if restart.upper() == "Y":
            while True:
                mode = input('''1 - For Single Player
2 - For Double Player
3 - For Tutorial
Enter the Mode : ''')
                if mode.isdigit() and int(mode) ==  2: 
                    print("\nYou Are Playing Double Player Mode \n")
                    game.current_mode = 2
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
                    game.current_mode = 1
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

                elif mode.isdigit() and int(mode) == 3:
                    print("\nYou have Selected the tutorial")
                    game.tutorial()
                    main()
            
                else:
                    print("Choose mode correctly")

        elif restart.upper() == "L":
            game.load()
            if game.current_mode == 2:
                print("\nYou Are Playing Double Player Mode \n")
                game.current_mode = 2
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
            elif game.current_mode == 1:
                print(" \nYou Are Playing Single Player Mode\n")
                game.current_mode = 1
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
            else:
                print("Invalid game mode loaded.")
                game.structure = ["_" for i in range(9)]
                
        elif restart.upper() == "N":
            break
        else:
            print("Y or N only allowed")
            main()

if __name__ == "__main__":
    main()
