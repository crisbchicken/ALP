# Program to calculate the area of a rectangle

# Get input for height & width. Convert to integers and store in variables

# Calculate the area & store the result in the area variable

# Output the area variable (converted to string)

height = int(input("Enter the height of the triangle: "))
width = int(input("Enter the width of the triangle: "))
area = height * width
print("The area is " + str(area))

mealcost = int(input("Enter the price of a meal at a restaurant "))
tip = mealcost / 5 
total = tip + mealcost
print("The tip is " + str(tip))
print("The total price is " + str(total))

height = int(input("Enter the height of a cuboid: "))
width = int(input("Enter the width of a cuboid: "))
length = int(input("Enter the length of a cuboid"))

volume = length * width * height
surfacearea = 2*(length * width * height)
print("The volume of a cuboid is " + str(volume) + " and the surface area is " + str(surfacearea))

'''
Extra Challenges
Perimeter Calc
Create a program that allows the user to enter 2 numbers representing the width and length of a rectangle. The program calculates and displays the perimeter of the rectangle. 
Restaurant Tip Calculator 
Create a program that allows the user to enter the price of a meal at a restaurant. The program calculates the amount of the tip to be paid at 20%. The tip and total price are then displayed separately.
Volume and Surface Calc 
Create a program that allows the user to enter 3 numbers representing the height, width and length of a cuboid. The program calculates and displays the volume and total surface area of the cuboid. 
'''