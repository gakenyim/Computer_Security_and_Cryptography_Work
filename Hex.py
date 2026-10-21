##we have been given a hexadecimal string
##63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d
## Convert it back to bytes which will reveal the flag
## Text -> ASCII numbers -> Hexadecimal -> Hex string
## Separate the numbers into pairs and the pairs represent a byte
## bytes.fromhex() can be used to convert the hex string back to bytes
## example 
data = bytes.fromhex("63")
print(data) # it outputs b'c' where b indicates it is a byte string and 'c' is the character represented by the hex value 63

## Now let's convert the full hex string to reveal the flag
hex_string = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"
flag = bytes.fromhex(hex_string)
print(flag)

## .hex() can be used to convert bytes back to a hex string..it does the opposite of bytes.fromhex()
eg1=bytes.fromhex("637279")
print(eg1)
eg1.hex() # it outputs '637279' which is the hex representation of the byte string b'cry'
print(eg1.hex()) # it outputs '637279' which is the hex representation of the byte string b'cry'
