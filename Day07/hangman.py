points = ['''
     __________
     |/      |
     |      (_)
     |      |||
     |       |
     |      | |
     |
 ____|____

''' , '''
     _________
     |/      |
     |      (_)
     |      |||
     |       |
     |      | 
     |
 ____|____

''', '''
     __________
     |/      |
     |      (_)
     |      |||
     |       |
     |      
     |
 ____|____

 ''', '''         
     __________
     |/      |
     |      (_)
     |      ||
     |       |
     |      
     |
 ____|____

''' , '''

     __________
     |/      |
     |      (_)
     |       |
     |       |
     |      
     |
 ____|____
          
''', '''

     __________
     |/      |
     |      (_)
     |       |
     |       
     |      
     |
 ____|____  

''' , '''
     __________
     |/     |
     |     (_)
     |       
     |       
     |      
     |
 ____|___       
          
''' , '''          
          
     __________
     |/      |
     |      
     |       
     |       
     |      
     |
 ____|____      
          

''', '''
     __________
     |/     
     |       
     |       
     |      
     |
 ____|____      
                   
          ''']



import random 


end = False

words = ["application", "alright", "always", "allotment", "access", "apply", "alert", "alive"
         "bandwagon", "banjo", "bayou, beekeeper", "blitz", "blizzard", "boggle", 
         "bookworm", "boxcar","boxful", "buffalo", "buffoon", "buxom",
         "buzzard", "buzzing", "buzzwords", "clone", "cockiness","club", "crypt", "cycle", 
         "daiquiri", "dam", "drop", "dial", "dynamic" "development", "equip", "elements", "electric", 
         "faking", "fishhook", "fixable", "flopping", "fight", "front", "flate", "fullstack"
         "guts", "good", "god", "gaint", "gossip", "grade", "grape", "graph", "greetings", "handle",
         "happy", "hyper", "hotter", "holding", "happiest", "harvesting", "hard", "hiding", "hunting", 
         "hammer", "iron", "injury", "ivory", "jute", "jumping", "jackpot", "jelly", "jaundice", "javascript"
         "joyful", "joke", "junk", "join", "joining", "know", "knowledge", "knowing", "knight",
         "keying", "key", "knock", "lamping", "lighting", "later", "looking", "lord", "loft", 
         "louder", "lacking", "loading", "matrix", "minimum", "maximum", "maintence", "matching",
         "melting", "nesting", "numbers", "nowdays", "noise", "notes", "nearest", "opposite",
         "opportunity", "oxygen", "ordering", "painting", "pirate", "python", "patterning", 
         "points", "plotting", "prompt", "queue", "quick", "queiting", "qutting", "quzzes",
         "reaction", "rating", "rhythm", "rhyming", "rickshaw", "roots", "random", "scratch", "snapping",
         "shower", "shatter", "solving", "salute", "stack", "storing", "starving","standard", 
         "security", "trucking", "scripting", "softness", "solid", "syntax"
         "trapes", "training", "tractor", "tracking", "troll", "temper", "upside", "upper", 
         "umpiring", "upset", "volting", "voting", "vampire", "varience", "variables", "wlovrine",
         "wanted", "wasted", "welcome", "waiting", "whizzing", "xylophone", "youthful", "zigzag", "zombie" ]

choose_word = random.choice(words)

print("'start'")

display = []
for fill in range(len(choose_word)):
  display += "_"

live = 8

while not end:
  #2
  guess = input("choose a letter : ").lower()

  for position in range(len(choose_word)):
    letter = choose_word[position]
    if letter == guess:
        display[position] = letter

  if guess not in choose_word:

    print(f"letter '{guess}' is not in the word. You lose a life.")

    live -= 1
    if live == 0:
      end = True
      print("#you lose")
      print(f"The word is : {choose_word}")

  print(f"{''.join(display)}")
  
  print(points[live])    

  if "_" not in display:
    end = True
    print("#you win")

  
  
 
  

