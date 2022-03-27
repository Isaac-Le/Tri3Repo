def gcd(num1, num2):
    if num1 == 0:
        return num1
    while num2 != 0:
        if num1 > num2:
            num1 = num1 - num2
        else:
            num2 = num2 - num1
    return num1
  
def gcd_run():
  print("The GCD of 69, 13", gcd(69, 13))
  print("The GCD of 208, 36", gcd(208, 36))
  