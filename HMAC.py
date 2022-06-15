import hashlib
import base64

def modify(m):
    l = list(m)
    l[0] =  l [0] ^ 1
    return bytes(l)

# Alice and Bob share a secret key
secret_key = "secret key".encode()


# Alice wants to compute a MAC
m = "Hey Bob. You are still awesome.".encode()
sha256 = hashlib.sha256()
sha256.update(secret_key)
sha256.update(m)
hmac = sha256.digest()
base64 = base64.b64encode(hmac)
print(m, hmac, base64)

#Eve comes along, observe the hmac of bob will be different
m = modify(m)
print(m)

# Bob receives and validates the HMAC
sha256 = hashlib.sha256()
sha256.update(secret_key)
sha256.update(m)
hmac = sha256.digest()
#base64b = base64.b64encode(hmac)
print(m, hmac)


