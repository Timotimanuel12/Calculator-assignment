
grocery_list = []
choice = 0
while choice != 4:
    print('[1] Add an item')
    print('[2] View the list')
    print('[3] Remove an item')
    print('[4] Exit')
    choice = int(input('Choice: '))

    match choice:
        case 1:
            add_fruit = input("Please enter an item: ")
            grocery_list.append(add_fruit)
        case 2:
            for fruits in grocery_list:
                print(fruits)

        case 3:
            rm = input("Please remove an item: ")
            if rm in grocery_list:
                grocery_list.remove(rm)
            else:
                print('Item not in list')


        case 4: break

        case _:print('not a valid command')

print("BYEEE!!!!!!")

# overall code is good! it works well, but it could use some input validation to let the user know that the operation was done successfully.
