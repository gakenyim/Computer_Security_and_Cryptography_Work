### Modular Arithmetic 1
### Arithmetic that focuses on remainders
### the modulus is the number we divide by to get the remainder
### example: 7 mod 3 = 1 because 7 divided by 3 leaves a remainder of 1

##Understanding the congruence symbol
### The congruence symbol is ≡
### a ≡ b (mod n) means that a and b leave the same remainder when divided by n
### example: 7 ≡ 1 (mod 3) because both 7 and 1 leave a remainder of 1 when divided by 3

##Basic properties of modular arithmetic
### 1. If a ≡ b (mod n), then a + c ≡ b + c (mod n)
### 2. If a ≡ b (mod n), then a - c ≡ b - c (mod n)
### 3. If a ≡ b (mod n), then a * c ≡ b * c (mod n)

##solve 
a = 11 % 6
print("11 mod 6 =", a)
b = 8146798528947 % 17
print("8146798528947 mod 17 =", b)

# Find the smaller of the two remainders
flag = min(a, b)
print("Flag:", flag)