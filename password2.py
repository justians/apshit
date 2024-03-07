import random
import string
import inquirer

lowercase_letters = list(string.ascii_lowercase)
uppercase_letters = list(string.ascii_uppercase)
digits = list(string.digits)
special_characters = list(string.punctuation)

all_characters = {"Lowercase Letters": lowercase_letters, "Uppercase Letters": uppercase_letters, "Numbers": digits, "Symbols": special_characters}
#print(all_characters)

def generate(password_length: int):
    questions = [
    inquirer.Checkbox('interests',
                        message="Make your selection of what types of characters youd like in your password: ",
                        choices=["Lowercase Letters", "Uppercase Letters", "Uppercase Letter", "Symbols"]
                        ),
    ]
    answers = inquirer.prompt(questions)
    char_list = []
    for i in range(length):
        char_list.append(random.choice(all_characters))
    print("".join(char_list))

length = int(input("Input the desired length of your password: "))
generate(length)
