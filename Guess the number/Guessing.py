# ---imports---
from time import sleep as wait 
import random as rd, Colors  


# ---solo gamemode---
def solo():
    target_num = rd.choice(range(1, 100)) 
    p_guesses = 0   
    location = None 
    print("\n\nLoading..\n")
    wait(2) 
    p_guess = input("Im thinking of a number between 1 and 100, what am I?\nguess: ") 
    if not p_guess.isdigit():
        print(Colors.RED + "\n" + f"*" * 5 + "Invalid input" + f"*" * 5 + Colors.END)  # dummy proof (:
        wait(1)
        exit()
    elif int(p_guess) not in range(1, 100):
        print(Colors.RED + "\n" + f"*" * 5 + "Invalid input" + f"*" * 5 + Colors.END)  # dummy proof (:
        wait(1)
        exit()
    while True:
        p_guesses = p_guesses + 1
        if int(p_guess) == target_num:
            print(Colors.YELLOW + "\n" + f"*" * 5 + f"Winner, in {p_guesses} tries" + f"*" * 5 + Colors.END)
            wait(1)
            exit()  # end program
        else:
            if int(p_guess) < target_num:  
                location = "under"
            elif int(p_guess) > target_num: 
                location = "over"
            print(f"Your guess is {location} the target guess.") 
            p_guess = input(f"Take your next guess\nguess: ")  
            if not p_guess.isdigit():
                print(Colors.RED + "\n" + f"*" * 5 + "Invalid input" + f"*" * 5 + Colors.END)  # dummy proof (:
                wait(1)
                exit()
            elif int(p_guess) not in range(1, 100):
                print(Colors.RED + "\n" + f"*" * 5 + "Invalid input" + f"*" * 5 + Colors.END)  # dummy proof (:
                wait(1)
                exit()


# ---vs gamemode---
def vs():
    print("\n\nLoading..\n")
    wait(2)  # wait 2 seconds
    target_num = rd.choice(range(1, 100)) 
    p_guesses = 0  
    b_guesses = 0
    bwn_guess = [4, 5, 6]  
    location = None 
    b_location = None
    p_guess = input("Im thinking of a number between 1 and 100, what am I?\nguess: ")  
    if not p_guess.isdigit():
        print(Colors.RED + "\n" + f"*" * 5 + "Invalid input" + f"*" * 5 + Colors.END)  # dummy proof (:
        wait(1)
        exit()
    elif int(p_guess) not in range(1, 100):
        print(Colors.RED + "\n" + f"*" * 5 + "Invalid input" + f"*" * 5 + Colors.END)  # dummy proof (:
        wait(1)
        exit()
    b_guess = rd.choice(range(1, 100))  # choose a random number from 1 to 100
    wait(2) 
    print("bot made his first guess.\n")
    while True:
        p_guesses = p_guesses + 1 
        b_guesses = b_guesses + 1 

        if int(p_guess) == target_num:
            print(Colors.YELLOW + "\n" + f"*" * 5 + f"You won in {p_guesses} tries" + f"*" * 5 + Colors.END)
            wait(1)
            exit()
        elif int(b_guess) == target_num:
            print(Colors.RED + "\n" + f"*" * 5 + f"The bot won in {b_guesses} tries with the number {target_num}" + f"*" * 5 + Colors.END)
            wait(1)
            exit() 
        else:
            if int(p_guess) < target_num:  
                location = "under"
            elif int(p_guess) > target_num:  
                location = "over"

            if int(b_guess) < target_num:  
                b_location = "under"
            elif int(b_guess) > target_num:  
                b_location = "over"

            print(f"Your guess is {location} the target guess.")  
            print(f"Bots guess was {b_guess} and was {b_location} the target number.")
            p_guess = input(f"Take your next guess\nguess: ")  
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
                    b_guess = rd.choice(range(1, 100)) 
                    wait(2)
                    print("Bot just made his next guess.\n")


# ---start---
print(Colors.GREEN + "Let's play one of two games.\n" + Colors.END + Colors.RED +
      "In game one, you test how many guesses\nit takes you until you find the "
      "random\nnumber, between 1 and 100.\n" + Colors.END + Colors.BLUE +
      "game two, you test who can get \nthe random number faster, "
      "you or a bot.\n" + Colors.END)  

st = input(str('To choose, enter [1] for "Game one" and enter [2] for "Game two"\nGame: ')) 

# ---Run game---
if st == "1":
    solo()  
elif st == "2":
    vs()  
else:
    print(Colors.RED + "\n" + f"*" * 5 + "Invalid input" + f"*" * 5 + Colors.END)  # dummy proof (:
    wait(1)
    exit()
