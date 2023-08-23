import random


num = random.randrange(1, 101)
range1 = range(1, 101)
usernum = int(input("Guess a number between 1 and 100:  "))

if usernum in range1:
    while a != num:
        if a > num:
            print("down")
            a = int(input("try again:  "))
        elif a < num:
            print("up")
            a = int(input("try again:  "))
        if not a != num:
            print("You got it!")
            break
else:
    a = int(input("Guess a number between 1 and 100:  "))
