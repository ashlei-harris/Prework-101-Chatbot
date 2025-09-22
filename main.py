def option_menu():
  print('\n Please select an option')
  print('1. View pets')
  print('2. Adopt a pet')
  print('3. Put a pet up for adoption')
  print('4. Serach for a pet')
  print('5. Exit menu')

def selection():
  option = int(input('\n Please enter the number for your option: '))
  if option == 1:
    viewpets()
  elif option == 2:
    adopt()
  elif option == 3:
    add()
  elif option == 4:
    serach()
  elif option == 5:
    print(' \n Thank you and goodbye',name,'! Have a nice day!')
  else:
    print('invalid option. Try again')
    option_menu()
    selection()

def viewpets():
  print('View pets')
  action = bool(input('\n Enter to return to main menu: '))
  if action == True:
    option_menu()
    selection()
  else:
   print(' \n Thank you and goodbye',name,'! Have a nice day!')

def adopt():
  print('Adopt a pet')
  action = bool(input('\n Enter to return to main menu: '))
  if action == True:
    option_menu()
    selection()
  else:
   print(' \n Thank you and goodbye',name,'! Have a nice day!')

def add():
  print('Add a pet')
  action = bool(input('\n Enter to return to main menu: '))
  if action == True:
    option_menu()
    selection()
  else:
   print(' \n Thank you and goodbye',name,'! Have a nice day!')

def serach():
  print('Serach for pet')
  action = bool(input('\n Enter to return to main menu: '))
  if action == True:
    option_menu()
    selection()
  else:
   print(' \n Thank you and goodbye',name,'! Have a nice day!')

print('Welcome to the pet adoption chatbot!')
name = input('Please enter your name: ')
age = input('Please enter your age: ')
print('\n Hello', name, 'you are', age, 'years old!')
print('\n How may I help you?')

option_menu()
selection()