letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
          'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
          'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
          'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caeser(start_text, shifting , cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shifting *= -1
    for character in start_text:
      if character in letters:
        position = letters.index(character)
        new_pos = position + shifting
        pos = letters[new_pos]
        end_text += pos  
      else:
         end_text += character
           
    print(f"The {direction}d is : {end_text}")

wants_continue = True 

while wants_continue:
 
  direction = input("To encrypt give encode, to decode type decrypt : \n")
  plain_text = input("Enter your message : ").lower()
  shift = int(input("Enter the shifting number : "))
  shift = shift % 26

  caeser(start_text = plain_text , shifting = shift , cipher_direction = direction)
 
  final = input("Tap 'yes' if you wifh to continue, otherwise tap 'no'\n")
  if final == "no":
     wants_continue = False
     print("'End'")