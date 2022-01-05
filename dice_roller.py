# What packages are being used
import random

# Main body of the game
def main():
  # Variables for amount of dice to roll and total of dice rolled
  dice_rolls = int(input('How many dice would you like to roll? '))
  dice_size = int(input('How many sides are the dice? '))
  dice_sum = 0
  # For loop to randomize the dice rolls and calcualte totals
  for i in range(0,dice_rolls):
    roll = random.randint(1,6)
    dice_sum += roll
    if roll == 1:
      print(f'You rolled a {roll}! Critical Failure')
    elif roll == dice_size:
      print(f'You rolled {roll}! Critical Success!')
    else:
      print(f'You rolled a {roll}')
  print(f'You have rolled a total of {dice_sum}')

if __name__== "__main__":
  main()