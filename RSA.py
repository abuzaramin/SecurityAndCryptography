import math
import random


def is_prime(p):
    for i in range(2, math.isqrt(p)):
        if p % i  == 0:
            return False
    return True

def get_prime(size):
    while True:
        p = random.randrange(size, 2 * size)
        if (is_prime(p)):
            return p


def lcm (a, b):
    return a*b//math.gcd(a,b)

def get_e (lambda_n):
    for e in range(2, lambda_n):
        if math.gcd(e, lambda_n) == 1:
            return e
    return False

def get_d(e,lambda_n):
    for d in range (2, lambda_n):
        if d*e % lambda_n == 1:
            return d
    return False

def factor(n):
    for p in range(2, n):
        if n%p == 0:
            return p, n//p


#Key gneration done by Alic(secret)
#Step 1 : Generate two Distinct primes

size = 300
p = get_prime(size)
q = get_prime(size)
print("Generated Primes p and q ", p, q)

#Step 2 : Compute n = p*q
n = p*q
print ("Modulus n: ", n)

# Step 3: Compute lambda (n) lcm(a, b) = |ab|/gcd(a, b).
lambda_n = lcm (p-1, q-1)
print ("Lambda N ", lambda_n)

#Step 4 : Choose an integer e such that 1 < e < λ(n) and gcd(e, λ(n)) = 1
e = get_e (lambda_n)
print ("public exponent", e)

#Step 5: solve for d the equation d⋅e ≡ 1 (mod λ(n));
d = get_d(e,lambda_n)
print ("Secret Exponent:", d)

#Done with Key generation:
print ("Public key (e,n):", e, n)
print ("Secret Key (d)", d)

# This is bob wants to send message
m = 117
c = m**e % n
print("Bob sends m = ", m , " ciper is ", c)

#This is Alice decrypting the cipher

m = c**d % n
print("Alice gets ", m)


#this is Eve

print("Eve sees the following")
print ("public key (e,n)" , e,n)
print ("Encrypted Cipher", c)
p, q = factor(n)
print ("factors", p, q)


lambda_n = lcm (p-1, q-1)
print ("Eve: Lambda N ", lambda_n)

d = get_d(e,lambda_n)
print ("Eve : Secret Exponent:", d)

m = c**d%n
print("Eve Message: ", m)


#This is Bob not being careful
print("This is Bob not being careful")
message = "Alice is awesome"

for m_c in message:
    c = ord(m_c) **e % n
    print (c, " ", end = "")

print()