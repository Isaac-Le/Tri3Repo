# Tri3Repo
| [Home Page](https://isaac-le.github.io/Tri3Repo/) | [Test Prep](https://isaac-le.github.io/Tri3Repo/testprep) | Joe biden |
|--------------------------------------------------|-----------------------|---------------------|

# Data Structures
### [Replit Link](https://replit.com/@IsaacLe2/Tri3Repo#main.py)


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
