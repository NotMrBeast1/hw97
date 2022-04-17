import random
name = input("Please enter your name:- ")
print("Hello " + name + ", Thank you for downloading our game: THE NUMBER GUESSER, let's start the game......")
number=random.randint(1,9)
chance=0
print("Guess a number between one and nine")
while chance < 5:
    guess = int(input("Enter your guess here:- "))
    if guess == number:
        print("You Win, WooHoo you are the winner...")
        break
    elif guess < number:
        print ("Your guess is low, try a number higher than" ,guess)
    else:
        print("Your guess was too high, try a number higher than", guess)
    chance = chance+1
if not chance < 5:
    print("U lose. Play a new game...")
    
    
