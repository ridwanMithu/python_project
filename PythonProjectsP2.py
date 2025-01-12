import random

actual=random.randint(1,100)
print(actual)
while True:
  guess=input("Guess the number: ")
  try:
    guess=int(guess)
    if guess==actual:
      print("You have guessed Correctly")
      break
    elif guess<actual:
      print("Think More")
    elif guess>actual:
      print('Think less')
  except ValueError:
    print("Guess a whole number")
