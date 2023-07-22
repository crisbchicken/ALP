# Example code 1

# Add comments to each line to say whehter it is inside or outside the loop and what it does.

# Explain the circumstances in which the loop will run.

print("What is the capital of France?")
#outside the loop
#string gets printed
answer = input() 
#outside the loop
#variable assigned from user

while answer != "Paris":
  #inside loop
  #runs the code as long as a condition is true
  print("Incorrect! Try again.")
  #inside loop 
  #string is printed when the code is not Paris
  
  answer = input("What is the capital of France?")
  #inside loop 
# The string gets printed again

print("Correct!")
#outside loop
#Loop ends when the user gets the correct answer so the loop is false

# Example code 2

counter = 1
#Variable assigned
# variable is assigned
while counter < 5:
  #start of loop
  #runs the code as long as condition is true
  print("This code is inside the loop")
  #string gets printedd
  counter += 1
  # c = c + 1

