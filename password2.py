import random
import string
import inquirer
import os

lowercase_letters = list(string.ascii_lowercase)
uppercase_letters = list(string.ascii_uppercase)
digits = list(string.digits)
special_characters = ['!', '#', '$', '%', '&', '(', ')', '*', '+', ',', '-', '=', '?', '@', '[', ']', '^', '_', '`', '{', '}', '~']

all_characters = {"Lowercase Letters": lowercase_letters, "Uppercase Letters": uppercase_letters, "Numbers": digits, "Symbols": special_characters}
#print(all_characters)

def generate(password_length: int):
    questions = [
    inquirer.Checkbox('selection',
                        message="Make your selection of what types of characters youd like in your password: ",
                        choices=["Lowercase Letters", "Uppercase Letters", "Numbers", "Symbols"]
                        ),
    ]
    answers = inquirer.prompt(questions)
    #(answers["interests"])
    user_selection = []
    char_list = []
    for i in answers["selection"]:
        for x in all_characters:
            if i == x:
                user_selection.extend(all_characters[x])
                #print(user_selection)

    for u in range(password_length):
        char_list.append(random.choice(user_selection))
    final_password = "".join(char_list)
    print("Your password is: " + final_password)

def get_length():
    global length
    length = int(input("Input the desired length of your password: "))



if __name__ == "__main__":
    get_length()
    generate(length)
