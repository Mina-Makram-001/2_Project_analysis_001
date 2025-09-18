#encrypt my password

import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()
random.shuffle(key)

print(f"chars: {chars}")
print(f"keys: {key}")

my_password=input("inter your password : ")
incrypted_password=""

for litter in my_password:
    index=chars.index(litter)
    incrypted_password+=key[index]

print(f"my password : {my_password} ")
print(f"my encryoted password : {incrypted_password} ")



