import random

actual=random.randint(1,100)
print(actual)
playing=True
while playing:
  guess=input("Guess the number: ")
  try:
    guess=int(guess)
  except ValueError:
    guess=input("Guess the number: ")
  
  guess=int(guess)
  if guess==actual:
    print("You have guessed Correctly")
    playing=False
    break
  elif guess<=actual:
    print("Think More")
  elif guess>=actual:
    print('Think less')
  elif ValueError:
    print("Try whole number")
