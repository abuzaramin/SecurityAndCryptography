import random

class KeyStream:
    def __init__(self, key=1):
        self.next = key

    def rand(self):
        self.next = (1103515245 * self.next + 12345) % 2**31
        return self.next

    def get_key_byte(self):
        return ((self.rand()//2**23) % 256)

def encrypt(key, message):
    return bytes([message[i] ^ key.get_key_byte() for i in range(len(message))])


def transmit(cipher, likely):
    b = []
    for c in cipher:
        if random.randrange(0, likely) == 0:
            c = c ^ 2**random.randrange(0, 8)
        b.append(c)
    return bytes(b)

def modification(cipher):
    mod = [0] * len(cipher)
    mod[10] = ord(' ') ^ ord('1')
    mod[11] = ord(' ') ^ ord('0')
    mod[12] = ord('1') ^ ord('0')
    return bytes([mod[i] ^ cipher[i] for i in range(len(cipher))])

def get_key(message, cipher):
    return bytes([message[i] ^ cipher[i]  for i in range(len(cipher))])

def crack(key_stream, cipher):
    lenght = min(len(key_stream), len(cipher))
    return bytes ([key_stream[i] ^ cipher[i] for i in range(lenght)])

def brute_force(plain, cipher):
    for k in range(2**31):
        bf_key = KeyStream(k)
        for i in range(len(plain)):
            xor_value = plain[i] ^ cipher[i]
            if xor_value != bf_key.get_key_byte():
                break
            else:
                return k
    return False

# key = KeyStream(10)
# message = "Send Bob:   10$".encode()
# print(message)
# cipher = encrypt(key, message)
# print(cipher)
#
# #this is Bob
# cipher = modification(cipher)
#
# # This is bank
# #cipher = transmit(cipher, 5)
# key = KeyStream(10)
# message = encrypt(key, cipher)
# print(message)
#
# #understanding of Re-use key problem with Stream cipher
# # Eve Goes to Alice and tells her message
# print ("Eves message")
# eves_message = "this is Eve's most valued secrets of all her life.".encode()
# print (eves_message)
#
# # this is alice alone
# key = KeyStream(10)
# message = eves_message
# print(message)
# cipher = encrypt(key, message)
# print(cipher)
#
# # this is EVE in middle all alone evil
# eves_key_stream = get_key(eves_message, cipher)
#
#
# #This is BOB
# key = KeyStream(10)
# message = encrypt(key, cipher)
# print(message)
#
# #Alice again, Eves already knows teh key
# header = "MESSAGE: "
# message = header +  "My Secret message to BOB"
# message = message.encode()
# key = KeyStream(10)
# cipher = encrypt(key, message)
# print(cipher)
#
# #Bob Again
#
# key= KeyStream(10)
# message = encrypt(key, cipher)
# print (message)
#
#
# #Eve again, as he sits in middle and knows the key
# print ("THIS is EVE")
# key = KeyStream(10)
# message = crack(eves_key_stream, cipher)
# print( message)

#Low key Scenario



#Alice again, Eves already knows teh key
secret_key = random.randrange(0, 2**20)
print ("Secret key of low key screaio is : ", secret_key)
key = KeyStream(secret_key)
header = "MESSAGE: "
message = header +  "My Secret message to BOB"
message = message.encode()
print(message)
cipher = encrypt(key, message)
print(cipher)

#Bob Again

key= KeyStream(secret_key)
message = encrypt(key, cipher)
print (message)


#Eve doing brute force on
print ("THIS is EVE brute forcing attack")
bf_key = brute_force (header.encode(), cipher)
print ("Eve's Brute force key: ", bf_key)
key = KeyStream(bf_key)
message = encrypt(key, cipher)
print(message)