import string
import random

class PasswordGenerator:
    def __init__(self, length, with_uppercase = False, with_numbers = False, with_special_characters = False):
        self.length = length
        self.with_uppercase = with_uppercase
        self.with_numbers = with_numbers
        self.with_special_characters = with_special_characters

    def generate(self):
        pwd = [random.choice(string.ascii_lowercase)]
        char_pool = string.ascii_lowercase
        if self.with_uppercase:
            pwd.append(random.choice(string.ascii_uppercase))
            char_pool += string.ascii_uppercase
        if self.with_numbers:
            pwd.append(random.choice(string.digits))
            char_pool += string.digits
        if self.with_special_characters:
            pwd.append(random.choice(string.punctuation))
            char_pool += string.punctuation

        if len(pwd) < self.length:
            pwd += random.choices(char_pool, k=(self.length - len(pwd)))

        random.shuffle(pwd)
        return ''.join(pwd)