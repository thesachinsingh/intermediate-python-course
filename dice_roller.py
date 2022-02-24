import random
def main():
  dice_rolls = int(input("How many Dice rolls do you want ? "))
  dice_size = int(input("How many sides are there on the dice? "))
  dice_sum = 0
  for i in range(0,dice_rolls):
    roll = random.randint(1,dice_size)
    dice_sum += roll
    if roll == 1:
      print(f'Lol, you got a {roll}! Nice Try')
    elif roll == 6:
      print(f'Wonderful! You are the chosen one, you got {roll}!')
    else:
      print(f'You rolled a {roll}')
  print(f'You have rolled a total of {dice_sum}')

if __name__== "__main__":
  main()