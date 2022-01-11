import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!%^(;')"

while 1:
    password_len = int(input("Enter password length: "))
    password_count = int(input("How many passwords?:"))
    for x in range(0,password_count):
        password  = ""
        for x in range(0,password_len):
            password_char = random.choice(chars)
            password      = password + password_char
        print("New Password: ", password)
