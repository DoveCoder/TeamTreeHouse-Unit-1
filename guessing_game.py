"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
"""

import random
from tkinter import E


def play():
     play_again = ''
     while play_again != 'yes' or play_again != 'no':
          play_again = input("Play again 'yes' or 'no':  ").lower()
          if play_again == 'yes':
               start_game()
          elif play_again == 'no':
               print("Thank you, for playing my game.")
               break
          else:
               print("Invaild selection")


def player(size):
     while True:
          try:
               choice = int(input("Please choose a number between (1 and {}):  ".format(size)))
          except ValueError:
               print("Please enter a number!")
               continue
          else:
               return choice


def high_score(tries):
     high_score = 0

     if high_score == 0:
          high_score = tries
     elif tries < high_score:
          high_score = tries
     else:
          print("Something went wrong!")
     return high_score


def start_game():
     """Starts guessing game."""

     size_start = 0

     print("""
     __    _     ____  __   __   _   _      __   
     / /`_ | | | | |_  ( (` ( (` | | | |\ | / /`_ 
     \_\_/ \_\_/ |_|__ _)_) _)_) |_| |_| \| \_\_/ 
     __     __    _      ____                    
     / /`_  / /\  | |\/| | |_                     
     \_\_/ /_/--\ |_|  | |_|__       \n""")

     
     difficulty = input("Choose your difficulty\n type 'H' for Hard 'M' for Medium 'E' for Easy:  ")
     difficulty = difficulty.upper()
     if difficulty == 'H':
          size_start = 100
     elif difficulty == 'M':
          size_start = 50
     else:
          size_start = 10
     
     computer_choice = random.randint(1, size_start)
     player_choice = player(size_start)
     number_of_tries = 1
     
     
     while player_choice != computer_choice:
          
          if player_choice == computer_choice:
               pass
          elif player_choice < computer_choice:
               print("_____It's Higher_____")
               number_of_tries += 1
               player_choice = player(size_start)
          elif player_choice > computer_choice:
               print("_____It's Lower_____")
               number_of_tries += 1
               player_choice = player(size_start)
          

     score = high_score(number_of_tries)     
               

     print("Your Guess was correct!")
     if number_of_tries == 1:
          print("You took {} try to find the number.".format(number_of_tries))
     else:
          print("You took {} tries to find the number.".format(number_of_tries))
     print("=====> Your High Score is #_{}_ <=====".format(score))
     

     play()
     

# Kick off the program by calling the start_game function.
start_game()