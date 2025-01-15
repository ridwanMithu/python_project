
def choice_manager(user_choice,computer_choice):
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