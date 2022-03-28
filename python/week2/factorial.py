class Factorial:
    def __init__(num):
        pass
    def __call__(num, n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * num(n - 1)

def factorial_run():
    num = int(input("Please enter a number: "))
    try:
        factorial_of = Factorial()
        print("Factorial number is", factorial_of(num))
    except:
        print("Sorry, didn't work")

if __name__ == "__main__":
    factorial_run()