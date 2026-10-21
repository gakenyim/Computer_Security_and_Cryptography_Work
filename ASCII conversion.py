## ASCII Conversion
## python chr() converts an ASCII code to its corresponding character
## example:
# print(chr(65))  # Output: 'A'

## implementation:
numbers = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]

for number in numbers: #goes through each number in the list
    print(chr(number), end='') #chr() converts the ASCII code to its corresponding character and prints it without a newline using end=''
print() #prints a newline at the end

print (ord ('S')) #prints the ASCII code for the character 'S'