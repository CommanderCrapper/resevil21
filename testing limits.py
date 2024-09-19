import random

randomNum = random.randrange(0,10)
if randomNum != 10:
    while(randomNum != 10):
        randomNum = random.randrange(0,10)
        print(randomNum)
print(randomNum)