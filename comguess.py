# GUESSING GAME
""" In this game computer will guess the number which is secret number of user within certain range,
       for every guess you have to provide feedback about computer's guess """
import random


def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f"Is guess {guess} too high(H), too low(L), or correct(C): ").lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1

    print(f"Congratulations, You have guessed the number right. The number is {guess}")


if __name__ == '__main__':
    print("WELCOME to NUMBER GUESSING GAME\n")
    computer_guess(200)
