import random


print("GAME RULES!!!")

print("\nGuess a number between 1 and 100.")
print("If you go outside of these numbers, you will get an 'OUT OF BOUNDS' warning.")
print("If your guess is within 10 of the number, you'll see 'WARM'.")
print("Else if further than 10 away from the number, you will see 'COLD'.")
print("If your next guesses are closer to the number than the previous guess, you'll see 'WARMER'.")
print("If not, then you'll see 'COLDER'.")
print("If you guess correctly you'll see 'CONGRATULATIONS' as well as how many guesses you took.")

print("\nReady? Let's play!")

#holds the player guesses
guesses = []

#the number the player needs to guess
secret_num = random.randint(1, 100)


#the game
while True:
  guess = input("\nI'm thinking of a number between 1 and 100. What is the secret number? ")

  if guess.isalpha():
    print("NUMBERS ONLY PLEASE!")

  else:
    number = int(guess)
    if number not in range(1, 101):
      print("OUT OF BOUNDS!")

    elif number == secret_num:
      print("\nCONGRATULATIONS!!!!")
      print(f"\nYou took {len(guesses)} to guess {secret_num} correctly.")

      again = input("\nDo you want to play again?[y/n] ")

      if again[0].lower() == 'y':
        print("\nAwesome, let's do this.")
        guesses.clear()
        secret_num = random.randint(1, 100)
        continue
      else:
        print("\nThanks for playing. Goodbye.")
        break

    elif abs(number - secret_num) <= 10:
      print("WARM")
      guesses.append(number)

    elif abs(number - secret_num) > 10:
      print("COLD")
      guesses.append(number)

    elif abs(number - secret_num) < abs(guesses[-1] - number):
      print("WARMER")
      guesses.append(number)

    else:
      print("COLDER")
      guesses.append(number)
