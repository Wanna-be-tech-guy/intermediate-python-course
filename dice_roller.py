# What packages are being used
import random

# Main body of the game
def main():
  # Variables for amount of dice to roll and total of dice rolled
  dice_rolls = 2
  dice_sum = 0
  # For loop to randomize the dice rolls and calcualte totals
  for i in range(0,dice_rolls):
    roll = random.randint(1,6)
    dice_sum += roll
    print(f'You rolled a {roll}')
  print(f'You have rolled a total of {dice_sum}')

if __name__== "__main__":
  main()