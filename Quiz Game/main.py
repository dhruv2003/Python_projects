print("Welcome to My Quiz Game")

playing=input("Do You want to Play? ")


if playing.lower() != "yes":
  quit()
  
print("OK let's go!")
score=0

answer=input("What is DPI? ")
if answer.lower() == "dots per inch":
  print("Correct Answer!")
  score += 1
else:
  print("You got it Wrong!!")
  
answer=input("What is CPU? ")
if answer.lower() == "central processing unit":
  print("Correct Answer!")
  score += 1
else:
  print("You got it Wrong!!")
  
answer=input("What is GPU? ")
if answer.lower() == "graphics processing unit":
  score += 1
  print("Correct Answer!")
else:
  print("You got it Wrong!!")
  
print("You got " + str(score)+" questions correct!!")

print("You got "+str((score/4)*100)+"%")       