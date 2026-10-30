## XOR encryption and decryption starter code
## XOR is a bitwise operator which returns 0 if the bits are the same, and 1 otherwise
##Example: 0 XOR 0 = 0, 0 XOR 1 = 1, 1 XOR 0 = 1, 1 XOR 1 = 0
## Exercise: Given the string label, XOR each character with the integer 13. Convert these integers back to a string and submit the flag as crypto{new_string}
##Process: ""label"->characters->ASCII values->XOR with 13->new ASCII values->new characters->new string

# #ord converts a character to its ASCII value
# print(ord('l')) ## so the ASCII value of 'l' is 108

#for the whole word
for char in "label":
    print(ord(char))

# XOR each ASCII value with 13 and convert back to character
for char in "label":
    new_char = chr(ord(char) ^ 13)
    print(new_char)
    print("crypto{" + new_char + "}")