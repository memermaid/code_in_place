def main():
    stones = 20

    while stones >= 3:
        p1 = int(input('Player 1 would you like to remove 1 or 2 stones? '))
        stones -= p1
        print(f"There are {stones} stones left.")
        p2 = int(input('Player 2 would you like to remove 1 or 2 stones? '))
        stones -= p2
        print(f"There are {stones} stones left.")

    p1 = int(input('Player 1 would you like to remove 1 or 2 stones? '))
    stones -= p1

    if stones == 0:
        print("Player 2 won!")
    elif stones < 0:
        print("You can't take more stones that there are available.")
        p1 = int(input('Player 1 would you like to remove 1 or 2 stones? '))
        stones -= p1
    else:
        p2 = int(input('Player 2 would you like to remove 1 or 2 stones? '))
        stones -= p2
        if stones == 0:
            print("Player 2 won!")
        elif stones < 0:
            print("You can't take more stones that there are available.")









if __name__ == '__main__':
    main()