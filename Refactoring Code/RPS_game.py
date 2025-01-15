import random

emojis={'r':'💎','p':'📃','s':'✂️'}
choices=('r','p','s')

while True:
  user_choice=input('Rock, paper, or scissors? (input r/p/s)').lower()
  if user_choice not in choices:
    print('Invalid Choice!')
    continue

  computer_choice=random.choice(choices)

  print(f'You chose {emojis[user_choice]}')
  print(f'Computer chose {emojis[computer_choice]}')

  if user_choice==computer_choice:
    print("Draw! Play Again")
  elif (
    (user_choice=='r' and computer_choice=='s') or
    (user_choice=='s' and computer_choice=='p') or
    (user_choice=='p' and computer_choice=='r')
  ):
    print("You Win")
  else:
    print('You lose')

  should_continue=input('continue? (Y/N)').lower()
  if should_continue=='n':
    break