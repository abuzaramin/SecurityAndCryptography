import hashlib
import base64

iterations = 45454
salt = base64.b64decode("6VuJKkHVTdDelbNMPBxzw7INW2NkYlR/LoW4OL7kVAI=".encode())
validation =  "SALTED-SHA512-PBKDF2"

password = "password".encode()
value = hashlib.pbkdf2_hmac("sha512",password, salt, iterations , dklen=128)
entropy = (base64.b64encode(value))
print("Alice", validation, salt, iterations, entropy)

# Same password differnet salt, will result in different encrypted message
salt = "6666".encode()
password = "password".encode()
value = hashlib.pbkdf2_hmac("sha512",password, salt, iterations , dklen=128)
entropy = (base64.b64encode(value))
print("Bob", validation, salt, iterations, entropy)
