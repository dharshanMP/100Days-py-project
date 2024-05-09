import os
print('''
 _____________________
|  _________________  |
| |                 | |                     
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
''') 
def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def multi(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

def calculator_function():
    def cal(n1, n2, operator):
        if operator == "+":
            return add(n1, n2)
        elif operator == "-":    
            return sub(n1, n2)
        elif operator == "*":  
            return multi(n1, n2)
        elif operator == "/":    
            return div(n1, n2)

    
    To_continue = True
    result = 0  
    while To_continue:
        if result == 0:
            n1 = int(input("Enter the 1st number : ")) 
        else:
            n1 = result  
        operator = input("Which operand you need (+ - * /): ")
        n2 = int(input("Enter the next number : "))

        result = cal(n1, n2, operator)
        print(f"{n1} {operator} {n2} = {result}")

        n = input("If you need to continue with another calculation, type 'yes', otherwise type 'no': ")
        if n.lower() != "yes":
            To_continue = False
            os.system('cls') 
            calculator_function()
        else:
            os.system('cls')  
calculator_function()  
         