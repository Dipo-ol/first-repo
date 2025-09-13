import random
num = random.randint(1, 10)
guess = 0
tries = 0
print("Welcome to the random number guesser!!")
while guess != num and tries <= 5:
    guess = int(input("guess the number "))
    tries += 1
    if guess > num:
        print("too high")
    elif guess < num:
        print("too low")
if tries == 5:
    print("5 tries reached , round over")
elif guess == num:
    print("you won!")
