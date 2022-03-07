# Write your code here :-)
import os.path
import random
import string

from os import path

print('Create random password')

pass_length = int(input('what is the minimum length required for your password?: '))

passwordIsUsedFor = str(input('What is this password for?:'))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation
all = lower + upper + num + symbols
temp = random.sample(all, pass_length)
password = "".join(temp)

passFileExists = path.exists("passFile.txt")

if passFileExists:
    password_file = open("passFile.txt", "a")
    password_file.write(passwordIsUsedFor.upper() + ": " + password + "\n")
    password_file.close()
else:
    password_file = open("passFile.txt", "w")
    password_file.write(passwordIsUsedFor + ": " + password)
