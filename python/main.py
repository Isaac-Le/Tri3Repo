# Main list of [Prompts, Actions]
# Two styles are supported to execute abstracted logic
# 1. file names will be run by exec(open("filename.py").read())
# 2. function references will be executed directly file.function()
from week0 import amongus, keypad, swap, tree
from week1 import datalists, fibonacci
from week2 import factorial, imperative_math, oop_math
from crossover import palindrome, factor, prime

main_menu = [
    ["Swap", swap.ageswap],
    ["Tree", tree.tree_run],
    ["Fibonacci", fibonacci.fibonacci_run],
    ["Datalists", datalists.main]
]

# Submenu list of [Prompt, Action]
# Works similarly to main_menu
sub_menu = [
    ["Among Us", amongus.ship],
    ["Keypad", keypad.keypad],
    ["Factorial", factorial.factorial_run],
    ["Greatest Common Denominator", imperative_math.gcd_run],
    ["OOP Math", oop_math.gcd_run],
    ["Palindrome Function", palindrome.menu],
    ["Factor Finding Function", factor.factorsmenu],
    ["Prime Number Function", prime.menu]

]

border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"


def menuc():
    title = "Class Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Submenu", submenuc])
    m = questy.Menu(title, menu_list)
    m.menu()  


def submenuc():
    title = "Class Submenu" + banner
    m = questy.Menu(title, sub_menu)
    m.menu()


def menu():
    title = "Function Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Submenu", submenu])
    buildMenu(title, menu_list)


def submenu():
    title = "Function Submenu" + banner
    buildMenu(title, sub_menu)

def buildMenu(banner, options):

    print(banner)

    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op


    for key, value in prompts.items():
        print(key, '->', value[0])
    choice = input("Type your choice> ")

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

    buildMenu(banner, options)  

if __name__ == "__main__":
    menu()
