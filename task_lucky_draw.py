import random

num=random.randint(1,20)

while True:
    guess=int(input("Guess a number between 1-20 : "))
    if guess==num:
        print("Correct Answer")
        break
    elif guess>num:
        print("Guess smaller number")
    elif guess<num:
        print("Guess Greater number")
