#Number Guessing Game Objectives:
import random as rd
print(r'''      
   ___                     _             
  / _ \_   _  ___  ___ ___(_)_ __   __ _ 
 / /_\/ | | |/ _ \/ __/ __| | '_ \ / _` |
/ /_\\| |_| |  __/\__ \__ \ | | | | (_| |
\____/ \__,_|\___||___/___/_|_| |_|\__, |
                                   |___/''')
e_attempt = 10
h_attempt = 5
answer = rd.randint(1, 100)

def checking(user_guess, answer, attempt):
    if user_guess > answer:
        print("Too high")
        return attempt - 1
    elif user_guess < answer :
        print("Too low")
        return attempt - 1
    else :
        print(f"you have done it!.... Answer is {answer}")

def levels():
    level = input("choose the level to play, if easy level give 'e' or high level 'h' : ")
    if level == "e":
        return e_attempt
    else :
        return h_attempt

def game():
    print("let's play the number guessing game.....")
    print("I am thinking an number b/w 1 - 100 try to find it out...")    
   # print(f"The correct answer is {answer}")
    
    attempt = levels()
    
    user_guess = 0
    while user_guess != answer:
        print(f"you have only {attempt} attempts to guess the number. ") 

        user_guess = int(input("enter the guessing number : "))
        attempt = checking(user_guess, answer, attempt)
        if attempt == 0:
            print("you had out of attempts to guess. you lose....")
        elif user_guess != answer:
            print("Try to guess again....")    


game()