import random

def layout():
    for row in range(3):
        for col in range(3):
            print("_",end="")
            if col != 2:
                print(" | ", end="")
        print()

def user_input():
    user_choice = input("Enter the number of your choice (1-9) : ")
    return int(user_choice)

def pc_choice():
    pc_choice = random.randint(0,9)
    return pc_choice

def move():
    player = user_input()
    pc = pc_choice()
    print(pc)