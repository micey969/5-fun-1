import os
import time
import random


def choice_word(level):
  """
  Returns a word to guess based on player's level
  """

  easy = ["mango", "woman", "children", "father", "snacks", "fridge"]
  medium = ["delivered", "arrogant", "ratchet", "television", "spectacle", "wardrobe"]
  hard = ["electricity", "stupendous", "perpendicular", "mitochondria", "legality", "mnemonic"]

  if level == 1:
    word = random.choice(easy)
  elif level == 2:
    word = random.choice(medium)
  else:
    word = random.choice(hard) 
  return word
    

def replay():
  """
  Asks the user if they would want to try the game again.
  """
  
  choice = input("\nDo you want to play again?[y/n] ")
  if choice[0] == 'y':
    return True
  elif choice[0] == 'n':
    print("\nThanks for playing. Good bye.")
    return False
  else:
    print("\nI think you may have had a stroke, please try again.")
    replay()


HANGMAN = [
"""
 ------
 |    |
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |   -+-
 | 
 |   
 |   
 |  
----------
""",
"""
 ------
 |    |
 |    O
 |  \-+-
 |   
 |   
 |     
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  \-+-/
 |   
 |   
 |     
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  \-+-/
 |    |
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  \-+-/
 |    |
 |   /
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |   /+\\
 |    |
 |   | |
 |  
----------
"""]


playing = True
while playing:
  print("\n \n\t \t Welcome to Hangman!\n\n")
  input("Press Enter to START: ")

  print("\n\nLEVELS: 1- EASY, 2- MEDIUM, 3- HARD")
  choice = int(input("Please enter a level: "))

  word = choice_word(choice)
  display = ["-"] * len(word)
  max_wrong = len(HANGMAN) -1
  guesses = []
  wrong = 0

  
  while wrong < max_wrong and "".join(display) != word:
    os.system("clear")
    print(HANGMAN[wrong])
    print("".join(display))
    print("Used letters: ", guesses)

    guess = input("What is your letter? ").lower()
    time.sleep(1) 

    while guess in guesses:
      print("\nTry again... You've already used this letter")
      guess = input("Guess a letter: ").lower()
      time.sleep(1)
    guesses.append(guess)

    if guess in word:
      for i in range(len(word)):
        if guess == word[i]:
          display[i] = guess

    else:
      print("\nINCORRECT! Try again!")
      wrong += 1

  time.sleep(1)
  os.system("clear")
  if wrong == max_wrong:
    print(HANGMAN[-1])
    print("\n\nGAME OVER!!!!!")

  else:
    print("\n\nWINNER!!! Congratulations!")

  playing = replay()
  os.system("clear")