name = (input("What is your name?\n"))
subject = (input("Is your subject Math, Science, or English?\n"))
classindex = ["Math", "Science","English"]
if subject == classindex[0]:
  print(name + " , your room number is 401 for " + subject)
elif subject == classindex[1]:
  print(name + ", your room number is 203 for " + subject)
elif subject == classindex[2]:
  print(name + ", your room number is 101 for " + subject)
else:
  print("I don't know which room that class is in")

  
  
  



