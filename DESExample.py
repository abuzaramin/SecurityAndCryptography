from pyDes import *

def modify(cipher):
    mod = [0]* len(cipher)
    mod[9] = 1
    return bytes([mod[i] ^ cipher [i] for i in range(len(cipher))])

#message = "0123456701234567"
message = "Give Bob:    10$ and send that to him"
key = "DESCRYPT"
iv = bytes([0]*8)
# k = des(key, ECB, iv, pad=None, padmode=PAD_PKCS5)
k = des(key, ECB, iv, pad=None, padmode=PAD_PKCS5)
cipher = k.encrypt(message)
print("Lenght of plain text:", len(message))
print("Lenght of cipher text:", len(cipher))
print("Encrypted:", cipher[0:8])
print("Encrypted:", cipher[8:16])
print("Encrypted:", cipher[16:])

#Bob modifying the cipher text
cipher = modify(cipher)


#This is the bank decrypting the message
message = k.decrypt(cipher)
print ("Decrypted:", message)
