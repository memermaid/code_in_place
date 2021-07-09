"""
Program randomly generates a simple addition problem for the user
until the user has gotten 3 problems correct in a row.
"""

import random

def main():
    correct = 0
    while correct != 3:
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        total = num1 + num2
        print("What is", num1, "+", num2, "?")
        answer = int(input("Your answer: "))
        if answer == total:
            correct += 1
            print("Correct! You've gotten {} correct in a row.".format(correct))
            if correct == 3:
                print("Congratulations! You mastered addition.")
        else:
            print("Incorrect. The expected answer is", total)
            correct = 0


if __name__ == '__main__':
    main()