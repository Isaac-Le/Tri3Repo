class GCD:
  def __call__(self, num1, num2):
      if num1 == 0:
          return num1
      while num2 != 0:
          if num1 > num2:
              num1 = num1 - num2
          else:
              num2 = num2 - num1
      return num1


def gcd_run():
    # Tester 1
    num1 = 133 # int(input("Input your first value: "))
    num2 = 66 # int(input("Input your second value: "))
    gcd = GCD()
    result = gcd(num1,num2)
    print("-"*45, "\nThe greatest common denominator of", num1, "and", num2, "is", result)
    # Tester 2
    num1 = 68
    num2 = 126
    result = gcd(num1,num2)
    print("-"*45, "\nThe greatest common denominator of", num1, "and", num2, "is", result) 

if __name__ == "__main__":
    gcd_run()