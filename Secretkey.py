import random
secret_key = random.randint(1, 10)
num = 0
while True:
    guess = int(input("Enter Your Number: "))
    if guess < secret_key:
        print("too low")
    elif guess == secret_key:
        print("You won")
        break
    else:
        print("Too high")
