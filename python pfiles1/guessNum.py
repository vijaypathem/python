from random import randint 
HARD_=5
EASY_=10

def difficulty():
    level=input("select difficulty level easy|hard:\n")
    if (level=="easy"):
        return EASY_
    else:
        return HARD_
#while not guess==answer:

def compare(guess,answer,turns):
    if guess==answer:
        print(f"your correct it is: {answer}")
        return 
    elif guess>answer:
        print("too high")
        return turns-1
    else:
        print("too low")
        return turns-1
def game():
    print("welcome to the guess number game")
    print("I guessed a number from 1 to 100")
    answer=randint(1,100)
    turns=difficulty()
    guess=0
    while guess!=answer:
        print(f"you have {turns} chances left")
        guess=int(input("guess a number"))
        turns=compare(guess,answer,turns)
        if turns==0:
            print("you lost")
            return
        else:
            print("guess again")
game()