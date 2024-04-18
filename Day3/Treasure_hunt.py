print("Welcome to Isalnd of 'Treasure Trove' ")
print("Let's enter the game")
way = input("Dense forest or Rain forest : ")

def dense():
    if way == "Dense forest" : 
        print("you entered into dense forest")
        print("left <--- cave , right ---> river")
        di = input(" enter the direction left or right : ")
        if di =="left" and di != "river":
            print("It's more dark")
            print("There is an big rock in the way, sorry ended")
        elif di == "right" and di != "cave":
            print("It's an river")     
            print("There is an Gaint sequoia, contains 'X' Mark underit. ")
            print("Congarts you had won the game")
            print(r'''
                            _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
            ___ '-._'-.|| |' `_.-'
                    '-.||_/.-' 

''')
    elif way == "rain forest":
        print("you had entered the Rain forest")
        di1 = input(" enter the direction left or right : ")
        
        if di1 == "left" :   
            print("Full of wet mud can't go, sorry game ended")
        elif di1 == "right":
            print("restricted area because of more snakes are there, sorry game ends")                  





dense()
        
            