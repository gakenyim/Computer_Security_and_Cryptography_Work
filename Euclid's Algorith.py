### Euclid’s Algorithm finds the GCD by repeatedly dividing and keeping the remainder.
### The rule is: gcd(a,b)=gcd(b,a mod b)
### You repeat this until the remainder becomes 0. The last non-zero number is the GCD.

##Example values
# a= 12
# b= 8
# while b !=0:
#     a, b= b, a % b

# print(a)

## actual implementation
a = 66528
b = 52920
while b != 0:
    a, b = b, a % b

print(a) #display the greatest common divisor of a and b