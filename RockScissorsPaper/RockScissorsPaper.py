"""
Rock-Paper-Scissors game. Each player chooses a move from the choices:
rock, paper or scissors.
If they chose the same move the game is a tie. Otherwise:
rock beats scissors
scissors beats paper
paper beats rock.

In this program a human plays against an AI. The AI chooses randomly.
"""
import random

def main():
    print_welcome()
    n_games = number_of_games()
    print()
    score = 0
    for i in range(n_games):
        human_move = get_human_move()
        ai_move = get_ai_move()
        winner = get_winner(ai_move, human_move)
        print("AI move was", ai_move)
        if winner == "ai" or winner == "human":
            print("Winner was", winner)
        elif winner == "tie":
            print("It was a tie!")
        print()
        score += score_result(winner)
    print("Your score", score)

def number_of_games(): # asks user how many games to play
    while True:
        try:
            n_games = int(input("How many games you want to play? "))
            if n_games > 0:
                return n_games
        except ValueError:
            print("Invalid input. Please enter the number of games you'd like to play. ")
            print()

def score_result(winner):
    if winner == "ai":
        return -1
    elif winner == "human":
        return +1
    else:
        return 0

def get_ai_move(): #gets AI move
    ai_move = random.choice(["scissors", "rock", "paper"])
    return ai_move

def get_human_move(): #gets human move and checks if it's valid
    while True:
        human_move = input("What do you play? ")
        if human_move == 'rock' or human_move == 'scissors' or human_move == 'paper':
            return human_move
        print("Invalid input. \n")

def get_winner(ai_move, human_move): # returns the winner
    if ai_move == human_move:
        return "tie"
    elif ai_move == "rock":
        if human_move == "scissors":
            return "ai"
        elif human_move == "paper":
            return "human"
    elif ai_move == "scissors":
        if human_move == "rock":
            return "human"
        elif human_move == "paper":
            return "ai"
    elif ai_move == "paper":
        if human_move == "scissors":
            return "human"
        elif human_move == "rock":
            return "ai"

def print_welcome():
    print('Welcome to Rock Scissors Paper. You will play against the AI')
    print('rock beats scissors \nscissors beats paper \npaper beats rock')
    print('----------------------------------------------')
    print('')

if __name__ == '__main__':
    main()