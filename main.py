import random

min = 1
max = 6
print("Rolling the dice")
print(random.randint(1, 6))
roll_again = input("Roll again?")

if roll_again == "yes":
    print("Rolling again...")
    print (random.randint(1, 6))
    break


