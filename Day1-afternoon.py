import sys
arguments = sys.argv
print(arguments)

def loop(arg):
    list_of_items = {
    "people": {"Danny", "David", "John"}, 
    "drinks": {"Beer", "Coffee", "Milk"}
    }
    for item in list_of_items:
        print(f"+{'=' * 15}+")
        print("| " + item, list_of_items[arg])
        print(f"+{'=' * 15}+")

if  arguments[1] == "get-people" or arguments[1] == "get-p":
    arg = "people"
    loop(arguments[1])
elif arguments[1] == "get-drinks" or arguments[1] == "get-d":
    arg = "drinks"
    loop(arguments[1])
else:
    print("What do you want from me? I can only tell you people and drinks. Use 'get-people' or 'get-drinks'.")