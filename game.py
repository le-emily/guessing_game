"""A number-guessing game."""

import random
import sys

# Put your code here
name = raw_input("What's your name? ")
print "Hi there, %s!" % (name.title())

scores_dict = {}

def guess_number(lowest_num_guess=11, best_score=1):
    guess = 0
    number_of_guesses = 0.0
    beg_range = int(raw_input("What is the beginning of your range? "))
    end_range = int(raw_input("What is the ending of your range? "))
    secret_number = random.randint(beg_range, end_range)
    while guess != secret_number and number_of_guesses < 6:
        number_of_guesses += 1
        try:
            guess = int(raw_input("Guess a number between " + str(beg_range) + " and " + str(end_range) + ": "))
            if guess not in range(beg_range, end_range+1):
                print "Can you count? That's not in range."
            elif guess > secret_number:
                print "Too high!"
            elif guess < secret_number:
                print "Too low!"
            else:
                print "You got it in " + str(number_of_guesses) + " tries!!"
                value = float(number_of_guesses/(end_range-beg_range))
                # append to list
                score_value.append(value)
                initials = raw_input("What are your initials? ")
                scores_dict[initials] = score_value
                print scores_dict
                # keep track of lowest_num_guess
                if number_of_guesses < lowest_num_guess:
                    lowest_num_guess = number_of_guesses
                # get best score of all user's games
                if value < best_score:
                    best_score = value
                play_again(lowest_num_guess, best_score)
        except ValueError:
            print "That's not a number."
        if number_of_guesses == 5:
                print "Sorry you have no more tries"
                play_again(lowest_num_guess, best_score)

# name of argument in play_again just represents the variable passed above in guess_number
def play_again(lowest_num_guess, best_score):
    again = raw_input("Would you like to play again? (Y or N) ").upper()
    if again == "Y":
        guess_number(lowest_num_guess, best_score)
    else:
        print "Thank you for playing! Here is your score history: "
        print scores_dict
        print "Your lowest number of guesses was " + str(lowest_num_guess) + " tries."
        print "Your best game had a difficulty score of " + str(best_score) + "!"
        # exit instead of break?
        sys.exit()

guess_number()
