import sys
arguments = sys.argv
print(arguments)

import os
import time
import traceback

#FUNCTIONS

def main_menu():
    main_menu = True
    while main_menu == True:
        clear()
        choice = int(input(logo_ascii + main_menu_message))
        inner_menu = True
        while inner_menu == True:
            people_dictionary = get_dict_from_file("people.txt")
            people_list = get_list_from_dict(people_dictionary)
            drinks_dictionary = get_dict_from_file("people.txt")
            drinks_list = get_list_from_dict(drinks_dictionary)
            if choice == 1:
                list_menu(inner_menu, people_list, drinks_list)
                inner_menu = False
            elif choice == 2:
                add_menu(inner_menu, people_list, drinks_list)
                inner_menu = False
            elif choice == 3:
                remove_menu(inner_menu, people_list, drinks_list)
                inner_menu = False
            elif choice == 4:
                create_round_menu()
            elif choice == 5:
                end_thanks()
                exit()
        else:
            clear()
            print(error_message)

def list_menu(inner_menu, people_list, drinks_list):
    menu = inner_menu
    while menu == True:
        clear()
        try:  
            choice = int(input(logo_ascii + list_menu_message))
        except:
            print("Please type a number!")
        view_list(choice, people_list, drinks_list)
        if choice == 1 or choice == 2:
            input("\nPress Enter to return to the previous menu.")
        elif choice == 3:
            menu = False
        else:
            clear()
            print(error_message)

def add_menu(inner_menu, people_list, drinks_list):
    menu = inner_menu
    while menu == True:
        clear()
        choice = int(input(logo_ascii + add_menu_message))
        add_an_item(choice, people_list, drinks_list)
        if choice == 1 or choice == 2:
            input("\nPress Enter to return to the previous menu.")
        elif choice == 3:
            menu = False
        else:
            clear()
            print(error_message)

def remove_menu(inner_menu, people_list, drinks_list):
    menu = inner_menu
    while menu == True:
        clear()
        choice = int(input(logo_ascii + remove_menu_message))
        remove_an_item(choice, people_list, drinks_list)
        if choice == 1 or choice == 2:
            input("\nPress Enter to return to the previous menu.")
        elif choice == 3:
            menu = False
        else:
            clear()
            print(error_message)

def create_round_menu():
    return

def exit_to_menu():
    pass

def clear():
    os.system("clear")

def end_thanks():
    clear()
    print(f"""{logo_ascii} 
                     ┌┐ ┬─┐╦╦ ╦┌─┐┬─┐
    Thanks for using ├┴┐├┬┘║║║║├┤ ├┬┘ v1!
                     └─┘┴└─╩╚╩╝└─┘┴└─""")
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

def view_list(choice, people_list, drinks_list):    
    clear()
    print(logo_ascii)
    if  choice == 1:
        arg = people_list
        list_name = "people"
        print_list(arg, list_name)
    elif choice == 2:
        arg = drinks_list
        list_name = "drinks"
        print_list(arg, list_name)
    elif choice == 3:
        pass
    else:
        print(error_message)

def input_cleaner(input_str):
    word_list = input_str.split(",")
    for index in range(0, len(word_list)):
        word = word_list[index].strip()
        word = word.strip("'")
        word = word.strip('"')
        word_list[index] = word
    return word_list
        
def add_an_item(choice, people_list, drinks_list):
    if choice == 1:
        clear()
        print(logo_ascii + "\n")
        add_name_message(people_list)
        added_names = input()
        added_names = input_cleaner(added_names)
        people_list += added_names
        people_dictionary = create_dict_key(people_list)
        save_by_rewrite("people.txt", people_dictionary)
        clear()
        print(logo_ascii)
        print("Name added!\n")
        print("The current list of people is: \n")
        print(people_list)
    elif choice == 2:
        clear()
        print(logo_ascii + "\n")
        add_drink_message(drinks_list)
        added_drinks = input()
        added_drinks = input_cleaner(added_drinks)
        drinks_list += added_drinks
        drinks_dictionary = create_dict_key(drinks_list)
        save_by_rewrite("people.txt", drinks_dictionary)
        clear()
        print(logo_ascii)
        print("Drink added!\n")
        print("The current list of drinks is: \n")
        print(drinks_list)
    elif choice == 3:
        pass
    else:
        print(error_message)

def remove_an_item(choice, people_list, drinks_list):
    try:
        if choice == 1:
            clear()
            print(logo_ascii + "\n")
            remove_name_message(people_list)
            removed_names = input()
            people_list.remove(removed_names)
            people_dictionary = create_dict_key(people_list)
            save_by_rewrite("people.txt", people_dictionary)
            clear()
            print(logo_ascii)
            print("Name removed!\n")
            print("The updated list of people is: \n")
            print(people_list)
        elif choice == 2:
            clear()
            print(logo_ascii + "\n")
            remove_drink_message(drinks_list)
            removed_drinks = input()
            drinks_list.remove(removed_drinks)
            drinks_dictionary = create_dict_key(drinks_list)
            save_by_rewrite("drinks.txt", drinks_dictionary)
            clear()
            print(logo_ascii)
            print("Drink removed!\n")
            print("The updated list of drinks is: \n")
            print(drinks_list)
        elif choice == 3:
            pass
        else:
            print(error_message)
    except Exception as e:
        clear()
        error_length = len(str(e))
        print(logo_ascii)
        print("There has been an error!\n")
        print(f"+{'=' * (error_length)}+")
        print(" " + str(e))
        print(f"+{'=' * (error_length)}+")

def get_dict_from_file(filepath):
    dictionary_of_items = {}
    try:
        with open(filepath, 'r') as items_file:
            for lines in items_file.readlines():
                list_from_file = []
                list_from_file.append(lines.strip("\n"))
                for item in list_from_file:
                    key = item.rstrip("|")
                    value = item.lstrip("|")
                    dictionary_of_items[key] = [value]
            items_file.close()
            return dictionary_of_items
    except:
        print("Failed to open file!")

def get_list_from_dict(dictionary_of_items):
    list_of_items = []
    for key, value in dictionary_of_items:
        list_of_items.append(value)
    return list_of_items

def save_by_rewrite(filepath, dictionary_of_items):
    try:
        list_from_dict = []
        for key, value in dictionary_of_items:
            list_from_dict.append(key + "|" + value)
        with open(filepath, 'w') as items_file:
            for item in list_from_dict:
                items_file.write(item + "\n")
    except:
        print("Failed to open file!")

# for i, v in enumerate([list_from_file])

#IMPORT INFORMATION FROM TEXT FILE
people_dictionary = get_dict_from_file("people.txt")
people_list = get_list_from_dict(people_dictionary)
drinks_dictionary = get_dict_from_file("people.txt")
drinks_list = get_list_from_dict(drinks_dictionary)

#MESSAGES & DESIGN
logo_ascii = """
bbbbbbbb                                                                                                                       
b######b                              IIIIIIIIIIWWWWWWWW                           WWWWWWWW                                    
b######b                              I########IW######W                           W######W                                    
b######b                              I########IW######W                           W######W                                    
 b####:b                              II######IIW######W                           W######W                                    
 b####:bbbbbbbbb    rrrrr   rrrrrrrrr   I####I   W####:W           WWWWW           W####:W eeeeeeeeeeee    rrrrr   rrrrrrrrr   
 b##############bb  r####rrr########:r  I####I    W####:W         W####:W         W####:Wee############ee  r####rrr########:r  
 b################b r################:r I####I     W####:W       W######:W       W####:We######eeeee####:eer################:r 
 b####:bbbbb######:brr######rrrrr######rI####I      W####:W     W########:W     W####:We######e     e####:err######rrrrr######r
 b####:b    b######b r####:r     r####:rI####I       W####:W   W####:W####:W   W####:W e######:eeeee######e r####:r     r####:r
 b####:b     b####:b r####:r     rrrrrrrI####I        W####:W W####:W W####:W W####:W  e################:e  r####:r     rrrrrrr
 b####:b     b####:b r####:r            I####I         W####:W####:W   W####:W####:W   e######eeeeeeeeeee   r####:r            
 b####:b     b####:b r####:r            I####I          W########:W     W########:W    e######:e            r####:r            
 b####:bbbbbb######b r####:r          II######II         W######:W       W######:W     e########e           r####:r            
 b################b  r####:r          I########I          W####:W         W####:W       e########eeeeeeee   r####:r            
 b##############:b   r####:r          I########I           W##:W           W##:W         ee############:e   r####:r            
 bbbbbbbbbbbbbbbb    rrrrrrr          IIIIIIIIII            WWW             WWW            eeeeeeeeeeeeee   rrrrrrr            
"""
menu_thanks_message = "Thanks for your choice! "
error_message = "Sorry, that is not an option. Please use one of the menu options. "

main_menu_message = """\n
           ┌┐ ┬─┐╦╦ ╦┌─┐┬─┐
Welcome to ├┴┐├┬┘║║║║├┤ ├┬┘ v1! Please choose an option from the below list:
           └─┘┴└─╩╚╩╝└─┘┴└─
\n--- MAIN MENU ---\n
    [1] Get a list
    [2] Add to a list
    [3] Remove from a list
    [4] Create a round
    [5] Exit
\n"""

list_menu_message = f"""\n--- VIEW A LIST ---\n\n{menu_thanks_message}Please choose an option from the below menu:\n
    [1] List of people
    [2] List of drinks
    [3] Exit to main menu
\n"""

add_menu_message = f"""\n--- ADD TO A LIST ---\n\n{menu_thanks_message}Please choose an option from the below menu:\n
    [1] Add people
    [2] Add drinks
    [3] Exit to main menu
\n"""

def add_name_message(people_list):
    print(f"""\n--- ADD A NAME ---\n\n{menu_thanks_message}Please type the name(s) of people you want to add to the list.\n
    Please make sure that each name is separated by a comma and a space when adding multiple people.
        e.g. Danny, Paul, Phil\n""")
    print_list(people_list, "people")
    print("""\nEnter name here: """)

def add_drink_message(drinks_list):
    print(f"""\n--- ADD A DRINK ---\n\n{menu_thanks_message}Please type the drink(s) which you would like to add to the list.\n
    Please make sure that each drink is separated by a comma and a space when adding multiple drinks.
        e.g. Beer, Water, Mocha\n""")
    print_list(drinks_list, "drinks")
    print("""\nEnter drink here: """)

remove_menu_message = f"""\n--- REMOVE AN ITEM ---\n\n{menu_thanks_message}Please choose an option from the below menu:\n
    [1] Remove people
    [2] Remove drinks
    [3] Exit to main menu
\n"""

def remove_name_message(people_list):
    print(f"""\n--- REMOVE A NAME ---\n\n{menu_thanks_message}Please type a name to remove it from the current the list of people.""")
    print_list(people_list, "people")
    print("""\n\nEnter name here: """)

def remove_drink_message(drinks_list):
    print(f"""\n--- REMOVE A DRINK ---\n\n{menu_thanks_message}Please type a drink to remove it from the current the list of drinks.""")
    print_list(drinks_list, "drinks")
    print("""\n\nEnter drink here: """)

main_menu()