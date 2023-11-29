count = 0//hi. ethan


def guessingFood():
  guess = input('Guess my favorite food: ')
  global count
  count = count + 1
  if (guess != 'Rice'):
    guessingFood()


def guessingDrink():
  guess = input('Guess my favorite drink: ')
  global count
  count = count + 1
  if (guess != 'Water'):
    guessingDrink()


print('Welcome to the best friend test.')
guessingFood()
print('you got it!')
guessingDrink()
print('you got it!')
if count < 5:
  print('You know me well.')
elif count < 10:
  print('We should probably talk more.')
else:
  print('You are a disgrace!')
