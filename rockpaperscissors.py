import random
print("'ROCK PAPER SCISSORS' GAME\n")
print("The game will be of 10 rounds\n")


def get_comp():
    computer = random.choice(['r', 'p', 's'])
    return computer


def get_call():
    user = (input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors: \n"))
    return user


j = 0
k = 0
i = 0
while i < 10:
    i += 1
    a = get_comp()
    b = get_call()
    if a == 'r' and b == 's':
        print("comp choose ROCK, you choose SCISSORS")
        print("comp won\n")
        j += 1
    elif a == 'r' and b == 'p':
        print("comp choose ROCK, you choose PAPER")
        print("you won\n")
        k += 1
    elif a == 's' and b == 'r':
        print("comp choose SCISSORS, you choose ROCK")
        print("you won\n")
        k += 1
    elif a == 's' and b == 'p':
        print("comp choose SCISSORS, you choose PAPER")
        print("comp won\n")
        j += 1
    elif a == 'p' and b == 'r':
        print("comp choose PAPER, you choose ROCK")
        print("comp won\n")
        j += 1
    elif a == 'p' and b == 's':
        print("comp choose PAPER, you choose SCISSORS")
        print("you won\n")
        k += 1
    else:
        print("both choose same")
        print("undecided\n")
print("Game Over\n")
print(f"you won {k} rounds")
print(f"comp won {j} rounds")

