'''
In the modify tasks, you are given some starter code. Use the instructions below to make changes to the code. Comment your changes to explain what you have done.

Run the program to see how it works.
Adapt the code to:

1. Get user input into the number variable.
2. Change the print statement so it outputs 'number' multiplied by 'counter' equals 'product'
3. Make the counter increase by 2 every loop
4. Add a line once the loop has finished to output 'The loop has finished' '''

number = int(input("Enter a number:\n"))
#gets the value of the variable from the user
counter = 1

while counter < 13:
  print(str(number) + " multiplied by " + str(counter) + " is equal to " + str(number*counter))
#converted integers to strings to concatenate them with sentence
  counter = counter + 2
  #counter increases by two every time
print("The loop has finished")
#outside the loop, when while condition got false

#Challenge
c = 1 
while c <=12:
  print(str(c) + " times 7 is " + str(c*7))
  c += 1

num = int(input("Enter a number\n"))
c = 1
while c <= num:
  print(str(c) + " times " + str(num) + " is " + str(c*num))
  c += 1