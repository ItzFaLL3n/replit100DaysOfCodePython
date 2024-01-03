print("Guess the Number")
print("Guess a number between 1 and 1,000,000 and I will tell you if you are too low, too high, or get it correct.")
print()
print("Let's play!")

number = 600000
attempt  = 1

while True:
  guess = int(input("Pick a number between 1 and 1,000,000: "))
  if guess < 0:
    print("Now we'll never know what the answer is …")
    exit()
  if guess < number:
    print("Too low, Try again!")
    attempt  +=1
  elif guess > number:
    print("Too high, Try again!")
    attempt  +=1
  elif guess == number:
    print("You got it, Let's Goo 🏆")
    break
    attempt  +=1
  else:
    print("That is not a number I recognize.")
print("It took you", attempt , "guesses")