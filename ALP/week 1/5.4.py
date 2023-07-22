
testMark = int(input("Enter a test mark between 1 and 100\n"))
if testMark > 100:
  print("Too high please type a valid number")
  exit()
elif testMark < 1:
  print("Too low please type a valid number")
  exit()

if testMark < 40: 
  fail = "Y"
else:
  fail = "N"

if fail != "N":
  print("Retake required")
else:
  print("Passed")

if testMark < 80:
  print("B grade")
elif testMark < 69:
  print("C grade")
elif testMark < 40:
  print("U grade")
else:
  print("A grade")

