import sys
arguments = sys.argv
print(arguments)

import os
import time
import traceback

#CREATE FILE IF IT DOESN'T ALREADY EXIST
people = []
drinks = []

#FUNCTIONS

def clear():
    os.system("clear")

def end_thanks():
    clear()
    print(f"{coffee_cup_ascii}\nThanks for using BrIWer v1!")
    time.sleep(1)
    clear()
    exit()

def print_list(arg, list_name):
    print(f"The current list of {list_name} is: \n")
    print(f"+{'=' * 18}+")
    for item in arg:
        spaces = (17 - len(item))
        print("| " + item + f"{' ' * spaces}" + "|")
    print(f"+{'=' * 18}+")

def view_list(choice):    
    clear()
    print(coffee_cup_ascii)
    if  choice == 1:
        arg = people
        list_name = "people"
        print_list(arg, list_name)
    elif choice == 2:
        arg = drinks
        list_name = "drinks"
        print_list(arg, list_name)
    elif choice == 3:
        pass
    else:
        print(error_message)

#NEED TO ADD APPEND-ONLY FOR ADD ITEM FUNCTION
def add_an_item(choice):
    if choice == 1:
        clear()
        added_name = str(input(coffee_cup_ascii + "\n" + add_name_message))
        people.append(added_name)
        #INSERT SAVE FUNCTION HERE?
        clear()
        print(coffee_cup_ascii)
        print("Name added!\n")
        print("The current list of people is: \n")
        print(people)
    elif choice == 2:
        clear()
        added_drink = str(input(coffee_cup_ascii + "\n" + add_drink_message))
        drinks.append(added_drink)
        #INSERT SAVE FUNCTION HERE?
        clear()
        print(coffee_cup_ascii)
        print("Drink added!\n")
        print("The current list of drinks is: \n")
        print(drinks)
    elif choice == 3:
        pass
    else:
        print(error_message)

#NEED TO ADD WRITE TO FILE FOR REMOVE AN ITEM FUNCTION 
def remove_an_item(choice):
    try:
        if choice == 1:
            clear()
            removed_name = str(input(coffee_cup_ascii + "\n" + remove_name_message))
            people.remove(removed_name)
            #INSERT SAVE FUNCTION HERE?
            clear()
            print(coffee_cup_ascii)
            print("Name removed!\n")
            print("The updated list of people is: \n")
            print(people)
        elif choice == 2:
            clear()
            removed_drink = str(input(coffee_cup_ascii + "\n" + remove_drink_message))
            people.remove(removed_drink)
            #INSERT SAVE FUNCTION HERE?
            clear()
            print(coffee_cup_ascii)
            print("Drink removed!\n")
            print("The updated list of drinks is: \n")
            print(drinks)
        elif choice == 3:
            pass
        else:
            print(error_message)
    except Exception as e:
        clear()
        error_length = len(str(e))
        print(coffee_cup_ascii)
        print("There has been an error!\n")
        print(f"+{'=' * (error_length)}+")
        print(" " + str(e))
        print(f"+{'=' * (error_length)}+")

def populate_list(filepath):
    list_of_items = []
    try:
        with open(filepath, 'r') as items_file:
            for lines in items_file.readlines():
                list_of_items.append(lines)
            items_file.close()
            return list_of_items
    except:
        print("Failed to open file!")

#MENU FUNCTIONS

def main_menu():
    people = populate_list("people.txt")
    drinks = populate_list("drinks.txt")
    main_menu = True
    while main_menu == True:
        clear()
        choice = int(input(coffee_cup_ascii + main_menu_message))
        inner_menu = True
        while inner_menu == True:
            if choice == 1:
                list_menu(inner_menu)
                inner_menu = False
            elif choice == 2:
                add_menu(inner_menu)
                inner_menu = False
            elif choice == 3:
                remove_menu(inner_menu)
                inner_menu = False
            elif choice == 4:
                end_thanks()
                exit()
        else:
            clear()
            print(error_message)

def list_menu(inner_menu):
    menu = inner_menu
    while menu == True:
        clear()
        try:  
            choice = int(input(coffee_cup_ascii + list_menu_message))
        except:
            print("Please type a number!")
        view_list(choice)
        if choice == 1 or choice == 2:
            input("\nPress Enter to return to the previous menu.")
        elif choice == 3:
            menu = False
        else:
            clear()
            print(error_message)

def add_menu(inner_menu):
    menu = inner_menu
    while menu == True:
        clear()
        choice = int(input(coffee_cup_ascii + add_menu_message))
        add_an_item(choice)
        if choice == 1 or choice == 2:
            input("\nPress Enter to return to the previous menu.")
        elif choice == 3:
            menu = False
        else:
            clear()
            print(error_message)

def remove_menu(inner_menu):
    menu = inner_menu
    while menu == True:
        clear()
        choice = int(input(coffee_cup_ascii + remove_menu_message))
        remove_an_item(choice)
        if choice == 1 or choice == 2:
            input("\nPress Enter to return to the previous menu.")
        elif choice == 3:
            menu = False
        else:
            clear()
            print(error_message)

def exit_to_menu():
    pass

#EXTRA FUNCTIONS

def save_items(filepath, list_of_items):
    try:
        with open(file_name, 'w') as items_file:
            for item in list_of_items:
                items_file.write(item + "\n")
    except:
        print("Failed to open file!")

# for i, v in enumerate([list_of_items])

#MESSAGES & DESIGN
coffee_cup_ascii = """
                            ß       o$$$$$$oo
                                 o$§        $$oo
                                 $   o$$o  $$o
                                $$  o  $o  $o   $
                                $$   $o $   $   o$
                                 $$       o$$$  o$
                                  $$ooooo$$  $  o$
                        o$ $ $     $ $$$   $  $
                      o$        $o    $$$   $   $
                     $$  $ $ $   $$$o$$    o  o$$
                     $$  o $ $   $$ $   o$  $$
                     $o  $ $  $  o$$   o$  o$$
                      $$o    $$  $   o$  o$$$
                       $o$o$$$  $oo$  o$$
                        o$$ $   $$$  o$$
                        o$ o oo$  $ $$o
                       o$o$ $          $
                      $$ $ o$   $ $ $   $o
                     $$ $  $  o$ o$o $   $
                    o$ $  $  o$$ $  $   $
                    o  $ $$  $ $o      o$
                    $ o         $o$oo$$
                   $o $   o  o  o$$$
                   $o  o  $  $    $$o
                   $o  $   o  $  $ $o
                    $  $   $o  $  $o$$o
                    $   $   o   $   o $$
            $o$o$o$o$$o$$$o$$o$o$$o$$o$$$o$o$o$o$o$o$o$o$o$ooo
            $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o
            $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$   $ $$$$$
            $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$      $$$$$
            $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$       $$$$
            $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$       $$$$
            $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$       $$$$
            $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     o$$$$$
            $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ooooo$$$$
            $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
            $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
            $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
            $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
            $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
            $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
            $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$o$o$o$o$o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
       """""""""""""""""""""""""""""""""""""""""""""""""""""
""

menu_thanks_message = "Thanks for your choice! "
error_message = "Sorry, that is not an option. Please use one of the menu options. "

main_menu_message = """
--- MAIN MENU ---

Welcome to BrIWer v1! Please choose an option from the below list:

    [1] Get a list
    [2] Add to a list
    [3] Remove from a list
    [4] Exit

"""

list_menu_message = f"""
--- VIEW A LIST ---

{menu_thanks_message}Please choose an option from the below menu:

    [1] List of people
    [2] List of drinks
    [3] Exit to main menu

"""

add_menu_message = f"""
--- ADD TO A LIST ---

{menu_thanks_message}Please choose an option from the below menu:

    [1] Add people
    [2] Add drinks
    [3] Exit to main menu

"""
add_name_message = f"""
--- ADD A NAME ---

{menu_thanks_message}Please type a name to add to the list of people.

    e.g.    Danny, Paul, Phil

The current list of people is:

    {people}

Enter name here: """
add_drink_message = f"""
--- ADD A DRINK ---

{menu_thanks_message}Please type a drink to add to the list of drinks.

    e.g.    Beer, Coffee, Milk

The current list of drinks:

    {drinks}

Enter drink here: """

remove_menu_message = f"""
--- REMOVE AN ITEM ---

{menu_thanks_message}Please choose an option from the below menu:

    [1] Remove people
    [2] Remove drinks
    [3] Exit to main menu

"""
remove_name_message = f"""
--- REMOVE A NAME ---

{menu_thanks_message}Please type a name to remove it from the current the list of people. The current list of people is:

    {people}

Enter name here: """
remove_drink_message = f"""
--- REMOVE A DRINK ---

{menu_thanks_message}Please type a drink to remove it from the current the list of drinks. The current list of drinks is:

    {drinks}

Enter drink here: """

main_menu()

# MAIN CODE
# outer_setting = True
# while outer_setting == True:
#     clear()
#     mid_setting = True
#     choice = int(input(coffee_cup_ascii + main_menu))
#     while mid_setting == True:
#         if choice == 1:
#             inner_choice = int(input(coffee_cup_ascii + list_menu_message))
#             view_list(choice)
#             if inner_choice == 1 or inner_choice == 2:
#                 input("\nPress Enter to return to the previous menu.")
#             elif inner_choice == 3:
#                 mid_setting = False
#             clear()
#         elif choice == 2:
#             inner_choice = int(input(coffee_cup_ascii + add_menu_message))
#             add_an_item()
#             if inner_choice == 1 or inner_choice == 2:
#                 input("\nPress Enter to return to the previous menu.")
#             elif inner_choice == 3:
#                 mid_setting = False
#             clear()
#         elif choice == 3:
#             inner_choice = int(input(coffee_cup_ascii + remove_menu_message))
#             remove_an_item()
#             if inner_choice == 1 or inner_choice == 2:
#                 input("\nPress Enter to return to the previous menu.")
#             elif inner_choice == 3:
#                 mid_setting = False
#         elif choice == 4:
#             clear()
#             print(coffee_cup_ascii)
#             input("Thank you for using BrIWer v1!")
#             clear()
#             exit()
#         else:
#             clear()
#             print(error_message)
#     mid_setting = True

# #Need to have the names/drinks written on to a file and the file saved (the file will save and be written once it is closed).
# #Also need to have a way of reading the file to return the lists as a list.

# #Use '.strip()' to remove white space in saved file and check the list for empty strings by comparing entries to len == 0. If () of strip contains characters, these will be removed.