import random
class game:
    def layout():
        count = 1
        for row in range(3):
            for col in range(3):
                print(count,end="")
                count += 1
                if col != 2:
                    print(" | ", end="")
            print("")

    def user_input():
        user_choice = input("Enter the number of your choice (1-9) : ")
        return int(user_choice)

    def pc_input():
        pc_choice = random.randint(0,9)
        return pc_choice

    def update(position, player):
        structure = [['0' for _ in range(3)] for _ in range(3)]
        count = 1
        for row in range(3):
            for col in range(3):
                if count == position and player == "human":
                    structure[row][col] = 'X'
                elif count == position and player == "pc":
                    structure[row][col] = 'O'
                print(structure[row][col],end="")
                count += 1
                if col!=2:
                    print(" | ",end="")
            print("")


def main():
    while True:
        player_position = game.user_input()
        player = "human"
        game.update(player_position,player)


if __name__ == "__main__":
    main()
