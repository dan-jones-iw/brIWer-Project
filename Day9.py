import sys
import os
import time
import traceback
arguments = sys.argv
print(arguments)

# FUNCTIONS


def main_menu():
    main_menu = True
    while main_menu == True:
        clear()
        choice = int(input(logo_ascii + main_menu_message))
        inner_menu = True
        while inner_menu == True:
            people = populate_list("people.txt")
            drinks = populate_list("drinks.txt")
            if choice == 1:
                list_menu(inner_menu, people, drinks)
                inner_menu = False
            elif choice == 2:
                add_menu(inner_menu, people, drinks)
                inner_menu = False
            elif choice == 3:
                remove_menu(inner_menu, people, drinks)
                inner_menu = False
            elif choice == 4:
                add_fave_drink(people, drinks)
                inner_menu = False
            elif choice == 5:
                create_round_menu()
                inner_menu = False
            elif choice == 6:
                end_thanks()
                exit()

def list_menu(inner_menu, people, drinks):
    menu = inner_menu
    while menu == True:
        try:
            clear() 
            choice = int(input(logo_ascii + list_menu_message))
            view_list(choice, people, drinks)
            if choice == 1 or choice == 2:
                input("\nPress Enter to return to the previous menu.")
            elif choice == 3:
                menu = False
        except:
            clear()
            input(logo_ascii + "\n" + "Please type a number! Press Enter to return to the menu.")

def add_menu(inner_menu, people, drinks):
    menu = inner_menu
    while menu == True:
        try:
            clear()
            choice = int(input(logo_ascii + add_menu_message))
            add_an_item(choice, people, drinks)
            if choice == 1 or choice == 2:
                input("\nPress Enter to return to the previous menu.")
            elif choice == 3:
                menu = False
        except:
            clear()
            input(logo_ascii + "\n" + "Please type a number! Press Enter to return to the menu.")

def remove_menu(inner_menu, people, drinks):
    menu = inner_menu
    while menu == True:
        try:
            clear()
            choice = int(input(logo_ascii + remove_menu_message))
            remove_an_item(choice, people, drinks)
            if choice == 1 or choice == 2:
                input("\nPress Enter to return to the previous menu.")
            elif choice == 3:
                menu = False
        except:
            clear()
            input(logo_ascii + "\n" + "Please type a number! Press Enter to return to the menu.")

#Print the current list of people & drinks. Ask for which person to add a fave (i)person on list or (ii)new person (if new person, new person needs to be added to list)
#Which drink is to be matched? Match person and drink in dictionary. Add functionality to choose a fave drink TYPE (e.g. hot, milky, cold, fizzy etc) instead of drinks list.
def add_fave_drink(people, drinks):
    longest_name = measure_biggest_length(people)
    longest_drink = measure_biggest_length(drinks)
    print(logo_ascii)
    print(f"The current list of people and drinks is: \n")
    print(f"+{'=' * (longest_name + 4)}+{'=' * (longest_drink + 4)}+")
    print_two_lists(people, drinks)
    print(f"+{'=' * (longest_name + 4)}+{'=' * (longest_drink + 4)}+")
    person = input("")

#Use createRound class.
def create_round_menu():
    return

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

def print_two_lists(people, drinks):
    longest_name = measure_biggest_length(people)
    longest_drink = measure_biggest_length(drinks)
    combined_list = []
    space = " "
    for person in people:
        length_of_name = len(person)
        required_spaces = longest_name - length_of_name
        string = ("|  " + person + (space * required_spaces) + "  |  ")
        combined_list.append(string)
    position = 1
    for drink in drinks:
        length_of_name = len(drink)
        required_spaces = longest_drink - length_of_name
        string = (drink + (space * required_spaces) + "  |")
        combined_list.insert(position, string)
        position += 2
    for item in range(0, len(combined_list), 2):
        print(combined_list[item] + combined_list[item + 1])


def view_list(choice, people, drinks):    
    clear()
    print(logo_ascii)
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

def input_cleaner(input_str):
    word_list = input_str.split(",")
    for index in range(0, len(word_list)):
        word = word_list[index].strip()
        word = word.strip("'")
        word = word.strip('"')
        word_list[index] = word
    return word_list
        
def add_an_item(choice, people, drinks):
    if choice == 1:
        clear()
        print(logo_ascii + "\n")
        add_name_message(people)
        added_names = input()
        added_names = input_cleaner(added_names)
        people += added_names
        rewrite_file("people.txt", people)
        clear()
        print(logo_ascii)
        print("Name added!\n")
        print("The current list of people is: \n")
        print(people)
    elif choice == 2:
        clear()
        print(logo_ascii + "\n")
        add_drink_message(drinks)
        added_drinks = input()
        added_drinks = input_cleaner(added_drinks)
        drinks += added_drinks
        rewrite_file("drinks.txt", drinks)
        clear()
        print(logo_ascii)
        print("Drink added!\n")
        print("The current list of drinks is: \n")
        print(drinks)
    elif choice == 3:
        pass
    else:
        print(error_message)


def file_error_handler(exception):
    clear()
    error_length = len(str(exception))
    print(logo_ascii)
    print("There has been an error!\n")
    print(f"+{'=' * error_length}+")
    print(" " + str(exception))
    print(f"+{'=' * error_length}+")


# THIS STINKS ----- not anymore :)
def remove_an_item(choice, people, drinks):
    if choice == 1:
        clear()
        print(logo_ascii + "\n")
        remove_name_message(people)
        removed_names = input()
        people.remove(removed_names)
        try:
            rewrite_file("people.txt", people)
        except FileNotFoundError as e:
            file_error_handler(e)
        clear()
        print(logo_ascii)
        print("Name removed!\n")
        print("The updated list of people is: \n")
        print(people)
    elif choice == 2:
        clear()
        print(logo_ascii + "\n")
        remove_drink_message(drinks)
        removed_drinks = input()
        people.remove(removed_drinks)
        try:
            rewrite_file("drinks.txt", drinks)
        except FileNotFoundError as e:
            file_error_handler(e)
        clear()
        print(logo_ascii)
        print("Drink removed!\n")
        print("The updated list of drinks is: \n")
        print(drinks)
    elif choice == 3:
        pass
    else:
        print(error_message)

def populate_list(filepath):
    list_of_items = []
    try:
        with open(filepath, 'r') as items_file:
            for lines in items_file.readlines():
                list_of_items.append(lines.strip("\n"))
            items_file.close()
            return list_of_items
    except:
        print("Failed to open file!")

def rewrite_file(filepath, list_of_items):
    try:
        with open(filepath, 'w') as items_file:
            for item in list_of_items:
                items_file.write(item + "\n")
    except:
        print("Failed to open file!")

def measure_biggest_length(list_of_items):
    biggest_length = 0
    for item in list_of_items:
        length = len(item)
        if length > biggest_length:
            biggest_length = length
        else:
            pass
    return biggest_length

# for i, v in enumerate([list_of_items])

#IMPORT INFORMATION FROM TEXT FILE
people = populate_list("people.txt")
drinks = populate_list("drinks.txt")

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
    [4] Add a favourite drink
    [5] Create a round
    [6] Exit
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

def add_name_message(people):
    print(f"""\n--- ADD A NAME ---\n\n{menu_thanks_message}Please type the name(s) of people you want to add to the list.\n
    Please make sure that each name is separated by a comma and a space when adding multiple people.
        e.g. Danny, Paul, Phil\n""")
    print_list(people, "people")
    print("""\nEnter name here: """)

def add_drink_message(drinks):
    print(f"""\n--- ADD A DRINK ---\n\n{menu_thanks_message}Please type the drink(s) which you would like to add to the list.\n
    Please make sure that each drink is separated by a comma and a space when adding multiple drinks.
        e.g. Beer, Water, Mocha\n""")
    print_list(drinks, "drinks")
    print("""\nEnter drink here: """)

remove_menu_message = f"""\n--- REMOVE FROM A LIST ---\n\n{menu_thanks_message}Please choose an option from the below menu:\n
    [1] Remove people
    [2] Remove drinks
    [3] Exit to main menu
\n"""

def remove_name_message(people):
    print(f"""\n--- REMOVE A NAME ---\n\n{menu_thanks_message}Please type a name to remove it from the current the list of people.""")
    print_list(people, "people")
    print("""\n\nEnter name here: """)

def remove_drink_message(drinks):
    print(f"""\n--- REMOVE A DRINK ---\n\n{menu_thanks_message}Please type a drink to remove it from the current the list of drinks.""")
    print_list(drinks, "drinks")
    print("""\n\nEnter drink here: """)

main_menu()