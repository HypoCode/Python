# 2 Guessing games - Solo, Vs
from time import sleep as wait  # Import modules
import random as rd, Colors  # Import modules


def solo():  # create the solo game-mode
    target_num = rd.choice(range(1, 100))  # create the random target number
    p_guesses = 0  # number of guesses that player has made
    p_guess = 0  # player guess
    location = None  # location variable
    print("\n\nLoading..\n")
    wait(2)  # wait 2 seconds
    p_guess = input("Im thinking of a number between 1 and 100, what am I?\nguess: ")  # guess the target number
    if not p_guess.isdigit():
        print(Colors.RED + "\n" + f"*" * 5 + "Invalid input" + f"*" * 5 + Colors.END)  # dummy proof (:
        exit()
    elif int(p_guess) not in range(1, 100):
        print(Colors.RED + "\n" + f"*" * 5 + "Invalid input" + f"*" * 5 + Colors.END)  # dummy proof (:
        exit()
    while True:
        p_guesses = p_guesses + 1  # add one to the players guesses

        if int(p_guess) == target_num:
            print(Colors.YELLOW + "\n" + f"*" * 5 + f"Winner, in {p_guesses} tries" + f"*" * 5 + Colors.END)
            exit()  # end program
        else:
            if int(p_guess) < target_num:  # if under the target
                location = "under"
            elif int(p_guess) > target_num:  # if over the target
                location = "over"
            print(f"Your guess is {location} the target guess.")  # print the player's guess location
            p_guess = input(f"Take your next guess\nguess: ")  # guess the target number
            if not p_guess.isdigit():
                print(Colors.RED + "\n" + f"*" * 5 + "Invalid input" + f"*" * 5 + Colors.END)  # dummy proof (:
                exit()
            elif int(p_guess) not in range(1, 100):
                print(Colors.RED + "\n" + f"*" * 5 + "Invalid input" + f"*" * 5 + Colors.END)  # dummy proof (:
                exit()


def vs():  # create the vs game-mode
    print("\n\nLoading..\n")
    wait(2)  # wait 2 seconds
    target_num = rd.choice(range(1, 100))  # create the random target number
    p_guesses = 0  # number of guesses that player has made
    p_guess = 0  # player guess
    b_guesses = 0
    b_guess = 0
    bwn_guess = [4, 5, 6]  # initialize the possible number it takes for the bot to win
    location = None  # location variable
    b_location = None
    p_guess = input("Im thinking of a number between 1 and 100, what am I?\nguess: ")  # guess the target number
    if not p_guess.isdigit():
        print(Colors.RED + "\n" + f"*" * 5 + "Invalid input" + f"*" * 5 + Colors.END)  # dummy proof (:
        wait(1)
        exit()
    elif int(p_guess) not in range(1, 100):
        print(Colors.RED + "\n" + f"*" * 5 + "Invalid input" + f"*" * 5 + Colors.END)  # dummy proof (:
        wait(1)
        exit()
    b_guess = rd.choice(range(1, 100))  # choose a random number from 1 to 100
    wait(2)  # wait 2 seconds
    print("bot made his first guess.\n")
    while True:
        p_guesses = p_guesses + 1  # add one to the player's guesses
        b_guesses = b_guesses + 1  # add one to the bots guesses

        if int(p_guess) == target_num:
            print(Colors.YELLOW + "\n" + f"*" * 5 + f"You won in {p_guesses} tries" + f"*" * 5 + Colors.END)
            wait(1)
            exit()  # end program
        elif int(b_guess) == target_num:
            print(Colors.RED + "\n" + f"*" * 5 + f"The bot won in {b_guesses} tries with the number {target_num}" + f"*" * 5 + Colors.END)
            wait(1)
            exit()  # end program
        else:
            if int(p_guess) < target_num:  # if under the target
                location = "under"
            elif int(p_guess) > target_num:  # if over the target
                location = "over"

            if int(b_guess) < target_num:  # if bot under the target
                b_location = "under"
            elif int(b_guess) > target_num:  # if bot over the target
                b_location = "over"

            print(f"Your guess is {location} the target guess.")  # print the player's guess location
            print(f"Bots guess was {b_guess} and was {b_location} the target number.")
            p_guess = input(f"Take your next guess\nguess: ")  # guess the target number
            if not p_guess.isdigit():
                print(Colors.RED + "\n" + f"*" * 5 + "Invalid input" + f"*" * 5 + Colors.END)  # dummy proof (:
                wait(1)
                exit()
            elif int(p_guess) not in range(1, 100):
                print(Colors.RED + "\n" + f"*" * 5 + "Invalid input" + f"*" * 5 + Colors.END)  # dummy proof (:
                wait(1)
                exit()
            else:
                if b_guesses == rd.choice(bwn_guess):
                    b_guess = target_num
                else:
                    b_guess = rd.choice(range(1, 100))  # randomly chooses bots guess again
                    wait(2)
                    print("Bot just made his next guess.\n")


# start
print(Colors.GREEN + "Let's play one of two games.\n" + Colors.END + Colors.RED +
      "In game one, you test how many guesses\nit takes you until you find the "
      "random\nnumber, between 1 and 100.\n" + Colors.END + Colors.BLUE +
      "game two, you test who can get \nthe random number faster, "
      "you or a bot.\n" + Colors.END)  # explain the game

st = input(str('To choose, enter [1] for "Game one" and enter [2] for "Game two"\nGame: '))  # Choose game-mode

if st == "1":
    solo()  # run the game-mode
elif st == "2":
    vs()  # run the game-mode
else:
    print(Colors.RED + "\n" + f"*" * 5 + "Invalid input" + f"*" * 5 + Colors.END)  # dummy proof (:
    wait(1)
    exit()
