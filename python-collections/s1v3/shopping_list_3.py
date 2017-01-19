import os
shopping_list = []

def clear_screen():
    os.system("cls" if os.name=="nt" else "clear")
    print("Clear!")

def show_help():
    print("What should we pick up at the store?")
    print("""
Enter 'DONE' to stop adding items.
Enter 'HELP' for this help.
Enter 'SHOW' to see your current list.
Enter 'REMOVE' to delete an item from the list.
Enter 'MOVE' to move an item in the list.
Enter 'CLEAR' to delete the list.
""")


def add_to_list(item):
    if len(shopping_list):
        position = input("Where should I add {}?\n"
                         "Press ENTER to add to the end of the list\n"
                         "> ".format(item))
    else:
        position= 0
    try:
        position = abs(int(position))
    except ValueError:
        position = None
    if position is not None:
        shopping_list.insert(position-1,item)
    else:
        shopping_list.append(item)
    show_list()


def show_list():
    clear_screen()
    print("Here's your list:")
    index = 1
    for item in enumerate(shopping_list):
        print("{}. {}".format(item[0]+1,item[1]))
        index+=1
    print("-"*10)


def remove_item():
    show_list()
    what_to_remove = input("What would you like to remove?\n> ")
    try:
        shopping_list.remove(what_to_remove)
    except ValueError:
        pass
    show_list()

def clear_list():
    shopping_list=[]
    show_list()


def move_item():
    show_list()
    what_to_remove = input("What item (number) would you like to move?\n> ")
    try:
        add_to_list(shopping_list.pop(int(what_to_remove)-1))

    except ValueError:
        pass

show_help()



while True:
    new_item = input("> ")

    if new_item.upper() == 'DONE' or new_item.upper == "QUIT":
        break
    elif new_item.upper() == 'HELP':
        show_help()
        continue
    elif new_item.upper() == 'SHOW':
        show_list()
        continue
    elif new_item.upper() == 'REMOVE':
        remove_item()
        continue
    elif new_item.upper() == 'CLEAR':
        clear_list()
        continue
    elif new_item.upper() == 'MOVE':
        move_item()
        continue
    else:
        add_to_list(new_item)

show_list()
