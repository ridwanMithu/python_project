# weight=input("Input your weight: ")
# unit=input("input k for KG and l for Pounds: ")

# if unit=='k':
#   weight=float(weight)*5
#   print(f'Your weight in pound: {weight}')
# elif unit=='l':
#   weight=float(weight)*2
#   print(f'Your weight in KG: {weight}')
# i=0
# while i<=10:
#   i+=1
#   print(i*"*")

# def multiply(*numbers):
#     total=1
#     for number in numbers:
#       total*=number
#     return total

# multiply(2,3,4,5)

# def save_user(**user):
#   print(user)

# save_user(id=1,name='John',age=22)

def fizzbuzz(input):
  if input%3==0 and input%5==0:
    print('fizzbuzz')
  elif input%5==0:
    print('buzz')
  elif input%3==0:
    print('fizz')
  #as we will come here any way we do not need an else function. instead we can dierectly give the print command outsiede of the loop.This only works with return function
  else:
    print(input)

fizzbuzz(25)