import random
import string

lowercase_letters = list(string.ascii_lowercase)
uppercase_letters = list(string.ascii_uppercase)
digits = list(string.digits)
symbols = list(string.punctuation)

all_characters = 


def generate(password_length: int):
    length = int(input("Input the desired length of your password: "))
    char_list = []
    for i in range(length):
        char_list.append("")
