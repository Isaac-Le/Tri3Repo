# Tri3Repo
## [Home Wiki Page](https://github.com/Isaac-Le/Tri3Repo/wiki)
## [Github Pages](https://isaac-le.github.io/Tri3Repo/)
# Test Prep
## 5.1 Notes

* Accelerometer used in Wiis, iPhones, Drones, automobiles, etc.
* Multirotor
> * Benefits - Deliveries, finding lost people, aerial photography is easy
> * Harmful - Flying in unregulated zones is illegal and dangerous, privacy concerns 
* Wii controller
> * Benefits - Gets people active playing video games
> * Harmful - Broken TV’s and injuries
* 3D Printers
> * Open-source software for the computer and printer
> * In schools and homes
> * Special 3D printers can make
> > * Organs/Prosthetics
> > * Houses
> > * Shoes and jewelry
> > * Themselves

* In first System the user hears the lists of departments and selects one on their phone which can lead to error
* In second system the customer describes the issue, while the system tries to identify the issue, so we can assume it will work as intended unless stated otherwise

5.1 Video 2: Beneficial and Harmful Effects

Ex:
* The Internet - Originally for Scientists
> * Many people now spend more time on internet and sleeping
> * What if you didn’t have the WWW
> * Dopamine feedback loops, is you trying to seek out that sense of happiness and pleasure, but it can lead to sleep deprivation, depression, anxiety, impulsivity, etc.
* Microtransactions
> * “Free” Games/Apps
> * Cosmetics, paywall to functionality, sometimes pay-to-win
> * Gold, V-bucks, coins, “chips”, SBUX
> * Loot Boxes - Banned in some countries

## Github pages action
### 1. **Benefits**: Automation of certain tasks, Accurate compared to the factor of human error, Fast communication
### **Harmfulness**: Prolonged use can cause poor health, Everyone's information is on the web, less social interaction
### 2. Dopamine issues are a real thing. Some people stick onto and stay on a computer for so long that it becomes attached to them and is one with them. They wire their brain to see the computer as something that gives them happiness leading to depression outside of the computer. Some people get so focused in on obtaining that dopamine and that happy feeling making the computer almost like a drug to them. I have been victim to this my self a couple of times and it isn't good for the mind or the body.
 
## 5.2 Notes

* The digital divide refers to differing access to computing devices and the internet, based on;
> * Socioeconomic
> > * How much money comes into the household per year
> * Geographic
> > * Depending on your area of residence, ISPs may not provide high speed internet to your home
> * Demographic characteristics
> > * Age
> > > * If you are older, you may not have devices in your household
> > * Religion
> > > * Example: the Amish People

* Some countries
> * Have rural areas where computers are not common
> * Only allow you to visit a limited number of websites
> * The internet is used to protect and advocate for the government
> * High level of surveillance on the internet to protect the government

## Github pages action
### 1. People empower themselves in a digital world by first having access to the digital world, and then using the information and tools that they have obtained from this digital world to benefit themselves or others.
### 2. Someone that is empowered can help someone that is not empowered by obtaining or giving them things that they don't have. You can help supply their needs and offer people feedback and input. Something that I could do at Del Norte HS would be teaching people how to use their current digital world access and expand upon it giving them more knowledge and helping empower in the digital space.
### 3. Yes there are many red tapes and papers blocking off in digital empowerment. Some barriers that exist in Del Norte HS include blocked websites that you can't access without a vpn. Their are papers blocking off digital empowerment everywhere we look, whether it be financial issues, supply and demand, or even when you have access to the digital world there are still some features that are being blocked off, for example what I said earlier with DNHS blocking off certain sites.

# Data Structures
### [Replit Link](https://replit.com/@IsaacLe2/Tri3Repo#main.py)


``` 
# Main list of [Prompts, Actions]
# Two styles are supported to execute abstracted logic
# 1. file names will be run by exec(open("filename.py").read())
# 2. function references will be executed directly file.function()
main_menu = [
    ["Swap", "swap.py"],
    ["Tree", "tree.py"]
]

# Submenu list of [Prompt, Action]
# Works similarly to main_menu
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
            # stop
            return
        try:
            # try as function
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:  # try as playground style
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")
            # end function try
        # end prompts try
    except ValueError:
        # not a number error
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        # traps all other errors
        print(f"Invalid choice: {choice}")
    # end validation try

    buildMenu(banner, options)  # recursion, start menu over again


if __name__ == "__main__":
    menu()
    #menuc() 
    ```
