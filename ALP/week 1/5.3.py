# Starter Code

number = 5
# 5 is assigned to the variable "number" 
print("I have thought of a number between 1 and 10")
#The text would print that I have thought of a number between 1 and 10
guess = int(input("Can you guess what it is?"))
# The code requires and input to see if the guess is correct


if guess < number:
  print("Too Low!")
# If the guess is less than it would print too low
if guess > number:
  print("Too High!")
#if the guess is greater than it would print too high
