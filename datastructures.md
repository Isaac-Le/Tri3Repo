{% include navbar.html %}

# Data Structures
### [Replit Link](https://replit.com/@IsaacLe2/Tri3Repo#main.py)   
(Replit Embed at the Bottom)

    
### This is my menu code

``` 
main_menu = [
    ["Swap", "swap.py"],
    ["Tree", "tree.py"]
]

sub_menu = [
    ["Among Us", "amongus.py"],
    ["Keypad", "keypad.py"]
]


# Menu banner is typically defined by menu owner
border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"


def menuc():
    title = "Class Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Submenu", submenuc])
    m = questy.Menu(title, menu_list)
    m.menu()  # method and data reside in object


# def submenuc
# using sub_menu list:
# submenuc works similarly to menuc
def submenuc():
    title = "Class Submenu" + banner
    m = questy.Menu(title, sub_menu)
    m.menu()


# def menu
# using main_menu list:
# 1. main menu and submenu reference are created [Prompts, Actions]
# 2. menu_list is sent as parameter to menuy.menu function that has logic for menu control
def menu():
    title = "Function Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Submenu", submenu])
    buildMenu(title, menu_list)

# def submenu
# using sub menu list above:
# sub_menu works similarly to menu()
def submenu():
    title = "Function Submenu" + banner
    buildMenu(title, sub_menu)

def buildMenu(banner, options):
    # header for menu
    print(banner)
    # build a dictionary from options
    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op

    # print menu or dictionary
    for key, value in prompts.items():
        print(key, '->', value[0])

    # get user choice
    choice = input("Type your choice> ")

    # validate choice and run
    # execute selection
    # convert to number
    try:
        choice = int(choice)
        if choice == 0:
            return
        try:
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:  
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")
    except ValueError:
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        print(f"Invalid choice: {choice}")

    buildMenu(banner, options)  # recursion, start menu over again


if __name__ == "__main__":
    menu()
    #menuc() 
```
    
### This is my datalists code
* There is an open list wher we will make a dictionary and input the data into the list
* Then we extract the data from the dictionary and the list and we print the data out in either a for loop, while loop, and recursion 
    
```
    InfoDb = []
# List with dictionary placed in a list  
InfoDb.append({  
               "FirstName": "Isaac",  
               "LastName": "Le",  
               "DOB": "May 27",  
               "Residence": "San Diego",  
               "Email": "isaacl51471@stu.powayusd.com",  
               "Owns_Cars":["1998 Lexus es300", "2022 Toyota Prius", "2018 Toyota Sienna"]  
              })  

InfoDb.append({  
               "FirstName": "Louis",  
               "LastName": "Le",  
               "DOB": "July 10",  
               "Residence": "San Diego",  
               "Email": "louisl39859@powayusd.com",  
               "Owns_Cars":["A","B","C"]  
              })  
# for loop iterates on length of InfoDb
def print_data(n):
    print(InfoDb[n]["FirstName"], InfoDb[n]["LastName"])  # using comma puts space between values
    print("\t", "Cars: ", end="")  # \t is a tab indent, end="" make sure no return occurs
    print(", ".join(InfoDb[n]["Owns_Cars"]))  # join allows printing a string list with separator
    print()
    
```

<iframe frameborder="0" width="100%" height="500px" src="https://replit.com/@IsaacLe2/Tri3Repo?embed=true" > 
