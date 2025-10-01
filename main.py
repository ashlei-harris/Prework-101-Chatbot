def option_menu():
  print('\n Please select an option')
  print('1. ')
  print('2. ')
  print('3. ')
  print('4. ')
  print('5. ')

def selection():
  option = int(input('\n Please enter the number for your option: '))
  if option == 1:
    option1()
  elif option == 2:
    option2()
  elif option == 3:
    option3()
  elif option == 4:
    option4()
  elif option == 5:
    option5(' \n Thank you and goodbye',name,'! Have a nice day!')
  else:
    print('invalid option. Try again')
    option_menu()
    selection()

def option1():
  print('1')
  action = bool(input('\n Enter to return to main menu: '))
  if action == True:
    option_menu()
    selection()
  else:
   print(' \n Thank you and goodbye',name,'! Have a nice day!')

def option2():
  print('2')
  action = bool(input('\n Enter to return to main menu: '))
  if action == True:
    option_menu()
    selection()
  else:
   print(' \n Thank you and goodbye',name,'! Have a nice day!')

def option3():
  print('3')
  action = bool(input('\n Enter to return to main menu: '))
  if action == True:
    option_menu()
    selection()
  else:
   print(' \n Thank you and goodbye',name,'! Have a nice day!')

def option4():
  print('4')
  action = bool(input('\n Enter to return to main menu: '))
  if action == True:
    option_menu()
    selection()
  else:
   print(' \n Thank you and goodbye',name,'! Have a nice day!')

print('Welcome to the chatbot!')
name = input('Please enter your name: ')
age = input('Please enter your age: ')
print('\n Hello', name, 'you are', age, 'years old!')
print('\n How may I help you?')

option_menu()
selection()
