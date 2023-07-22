# Example code 1

number = 7
#variable assigned
print("I have thought of a number between 1 and 10")
#string gets printed
guess = int(input("Can you guess what it is?"))
#string is printed and user inputs their guess
if guess == number:
  print("Correct!")
#if their guess is the number, string would print correct
elif guess < number:
  print("Too Low!")
#if their guess is less than the number, string would print too low
else:
  print("Too High!")
#if their guess is greater than the numberm string would print too high
# Example code 2

number1 = int(input("Please enter a number"))
#string is printed and user inputs their first number
number2 = int(input("Please enter another number"))
#string is printed and user inputs their second number
if number1 > number2:
  print("Number 1 is bigger than number 2")
#If their first number is greater than their second number this string would be printed
elif number2 > number1: 
  print("Number 2 is bigger than number 1")
#If their second number is greater than their first number this string would be printed
else:
  print("Both numbers are the same")
#If they are equal then this string would be printed
