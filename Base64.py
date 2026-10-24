## All about Base64
#Base64 is an encoding method that converts binary data into readable text
##ASCII converts numbers into characters and hexadecimal represents bytes using the symbols 1-9, A-F
##Base64 represents bytes using a set of 64 printable ASCII characters
# that is a-z (26), A-Z (26), 0-9 (10), +, /(2)
# The '=' character is used for padding to make the output length a multiple of 4
import base64
## First convert the hex string to bytes
data = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
result= bytes.fromhex(data)

print(result)

## Now encode the bytes to Base64; 1 byte = 8 bits, 6 bits per Base64 character
encoded = base64.b64encode(result)
print(encoded)

## Convert the Base64 into a readable string
decoded = base64.b64decode(encoded)
print(decoded)