def layout():
    for row in range(3):
        for col in range(3):
            print("_",end="")
            if col != 2:
                print(" | ", end="")
        print()
