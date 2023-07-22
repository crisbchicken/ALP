# Example Code 1

def say_hi():
  #subroutine is defined
  print("Why hello there!")
# when subroutine is called it displays this script
def offer_drink():
  #subroutine is defined
  print("Would you care for a spot of tea?")
# when subroutine is called it displays this script

def offer_food():
  #subroutine is defined
  print("Biscuit?")
# when subroutine is called it displays this script
def say_bye():
  #subroutine is defined
  print("Cheerio then.")
# when subroutine is called it displays this script

offer_drink() #displays the scripts that made their subroutines defined
say_hi()
offer_food()

# Example code 2
def maths1(): 
  #subroutine defined
  num1 = 50
  num2 = 5
  return num1 + num2

def maths2():
  #subroutine defined
  num1 = 50
  num2 = 5
  return num1 - num2

def maths3():
  #subroutine defined
  num1 = 50
  num2 = 5
  return num1 * num2

outputNum = maths2()
#variable, outputNm, is assigned to a subroutine 
print(outputNum)
#variable is printed

# Example Code 3
def location(country):
  print("I am from " + country)

#subroutine is defined
location("Brazil")
'''
I am from Brazil would be printed
'''
