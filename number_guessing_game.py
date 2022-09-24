import time
import random

print("WELCOME TO NUMBER GUESSING GAME", "YOU HAVE 10 CHANCES", sep='/')


def guessing():
    print("function is working")
    randomNumber = random.randint(1, 1000)
    return randomNumber

machineGuess = guessing()
while True:
    chances = 10

    print("Press q to quit")
    guess = int(input("PLEASE ENTER YOUR GUESS"))
    if (chances <= 0):
        print("your chances are done!!!")
        break
    elif (chances > 0):
        if (guess == "q"):
            print("application is closing...")
            time.sleep(1)
            break
        elif (guess > machineGuess):
                print("YOUR GUESS IS BIGGER THAN EXPECTED OUTPUT")
                chances -= 1
        elif (guess < machineGuess):
                print("YOUR GUESS IS SMALLER THAN EXPECTED OUTPUT")
                chances -= 1
        elif (guess == machineGuess):
                print("*******congratulations******")
        else:
                 print("program is crushed....")
                 break

    else:
        print("application is closing end point...")



