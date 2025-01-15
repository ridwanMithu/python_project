def get_user_choice(choices):
  while True:
    user_choice=input('Rock, paper, or scissors? (input r/p/s)').lower()
    if user_choice in choices:
      return user_choice
    else:
      print('Invalid Choice!')