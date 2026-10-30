## Key idea message->bytes->one big integer->RSA encryption
## Decryption: RSA decryption->big integer->bytes->message

##for example: when encrypting
## HELLO-> ASCII/bytes -> hexadecimal -> large integer
##import the necessary libraries
from Crypto.Util.number import bytes_to_long, long_to_bytes

number = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
## long_to_bytes converts a long integer to bytes to character/message
message = long_to_bytes(number)
## print the original message
print(message)

## convert a message back to a long integer
message=b"HELLO"
## bytes_to_long converts a message in bytes to a long integer
number= bytes_to_long(message)
## print the converted number
print(number)