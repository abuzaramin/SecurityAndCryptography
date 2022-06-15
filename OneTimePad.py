import random

def generate_key_stream (n):
    return bytes([random.randrange(0,256) for i in range(n)])

def xor_bytes(key_stream, message):
    lenght = min(len (key_stream), len(message))
    return bytes([key_stream[i] ^ message[i] for i in range(lenght)])

message = "DO ATTACK"
message = message.encode()
key_stream = generate_key_stream(len(message))
cipher = xor_bytes(key_stream, message)

# this is us trying to break it

print (cipher)
message = "NO ATTACK"
message = message.encode()
guess_key_stream = xor_bytes(message, cipher)
print ( xor_bytes(key_stream, cipher))
print (xor_bytes(guess_key_stream, cipher))