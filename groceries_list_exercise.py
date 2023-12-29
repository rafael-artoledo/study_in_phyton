#Date 12-29-2023
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
        erase_item = (input("Chose the item's index:"))
        for index, item in enumerate(grocery_list):
            try:
                erase_item = int(erase_item)
            except TypeError:
                os.system('cls')
                print('Just number, please.')
                continue 
            if erase_item != index and erase_item in range(len(grocery_list)):
                pass   
            elif erase_item == index:
                os.system('cls')
                print(f'The item {grocery_list[erase_item]} was erased.')
                del grocery_list[erase_item]
                break
            else:
                os.system('cls')
                print('Please, select the correct index number item.')
                break
    
    elif entry == 's':
        os.system('cls')
        for index, item in enumerate(grocery_list):
            print(index, item)
    
    elif entry == "q":
        os.system('cls')
        break        
    
    else:
        os.system('cls')
        print('Unrecognized command.')
        continue           