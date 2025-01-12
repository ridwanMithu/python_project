import random

playing=True
while playing:
  input_command=input('Roll the dice? (y/n) ').lower()
  if input_command=="y":
      x=random.randint(0,9)
      z=random.randint(0,9)
      print(x,z)
  elif input_command=="n":
    print('Thanks for Playing')
    playing=False
  else:
    print("Please input y or n to play the game")


