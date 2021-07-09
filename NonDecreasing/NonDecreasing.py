'''
Program asks the user to enter a sequence of "non-decreasing"
numbers one at a time. When the user enters a number which is smaller
than their previously entered value, the program is over.
Program tells the user how long their sequence was.
'''
def main():
    print("Enter a sequence of non-decreasing numbers. ")
    num1 = int(input("Enter num: "))
    num2 = int(input("Enter num: "))
    length = 0
    while num2 > num1:
        num1 = int(input("Enter num: "))
        length +=1
        if num1 > num2:
            num2 = int(input("Enter num: "))
            length += 1
        else:
            break
    print("Thanks for playing!")
    print("Sequence length:", length)


if __name__ == "__main__":
    main()