### Extended Euclidean's Algorithm
### Find u and v such that:
### a*u + b*v = gcd(a,b)
###given a= 26513 and b is 32321

a = 26513
b = 32321

p = a
q = b
## Ordinary Euclidean's Algorithm

while b !=0:
    a,b = b, a%b
    
print("gcd:", a)

## Extended Euclidean's Algorithm
a = p
b = q
# Coefficients for the extended Euclidean algorithm
u1, u2 = 1,0
v1, v2 = 0,1

while b != 0:
    #calculate quotient for this step
    quotient = a // b
    # calculate the remainder
    remainder = a % b
    # update a and b with the remainder
    a, b = b, remainder
    # update the coefficients for u and v
    u1, u2 = u2, u1 - quotient * u2
    v1, v2 = v2, v1 - quotient * v2

print("u:", u1)
print("v:", v1)

#verify the result
print("Check: a*u + b*v =", p*u1 + q*v1)
#the question asks for the smaller of u and v

print("Flag:", min(u1, v1))
