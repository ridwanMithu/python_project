import random

#I will input my choice
# Computer will randomly choose one options
# I have set the winning conditions
# I have to loop through the game
# Make sure to put a condition incase user makes wrong input

while True:
  user_choice=input(f'Rock, Paper or Scissors? (r/p/s): ').lower()

  user_choice=user_choice.replace("r","rock")
  user_choice=user_choice.replace("p","paper")
  user_choice=user_choice.replace("s","scissors")
  print(user_choice)

  computer_choice_list=['rock','paper','scissors']
  computer_choice=random.choice(computer_choice_list)
  if user_choice=='r'or user_choice=='p'or user_choice=='s':
    print(f'You chose {user_choice}')
    print(f'Computer chose {computer_choice}')  
    if user_choice==computer_choice:
      print ('Draw! Try Again')
    elif user_choice=='rock' and computer_choice=='paper':
      print('Computer Wins')
    elif user_choice=='rock' and computer_choice=='scissors':
      print('You Win')
    elif user_choice=='paper' and computer_choice=='rock':
      print('You Win')
    elif user_choice=='paper' and computer_choice=='scissors':
      print('Computer Win')
    elif user_choice=='scissors' and computer_choice=='paper':
      print('You Win')
    elif user_choice=='scissors' and computer_choice=='rock':
      print('Computer Win')
  else:
    print('Invalid Input')

  
