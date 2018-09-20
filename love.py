import os
import random

file = open("affirmations.txt", "r")
affirmations = file.readlines()

print("I was reminded yesterday that there are people out there that suffer from depression.")
print("This program today is a pretty simple one to remind persons of what they may need to hear sometimes. It has words of affirmations and words of encouragement. So, whenever you want to hear from someone, or you just need a boost, just press Enter.")
print("\nType 'exit' to stop the program.")

os.system("clear")
comm = raw_input("Press Enter please:")
while comm != "exit":
  os.system("clear")
  print(random.choice(affirmations))
  comm = raw_input("Do you know what else? ")

print("\n\nI hope this has been a source of encouragement for you. You are not alone and you are loved.")
print("BE STRONG.")