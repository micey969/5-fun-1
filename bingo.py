import os
import random
from time import sleep
from datetime import datetime


class Sheet():
  def __init__(self):
    self.sheet = [["B","I","N","G","O"],[],[],[],[],[]]
    for x in range(1, len(self.sheet)):
      for i in range(1, len(self.sheet)):
        self.sheet[x].append(random.randint(1,100))

  def print_sheet(self):
    print(f"|  {self.sheet[0][0]}  |  {self.sheet[0][1]}  |  {self.sheet[0][2]}  |  {self.sheet[0][3]}  |  {self.sheet[0][4]}  |")
    print(f"|  {self.sheet[1][0]} |  {self.sheet[1][1]} |  {self.sheet[1][2]} |  {self.sheet[1][3]} |  {self.sheet[1][4]} |")
    print(f"|  {self.sheet[2][0]} |  {self.sheet[2][1]} |  {self.sheet[2][2]} |  {self.sheet[2][3]} |  {self.sheet[2][4]} |")
    print(f"|  {self.sheet[3][0]} |  {self.sheet[3][1]} |  {self.sheet[3][2]} |  {self.sheet[3][3]} |  {self.sheet[3][4]} |")
    print(f"|  {self.sheet[4][0]} |  {self.sheet[4][1]} |  {self.sheet[4][2]} |  {self.sheet[4][3]} |  {self.sheet[4][4]} |")
    print(f"|  {self.sheet[5][0]} |  {self.sheet[5][1]} |  {self.sheet[5][2]} |  {self.sheet[5][3]} |  {self.sheet[5][4]} |")

  def mark_sheet(self, col, index):
    self.sheet[col][index] = 'x'

  def check_ball(self, ball):
    letter, number = ball
    for row in self.sheet:
      if letter in row:
        index = row.index(letter)
        for col in range(1, len(self.sheet)-1):
          if number == self.sheet[col][index]:
            self.mark_sheet(col, index)
            return True
    return False    
    

  def check_win(self):
    # win straight across
    if (self.sheet[1][0] == self.sheet[1][1] == self.sheet[1][2] == self.sheet[1][3] == self.sheet[1][4] =='x') or (self.sheet[2][0] == self.sheet[2][1] == self.sheet[2][2] == self.sheet[2][3] == self.sheet[2][4] == 'x') or (self.sheet[3][0] == self.sheet[3][1] == self.sheet[3][2] == self.sheet[3][3] == self.sheet[3][4] == 'x') or (self.sheet[4][0] == self.sheet[4][1] == self.sheet[4][2] == self.sheet[4][3] == self.sheet[4][4] == 'x') or (self.sheet[5][0] == self.sheet[5][1] == self.sheet[5][2] == self.sheet[5][3] == self.sheet[5][4] == 'x'):
      return True
    # win straight down
    elif (self.sheet[1][0] == self.sheet[2][0] == self.sheet[3][0] == self.sheet[4][0] == self.sheet[5][0] =='x') or (self.sheet[1][1] == self.sheet[2][1] == self.sheet[3][1] == self.sheet[4][1] == self.sheet[5][1] == 'x') or (self.sheet[1][2] == self.sheet[2][2] == self.sheet[3][2] == self.sheet[4][2] == self.sheet[5][2] == 'x') or (self.sheet[1][3] == self.sheet[2][3] == self.sheet[3][3] == self.sheet[4][3] == self.sheet[5][3] == 'x') or (self.sheet[1][4] == self.sheet[2][4] == self.sheet[3][4] == self.sheet[4][4] == self.sheet[5][4] == 'x'):
      return True
    else:
      return False


def get_ball():
  letters = ["B", "I", "N", "G", "O"]
  return (random.choice(letters), random.randint(1, 100))


def welcome():
  print("\t \t Welcome to Bingo!!")
  print("You willl receive a 5*6 Bingo sheet that you will use throughout the game. On every spin, you will be shown a ball with a Letter and a number. If the number and letter matches what is on your sheet, a mark will be placed on your sheet.")
  print("You have 5 minutes to complete the game before time runs out. If you manage to get a row or column of marks before time runs out, you will win the game. Goodluck!!!")
  sleep(3)


def replay():
  choice = input("\nDo you want to play again?[y/n] ")
  while choice[0] != 'y' and choice[0] != 'n':
    choice = input("\nDo you want to play again?[y/n] ")
  
  if choice[0] == 'y':
    return True
  else:
    print("\nThanks for playing. Good bye.")
    return False


def main():
  welcome()
  os.system("clear")

  playing, time = True, False
  start = datetime.now().minute
  end = start + 5

  while playing:
    game = Sheet()
    game.print_sheet()
    while not time:
      os.system("clear")
      input("\nTo spin the bingo wheel, please press Enter: ")

      # get a bingo ball
      ball = get_ball()
      print("\n\nThe ball is: ", ball)
      
      # check if match
      if game.check_ball(ball):
        print("\nMatch")
      else:
        print("\nNo Match.")

      # print sheet  
      game.print_sheet()

      # check for win
      if game.check_win():
        print("\n\nBINGO!!!!")
        print("Congratulations.")
        break
      
      # times up
      if datetime.now().minute == end:
        time =True

    print("\n Times up!!!")
    if replay():
      playing = True
    else:
      playing = False


if __name__ == "__main__":
  main()
 
