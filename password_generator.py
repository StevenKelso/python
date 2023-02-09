#!/usr/bin/env python3

import string
import secrets

password_length = int(input("How many characters do you want in each password: "))
password_count = int(input("How many passwords do you want to generate: "))


available = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

for x in range(0,password_count):
    password = ""
    for x in range(0,password_length):
        random_character = secrets.choice(available)
        password = password + random_character
    print("Your password is: ", password)
