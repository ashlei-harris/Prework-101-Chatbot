from Invetory import Inventory

def option_menu():
  print('\n Please select an option')
  print('1. Return item')
  print('2. Exchage item')
  print('3. View invetory')
  print('4. Exit')

def selection():
  option = int(input('\nplease enter the number for your option: '))
  if option == 1:
    Return()
  elif option == 2:
    exchage()
  elif option == 3:
    view()
  elif option == 4:
    print(' \n thank you and goodbye',name,'! Have a nice day!')
  else:
    print('invalid option. try again')
    option_menu()
    selection()

def Return():
  print('Return Item')
  returning = True
  while returning:
      Id = input('Enter the product Id: ')
      Product_Quanity = int(input('Enter the amount of product you have: '))
      found = False
      for item in Inventory:
        if item["id"] == Id:
            item["quanity"] += Product_Quanity
            total_value = item["price"] * Product_Quanity
            print(f"${total_value:.2f} has been added to your account")
            found = True
            break

      if not found:
        print("product not found")
        continue
      returning = False

  action = input('\nEnter to return to main Menu (y/n): ')
  if action != 'y':
    print(f'Goodbye {name}!')
  else:
    option_menu()
    selection()

def exchage():
  print('Exchage Item')
  exchaging = True
  while exchaging:
    Id = input('Enter the product id: ')
    Product_Quanity = int(input('enter the amount of product you have: '))
    found = False
    for item in Inventory:
     if item["id"] == Id:
      item["quanity"] += Product_Quanity
      total_value = item["price"] * Product_Quanity
      print(f"you have ${total_value:.2f}")
      found = True
      break
    if not found:
        print("product not found")
        continue
    while True:
      wanted_product = input('What would you like to buy: ')
      product_found = False
      for item in Inventory:
        if item['type'] == wanted_product.lower():
          product_found = True
          print(f"that is {item['price']}")
          wanted_number= int(input('how many would you like: '))
          while wanted_number > item['quanity']:
            print(f"we only have {item['quanity']} avalibe ")
            wanted_number= int(input('how many would you like: '))

          wanted_total = item['price'] * wanted_number
          if wanted_total > total_value:
            extra = abs(wanted_total - total_value)
            pay = input(f'that is worth more than the exchange item. \nWould you like to pay {extra}? (y/n): ')
            if pay.lower() !='y':
              print('exchage caneled')
              continue
            else:
              print('Amount Payed')
              item['quanity'] -= wanted_number
          
          elif wanted_total < total_value:
            extra = abs(wanted_total - total_value)
            pay = input(f'you will have {extra} left. Would you like to pay? (y/n): ')
            if pay.lower() !='y':
             print('Exchage Caneled')
             continue
            else:
              item['quanity'] -= wanted_number
              print('Amount Payed')
              break
            
          else:
            pay = input(f'that is a perfect exchage! Would you like to pay (y/n): ')
            if pay.lower() !='y':
              print('Exchage Caneled')
              continue
            else:
              item['quanity'] -= wanted_number
              print('Amount Payed')  
          break
      if not product_found:
          print("No product found")
          continue
      else:
        break
    exchaging = False

  action = input('\nenter to return to main menu (y/n): ')
  if action != 'y':
    print(f'Goodbye {name}!')
  else:
    option_menu()
    selection()         
 
def view():
  for index, item in enumerate(Inventory):
    print(f"Item {index + 1}:")
    for key, value in item.items():
        print(f"  {key}: {value}")
    print("-------------------")
  action = input('\nEnter to return to main menu (y/n): ')
  if action != 'y':
    print(f'Goodbye {name}!')
  else:
    option_menu()
    selection() 


print('Welcome to the chatbot!')
name = input('Please enter your name: ')
age = input('Please enter your age: ')
print('\n Hello', name, 'you are', age, 'years old!')
print('\nHow may I help you?')

option_menu()
selection()