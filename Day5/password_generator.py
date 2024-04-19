import random
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q",
            "r", "s", "t", "u", "v", "w", "x", "y", "z"]
num = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
symbols = ["*", "#", "_", "()", "&", "%", "$", "@", "!", "+"]
le = int(input("enter how many letters you want : "))
nu = int(input("enter how many numbers you need in : "))
sy = int(input("enter how many symbols you need : "))

password = []

for pas in range (1, le+1):
     password.append(random.choice(letters))

for pas in range (1, sy+1):
     password += random.choice(symbols)

for pas in range (1, nu+1):
     password += random.choice(num)

random.shuffle(password)

new_password = ""
for pas in password:
     new_password += pas

        
print(f"New password is {new_password}")       