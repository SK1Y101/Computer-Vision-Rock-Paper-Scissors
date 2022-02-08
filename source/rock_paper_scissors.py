# import required modules
from random import randint
import numpy as np
import math

# return whether the user picked rock, paper, or scissors
def get_rock_paper_scissor():
    # compile a list of allowed choices
    choices = [["1", "rock", "r"],
               ["2", "paper", "p"],
               ["3", "scissors", "s", "scissors"]]
    # keep looping until we have chosen an appropriate response
    while True:
        # fetch the users choice, ensuring it is lowercase
        selected = input("Make your choice:\n1) Rock\n2) Paper\n3) Scissors\n> ").lower()
        # check if the input contains a valid portion
        valid = [ selected in choice for choice in choices ]
        # if we had a single match
        if valid.count(True) == 1:
            # then return the users selection
            return valid.index(True)

# play a round of rock paper scissors
def play_round():
    outputs = ["Rock", "paper", "Scissors"]
    # select the computers choice
    computer_choice = randint(0, 2)
    # fetch the users choice
    user_choice = get_rock_paper_scissor()
    # show the user the responses
    print("Computer: {}\nYou:      {}\n".format(outputs[computer_choice], outputs[user_choice]))
    # compare the responses
    result = math.fmod(computer_choice - user_choice, 3)
    # determine who won!
    if result == 0:
        # the round is a draw if they chose the same
        print("That round was a draw!")
        return np.array([0, 0])
    elif result == 1:
        # the computer won if it chose the answer to the right of the user in our cyclic set
        print("The computer won that round!")
        return np.array([1, 0])
    else:
        # the user won if it chose the answer to the left of the computer in our cyclic choice set
        print("You won that round!")
        return np.array([0, 1])

# main program script
def main():
    # track the cumulative score, stored as an array of [comp, user]
    score = np.array([0, 0])
    # track the win condition
    win_score = 0
    # ask the user to select the wining score
    while win_score < 1:
        try:
            # fetch the users choice
            win_score = int(input("At what score should a winner be declared?\n> "))
        # if they didn't choose a valid integer, this exception block will catch it
        except:
            print("That was not a valid choice I'm afrad")
    # add a break to the output
    print()
    # while noone has won the game, loop
    while not win_score in score:
        # play a round and fetch the score
        score += play_round()
        # show the score
        print("The current score is:\nComputer: {}\nYou:      {}\n".format(*score))
    # determine which part of the score array has a win condition
    winner = np.where(score==win_score)[0][0]
    # tell the user if they have won or not
    print("{}, you have {} the game!".format("Congratulations" if winner else "Commiserations",
                                             "won" if winner else "lost"))

# ensure this is the top level script
if __name__ == "__main__":
    main()