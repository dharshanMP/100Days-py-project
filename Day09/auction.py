import os

logo = '''
                         ___________
                         |         |
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         |_________|
                         `'-------'`
                       .-------------.
                      |_______________|
'''                   
print(logo)

print("Let's start the auction")

auction = {}

bid_end = False

def end_auction(highest_lender):
    bids = 0
    winner = ""
    for person in highest_lender:
      amount = highest_lender[person]
      if amount > bids:
        bids = amount
        winner = person   
    print(f"The winner of this auction is {winner} with the amount of rs.{bids}")

    
while not bid_end:
    name = input("what is your name : ")
    bid_price = int(input("how are you biding : "))  
    auction[name] = bid_price
    next_person = input("Is there any other person for biding ? if there tap 'yes' otherwise 'no' : ")
    
    if next_person == "no":
        bid_end = True
        end_auction(auction)
    elif next_person == "yes" :    
        os.system('cls')

    
        

