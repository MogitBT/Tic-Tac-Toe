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

def move():
    player = user_input()
    pc = pc_choice()
    print(pc)