import pandas
alphabet_data = pandas.read_csv("nato_phonetic_alphabet.csv")

file1 =  {row.letter:row.code for (index, row) in alphabet_data.iterrows()}

user_input = input("enter the word: ").upper()
li = [file1 [letter]for letter in user_input]
print(li)