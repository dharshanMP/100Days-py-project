import random as rd
from game_data import data as dt

random_a = rd.choice(dt)
random_b = rd.choice(dt)

def details():
    name_a = random_a["name"]
    description_a = random_a["description"]
    country_a = random_a["country"] 
    print(f"(a) {name_a} an {description_a} from {country_a}")

    print(r''' 
              \ \ / / __|
               \ V /\__ \
                \_/ |___/ ''')
    
    name_b = random_b["name"]
    description_b = random_b["description"]
    country_b = random_b["country"]
    print(f"(b) {name_b} an {description_b} from {country_b}")

    return random_a,random_b

def camparing(a,b):   
    if a["follower_count"] > b["follower_count"]:
        return "a"
    elif a["follower_count"] < b["follower_count"]:
        return "b" 
    else :
        print("both A & B are tie")


def game():
    score = 0
    while True:
        random_a,random_b = details()
        user_choice = input("If option(a) type 'a' or option(b) type 'b' : ").lower()
        
        result = camparing( random_a,  random_b)

        if result == user_choice:
            score += 1 
            print("you'r correct")
            print(f"your current score is {score}")    
        else:
            print("you'r wrong try again!....")
            again = input("if you want to try again give 'yes', or give 'no' : ").lower()
            if again == "yes":
                print("let's play")
                game() 

            else : 
                print(r'''
                         __ _____________ _________     
                        / // /  _/ ___/ // / __/ _ \    
                       / _  // // (_ / _  / _// , _/    
                      /_//_/___/\___/_//_/___/_/|_|____ 
                             / /  / __ \ | /| / / __/ _ \
                            / /__/ /_/ / |/ |/ / _// , _/
                           /____/\____/|__/|__/___/_/|_| 
                                  ''')
                print(f"'you'r final score is {score}'")  
                break

game()

