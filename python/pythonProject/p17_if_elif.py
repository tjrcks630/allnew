while True:
    i = input("input the number(p : Quit) : ")

    if i == 'q':
        break

    else:
        if int(i) > 0:
            print("This is positive")
        elif int (i) == 0:
            print("This is zero")
        else:
            print("This is negative")
