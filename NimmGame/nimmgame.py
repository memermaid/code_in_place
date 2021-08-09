def main():
    stones = 20
    turn = 1

    while stones > 0:
        if turn == 1:
            print('Player 1')
            amount = askforinput()
            stones -= amount
            turn += 1
            print(f"There are {stones} stones left.\n")
        elif turn == 2:
            print("Player 2")
            amount = askforinput()
            stones -= amount
            print(f"There are {stones} stones left.\n")
            turn -= 1
    if turn == 1:
        print("Player 1 won!")
    else:
        print("Player 2 won!")        

def askforinput():
    while True:
        try:
            msg = int(input('Would you like to remove 1 or 2 stones? '))
            if msg == 1 or msg == 2:
                break
        except ValueError:
            print("Invalid input.")
    return msg





if __name__ == '__main__':
    main()
