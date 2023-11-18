import random
i = 1 # counter to keep  track of guesses
j = 0 # to set up a while loop
goal = random.randint(1, 10000)

guess = int(input("Guess what number (1 - 10000) I'm thinking of! "))

while j == 0:
    if guess == goal and i == 1:
        print("You got it in 1 guess!")
        j += 1

    elif guess == goal and i != 1:
        print("You got it in " + str(i) + " guesses!")
        j += 1

    elif guess < goal:
        i += 1
        print("Higher!")

    else:
        i += 1
        print("Lower!")

    if j == 0:
        guess = int(input("Try again! "))
