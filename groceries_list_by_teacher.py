import os

grocery_list = []

print('Here you can make your groceries list')
while True:
    print('Select one option:')
    entry = input('[a]dd, [e]rase , [s]how list and [q]uit:').lower()
    
    if entry == 'a':
        add_item = input('Which item:')
        os.system('cls')
        grocery_list.append(add_item)
        print(f'The item "{add_item}" was added to the list.')
    
    elif entry == 'e':
        erase_item_str = (input("Chose the item's index:"))
        try:
            erase_item = int(erase_item_str)
            os.system('cls')
            print(f'The item {grocery_list[erase_item]} was erased.')
            del grocery_list[erase_item]
        except ValueError:
            os.system('cls')
            print('Just number, please.')
        except IndexError:
            os.system('cls')
            print('Please, select the correct index number item.')        
        except Exception:
            os.system('cls')
            print('Unknow error.') 
    
    elif entry == 's':
        os.system('cls')
        if len(grocery_list) == 0:
            print('Nothing in the list.')
        
        for index, item in enumerate(grocery_list):
            
            print(index, item)
    
    elif entry == "q":
        os.system('cls')
        break        
    
    else:
        os.system('cls')
        print('Unrecognized command.')
             