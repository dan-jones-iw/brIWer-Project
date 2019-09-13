import sys
arguments = sys.argv
print(arguments)

import os
import traceback

people_file = open("people.txt", "w")
people_file.close()
drinks_file = open("drinks.txt", "w")
drinks_file.close()
people = []
drinks = []
favourite_drinks = {}
#favourite_drinks = {"Danny": "Beer", "David": "Coffee", "John": "Milk"}
#people = favourites_list.keys()
#drinks = favourites_list.values()

#MESSAGES & DESIGN
coffee_cup_ascii = ("""
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
"")
welcome = "Welcome to BrIWer v1! "
main_menu = """
--- MAIN MENU ---

Please choose an option from the below list:

    [1] Get a list
    [2] Add to a list
    [3] Remove from a list
    [4] Exit

"""
menu_thanks = "Thanks for your choice! "
error = "Sorry, that is not an option. Please use one of the menu options. "
list_view_menu = f"""
--- VIEW A LIST ---

{(menu_thanks)}Please choose an option from the below menu:

    [1] List of people
    [2] List of drinks
    [3] Exit to main menu

"""
list_remove_menu = f"""
--- REMOVE AN ITEM ---

{(menu_thanks)}Please choose an option from the below menu:

    [1] Remove people
    [2] Remove drinks
    [3] Exit to main menu

"""
list_add_menu = f"""
--- ADD TO A LIST ---

{(menu_thanks)}Please choose an option from the below menu:

    [1] Add people
    [2] Add drinks
    [3] Exit to main menu

"""
add_name = f"""
--- ADD A NAME ---

{(menu_thanks)}Please type a name to add to the list of people.

    e.g.    Danny, Paul, Phil

The current list of people is:

    {(people)}

Enter name here: """
remove_name = f"""
--- REMOVE A NAME ---

{(menu_thanks)}Please type a name to remove it from the current the list of people. The current list of people is:

    {(people)}

Enter name here: """
add_drink = f"""
--- ADD A DRINK ---

{(menu_thanks)}Please type a drink to add to the list of drinks.

    e.g.    Beer, Coffee, Milk

The current list of drinks:

    {(drinks)}

Enter drink here: """
remove_drink = f"""
--- REMOVE A DRINK ---

{(menu_thanks)}Please type a drink to remove it from the current the list of drinks. The current list of drinks is:

    {(drinks)}

Enter drink here: """

#FUNCTIONS
def clear():
    os.system("clear")

def print_list(arg):
    print("The current list of people is: \n")
    print(f"+{'=' * 18}+")
    for item in arg:
        spaces = (17 - len(item))
        print("| " + item + f"{' ' * spaces}" + "|")
    print(f"+{'=' * 18}+")

def view_a_list():    
    clear()
    print(coffee_cup_ascii)
    if  inner_choice == 1:
        arg = people
        print_list(arg)
    elif inner_choice == 2:
        arg = drinks
        print_list(arg)
    elif inner_choice == 3:
        pass
    else:
        print(error)

#NEED TO ADD APPEND-ONLY FOR ADD ITEM FUNCTION
def add_an_item():
    if inner_choice == 1:
        clear()
        added_name = str(input(coffee_cup_ascii + "\n" + add_name))
        people.append(added_name)
        #INSERT SAVE FUNCTION HERE?
        clear()
        print(coffee_cup_ascii)
        print("Name added!\n")
        print("The current list of people is: \n")
        print(people)
    elif inner_choice == 2:
        clear()
        added_drink = str(input(coffee_cup_ascii + "\n" + add_drink))
        drinks.append(added_drink)
        #INSERT SAVE FUNCTION HERE?
        clear()
        print(coffee_cup_ascii)
        print("Drink added!\n")
        print("The current list of drinks is: \n")
        print(drinks)
    elif inner_choice == 3:
        pass
    else:
        print(error)

#NEED TO ADD WRITE TO FILE FOR REMOVE AN ITEM FUNCTION 
def remove_an_item():
    try:
        if inner_choice == 1:
            clear()
            removed_name = str(input(coffee_cup_ascii + "\n" + remove_name))
            people.remove(removed_name)
            #INSERT SAVE FUNCTION HERE?
            clear()
            print(coffee_cup_ascii)
            print("Name removed!\n")
            print("The updated list of people is: \n")
            print(people)
        elif inner_choice == 2:
            clear()
            removed_drink = str(input(coffee_cup_ascii + "\n" + remove_drink))
            people.remove(removed_drink)
            #INSERT SAVE FUNCTION HERE?
            clear()
            print(coffee_cup_ascii)
            print("Drink removed!\n")
            print("The updated list of drinks is: \n")
            print(drinks)
        elif inner_choice == 3:
            pass
        else:
            print(error)
    except Exception as e:
        clear()
        print(coffee_cup_ascii)
        print("There has been an error!")
        print(f"+{'=' * 18}+")
        print(str(e))
        print(f"+{'=' * 18}+")

def populate_list(filepath, list_of_items):
    list_of_items = []
    items_file = open(filepath, "r")
    for lines in items_file.readlines():
        list_of_items.append(lines)
    items_file.close()
    return list_of_items

def save_items(filepath, list_of_items):
    try:
        with open(file_name, 'w') as items_file:
            for item in list_of_items:
                items_file.write(item + "\n")
    except:
        print("Failed to open file!")

#MAIN CODE
people = populate_list("people.txt", people)
drinks = populate_list("drinks.txt", drinks)
outer_setting = True
while outer_setting == True:
    clear()
    mid_setting = True
    choice = int(input(coffee_cup_ascii + main_menu))
    while mid_setting == True:
        if choice == 1:
            inner_choice = int(input(coffee_cup_ascii + list_view_menu))
            view_a_list()
            if inner_choice == 1 or inner_choice == 2:
                input("\nPress Enter to return to the previous menu.")
            elif inner_choice == 3:
                mid_setting = False
            clear()
        elif choice == 2:
            inner_choice = int(input(coffee_cup_ascii + list_add_menu))
            add_an_item()
            if inner_choice == 1 or inner_choice == 2:
                input("\nPress Enter to return to the previous menu.")
            elif inner_choice == 3:
                mid_setting = False
            clear()
        elif choice == 3:
            inner_choice = int(input(coffee_cup_ascii + list_remove_menu))
            remove_an_item()
            if inner_choice == 1 or inner_choice == 2:
                input("\nPress Enter to return to the previous menu.")
            elif inner_choice == 3:
                mid_setting = False
        elif choice == 4:
            clear()
            print(coffee_cup_ascii)
            input("Thank you for using BrIWer v1!")
            clear()
            exit()
        else:
            clear()
            print(error)
    mid_setting = True

#Need to have the names/drinks written on to a file and the file saved (the file will save and be written once it is closed).
#Also need to have a way of reading the file to return the lists as a list.

#Use '.strip()' to remove white space in saved file and check the list for empty strings by comparing entries to len == 0. If () of strip contains characters, these will be removed.