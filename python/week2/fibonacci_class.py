
class Fibonacci:
    def __init__(self):
        self.fiboSeq = [0, 1]
    def __call__(self, n):
        if n < len(self.fiboSeq):
            return self.fiboSeq[n]
        else:
            # Compute the requested Fibonacci number
            fib_number = self(n - 1) + self(n - 2)
            self.fiboSeq.append(fib_number)
        return self.fiboSeq[n]


def fibonacci_class():
    # Make a fibonacci object
    while True:
        fibo_of = Fibonacci()
        n = input("Enter the number of terms: ")
        try:
            n = int(n)
            # Validate the value of n
            if n < 2 or n > 99:
                raise ValueError
            # Fibonacci term corresponding to n
            print(f"Term {n} of Fibonacci sequence is: ", fibo_of(n - 1))
            # Produces a list of fibonacci values, one fibonacci result for each step in range
            print(f"Fibonacci sequence of {n} terms is: ", [fibo_of(i) for i in range(n)])
            break
        except ValueError:
            print(f'Positive integer number in range 2 to 99 is expected, got "{n}" Try again.')


if __name__ == "__main__":
    fibonacci_class()