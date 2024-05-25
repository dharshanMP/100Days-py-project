import pandas
alphabet_data = pandas.read_csv("nato_phonetic_alphabet.csv")

file1 =  {row.letter:row.code for (index, row) in alphabet_data.iterrows()}

def generate_phenetic():
    user_input = input("enter the word: ").upper()
    try:
        li = [file1 [letter]for letter in user_input]
    except KeyError:
        print("sorry Alphabet's only allowed")
        generate_phenetic()
    else:    
        print(li)

generate_phenetic()