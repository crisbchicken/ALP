# Starter Code

number1 = int(input("Please enter a number\n"))
number2 = int(input("Please enter a second number\n"))
number3 = int(input("Please enter a third number\n"))

if number1 > number2:
  print("Number 1 is bigger than number 2")
elif number2 > number1: 
  print("Number 2 is bigger than number 1")
else:
  print("Number 1 and number 2 are the same")

if number3 > number2:
  print("Number 3 is bigger than number 2")
elif number2 > number3:
  print("Number 2 is bigger than number 3")
else:
  print("Number 3 and number 2 are the same")

if number3 > number1:
  print("Number 3 is bigger than number 1")
elif number1 > number3:
  print("Number 1 is bigger than number 3")
else:
  print("Number 3 and number 1 are the same")
