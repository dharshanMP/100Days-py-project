name_replacer = "[name]"


with open("/Users/Admin/OneDrive/Desktop/100Days-py-project/Day24/names/names.txt") as name_file:
    names = name_file.readlines()
    print(names)

s_letter = open("/Users/Admin/OneDrive/Desktop/100Days-py-project/Day24/letter/main_letter.txt")
letter_content = s_letter.read()
for name in names:
    strip_name = name.strip()
    new_letters = letter_content.replace(name_replacer, name)
    with open(f"/Users/Admin/OneDrive/Desktop/100Days-py-project/Day24/send_to/letter_to_{strip_name}.txt", mode = "w") as letters:
        letters.write(new_letters)
