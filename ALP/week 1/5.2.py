'''
Task - Investigate
Use comments to answer the investigate questions on the example code.

'''
# Example Code

number = 5
print("I have thought of a number between 1 and 10")
guess = int(input("Can you guess what it is?"))

if guess == number:
  print("Correct!")
if guess < number:
  print("Too Low!")
if guess > number:
  print("Too High!")

# What happens if you input the guess '2'?
  # Answer It would print Too low

# What happens if you input the guess '6'?
  # Answer It would print Too high

# What happens if you input the guess '5'?
  # Answer It would print Correct

# What happens if you input the guess '-5'?
  # Answer It would print Too low

# What happens if you input the guess '0'?
  # Answer It would print Too low

# What do the symbols '<' and '>' mean on lines 9 and 11?
  # Answer It checks if the guessed number is greater or less than the number

# What happens if you change line 5 to if guess = number: ?
  # Answer It would be an error because one equal sign assigns a variable and two equal signs check if they are true

# What do you notice about each line that FOLLOWS each IF statement?
  # Answer If statements get repeated more because they didnt use else


