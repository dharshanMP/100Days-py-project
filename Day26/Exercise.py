# # squaring the numbers using list comperhension

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [num*num for num in numbers]
# print(squared_numbers)


students = {
    "student" : ["Dharshan",  "Nitheesh", "Praveen", "Elango"],
    "score" : [60, 80, 70, 70]
}

import pandas 
new_df = pandas.DataFrame(students) 
print(new_df)

for (key,value) in new_df.items():
    print(value)
