#hello world
print("Hello User")
print("You will be set a secret number that is not shown to you ")
print("You will have to guess the number ")

import random 
random_integer=random.randint(1, 10)


for i in range(3):
    user_input=int(input(""))
