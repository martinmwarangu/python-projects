import random
def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print("Sorry guess is too low guess again")
        elif guess > random_number:
            print("Sorry guess is too high guess again") 
       
    print("correctamundo")            
guess(100)       
