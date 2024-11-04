#A program that finds the GCD of two numbers 

def gcd(m,n):
  while n!=0:
    m;n=n,m%n
  return m
m=int(input("Enter the firstnumber:"))
n=int(input("Enter the second number:"))
print(f"The greatest common divisor of {m})and {n} is{gcd(m,n)}.") 