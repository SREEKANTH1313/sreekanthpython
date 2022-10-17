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
 

# Output:
# Enter Your Number: 3
# too low
# Enter Your Number: 1
# too low
# Enter Your Number: 2
# too low
# Enter Your Number: 4
# too low
# Enter Your Number: 5
# You won
