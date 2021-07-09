"""
Rock-Paper-Scissors game!
Each player chooses a move from the choices:
rock, paper or scissors.
If they chose the same move the game is a tie. Otherwise:
rock beats scissors
scissors beats paper
paper beats rock.

In this program a human plays against an AI. The AI chooses randomly.
"""
import random

N_GAMES = 3


def main():
    print_welcome()
    score = 0
    for i in range(N_GAMES):
        human_move = get_human_move()
        ai_move = get_ai_move()
        winner = get_winner(ai_move, human_move)
        print("AI move was", ai_move)
        print("Winner was", winner)
        print()
        score += score_result(winner)
    print("Your score", score)


def score_result(winner):
    score = 0
    if winner == "ai":
        return -1
    elif winner == "human":
        return +1
    else:
        return 0


def get_ai_move():
    ai_move = random.choice(["scissors", "rock", "paper"])
    return ai_move


def get_human_move():
    while True:
        human_move = input("What do you play? ")
        if is_valid_move(human_move):
            return human_move
        print("Invalid input.")


def is_valid_move(move):
    """
    parameter move: string representing what the user entered
    return: boolean which is True, if the move was valid
    Doctest:
    >>> is_valid_move('rock')
    True
    >>> is_valid_move('paper')
    True
    >>> is_valid_move('unicorn')
    False
    """

    if move == 'rock':
        return True
    elif move == 'scissors':
        return True
    elif move == 'paper':
        return True
    return False


def get_winner(ai_move, human_move):
    """
    Returns the winner depends on who won
    Doctest:
    >>> get_winner(rock, paper)
    "human"
    >>> get_winner(rock, scissors)
    "ai"
    >>> get_winner(rock, rock)
    "tie"
    """

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
    print('Welcome to Rock Paper Scissors')
    print('You will play ' + str(N_GAMES) + ' games against the AI')
    print('rock beats scissors')
    print('scissors beats paper')
    print('paper beats rock')
    print('----------------------------------------------')
    print('')


if __name__ == '__main__':
    main()