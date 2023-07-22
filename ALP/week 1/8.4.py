'''
Reference Link
https://docs.google.com/document/d/1Lf221krWqB0vv5zSaQDvzBi6you6AuKdfn5x1TETh7Q/edit?usp=sharing
'''
'''
## Task Instructions - Beat The Zombie

This task requires you to combine lots of skills from earlier lessons. Don't be afraid to look at your old code, google ideas and have fun with the dialogue.  Good luck!

Write a program that simulates an encounter with a zombie in an RPG

1- Create a list of possible weapons.
2- In a variable called ‘zombieWeakness’ store the name of one of the weapons from the list.
3- Output messages telling the user that they have encountered a zombie and should prepare to fight.
4- Output the list of weapons to the user.  Ask if they want to type 1 to use one from the list or 2 to pick their own.  
  4.1- If they type 1 then they should input the weapon name - store it to a new variable. 
  4.2- If they type 2 they should input the weapon name - add it to the list and save it to a new variable.
5- If the weapon picked matches the zombieWeakness, output a message telling the user that they have won the fight.  
  5.1- Otherwise output a message saying that they have lost.

'''
import random
weapons = ["Axe", "Crossbow","Chainsaw", "Hammer" ]
zombieWeakness = weapons[random.randrange(len(weapons))]
print("You have encountered a zombie, prepare to fight!")
print(weapons)

Pickweapon = int(input("Type 1 to use a weapon from the list. Type 2 to have your own weapon!\n"))

if Pickweapon == 1:
  userweapon = input("Please type the name from the list\n")
elif Pickweapon == 2:
  userweapon = input("Please type the name of a weapon you would like to add.\n")
  weapons.append(userweapon)
if zombieWeakness == userweapon:
  print("You have won the fight")
else:
  print("You have lost")

  
