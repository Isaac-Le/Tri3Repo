InfoDb = []
# List with dictionary records placed in a list  
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
  
def for_loop():
    for n in range(len(InfoDb)):
        print_data(n)
# while loop contains an initial n and an index incrementing statement (n += 1)
def while_loop(n):
    while n < len(InfoDb):
        print_data(n)
        n += 1
    return
def recursive_loop(n):
    if n < len(InfoDb):
        print_data(n)
        recursive_loop(n + 1)
    return

def main():
  print("For loop: ")
  for_loop()
  print("While loop: ")
  while_loop(0)
  print("Recursive loop: ")
  recursive_loop(0)
