import random as rd

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

Paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

Scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''
game = [rock, Paper, Scissors]

player = int(input("0 - rock, 1 - paper, 2 - scissor : "))
if player >=3 or player < 0 :
    print("invalid number for the game")
else:
    
    print(game[player])
    computer = rd.randint(0,2)
    print(f"computer is {computer}")
    print(game[computer])

    if player == 0 and computer == 2:
        print("you win.....")
    elif computer == 0 and player == 2:
        print("you lose.....")        
    elif computer > player:
        print("you lose.....") 
    elif player > computer :
        print("you win.....")  
    elif player == computer:
        print("game is draw.....")          
        

