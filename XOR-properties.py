## XOR properties
## Commutative: A ⊕ B = B ⊕ A
## Associative: A ⊕ (B ⊕ C) = (A ⊕ B) ⊕ C
## Identity: A ⊕ 0 = A
## Self-inverse: A ⊕ A = 0

from binascii import hexlify, unhexlify
KEY1 = unhexlify("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")

KEY2_XOR_KEY1 = unhexlify("37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e")

KEY2_XOR_KEY3 = unhexlify("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")

ENCRYPTED_FLAG = unhexlify("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf")

##Find KEY2
KEY2 = bytes(a ^ b for a,b in zip(KEY2_XOR_KEY1, KEY1))

##Find KEY3
KEY3 = bytes(a ^ b for a,b in zip(KEY2_XOR_KEY3, KEY2))

##Find the flag
FLAG = bytes(
    a ^b ^ c ^ d
    for a, b, c, d in zip(ENCRYPTED_FLAG, KEY1, KEY2, KEY3)
)

print(FLAG.decode())