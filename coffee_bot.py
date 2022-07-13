# Define your functions
def coffee_bot():
  print("Welcome to the cafe!")
  size = get_size()
  drink_type = get_drink_type()
  cup_type = get_cup_type()
  print('Alright, that\'s a {} {} {}!'.format(size, drink_type, cup_type))
  name = input("Can I get your name please? \n> ")
  print('Thanks, {}! Your drink will be ready shortly.'.format(name))
  
def print_msg():
  print('I\'m sorry, I did not understand your selection. Please enter the corresponding letter for your response.')

def get_size():
  res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ')
  if res == 'a':
    return('Small')
  elif res == 'b':
    return('Medium')
  elif res == 'c':
    return('Large')
  else:
    print_msg()
    return get_size()
    
def get_drink_type():
  res = input('What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n> ')
  if res == 'a':
    return('Brewed Coffee')
  elif res == 'b':
    return('Mocha')
  elif res == 'c':
    return order_latte()
  else:
    print_msg()
    return get_drink_type()

def order_latte():
  res = input("And what kind of milk for your latte? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk. \n> ")
  if res == 'a':
    return('2% milk')
  elif res == 'b':
    return('Non-fat milk')
  elif res == 'c':
    return('Soy milk')
  else:
    print_msg()
    return order_latte()

def get_cup_type():
  res = input('What kind of cup would you like: \n[a] Plastic \n[b] Reusable \n> ')
  if res == 'a':
    return('Plastic')
  elif res == 'b':
    return('Reusable')
  else:
    print_msg()
    return get_cup_type()


# Call coffee_bot()!
coffee_bot()