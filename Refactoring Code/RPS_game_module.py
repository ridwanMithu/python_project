import random
from choice_manager import choice_manager
from get_user_choice import get_user_choice
from display_choices import display_choice

emojis={'r':'💎','p':'📃','s':'✂️'}
choices=('r','p','s')

def play_game():
  while True:
    user_choice=get_user_choice(choices)

    computer_choice=random.choice(choices)

    display_choice(emojis,user_choice,computer_choice)

    choice_manager(user_choice,computer_choice)

    should_continue=input('continue? (Y/N)').lower()
    if should_continue=='n':
      break

play_game()