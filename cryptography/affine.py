"""
The affine cipher is defined by the encryption function
    E_k(m) = am + b     a, b, m in Z_26
where the key is k = (a, b). However, not all pairs (a, b) are possible keys.

The affine cipher outputs the following ciphertext for some plaintext and key:
    fmxvedkaphferbndkrxrsrefmorudsdkdvshvufedkaprkdlyevlrhhrh
Determine the plaintext and key.
"""

from __future__ import division
from operator import mul, sub

BASE = 26

def gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = gcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = gcd(a, m)
    if g != 1:
        return -1
    else:
        return x % m

inverses = {}
for n in range(1, BASE + 1):
    inverse = modinv(n, BASE)
    if inverse != -1:
        inverses[n] = inverse

for n in inverses:
    assert (n * inverses[n]) % BASE == 1

def inverse(a):
    return inverses[a]

def E(m, k):
    (a, b) = k
    m = ord(m) - ord("a")
    c = (((a * m) % BASE) + b) % BASE
    return chr(c + ord("a"))

def D(c, k):
    (a, b) = k
    c = ord(c) - ord("a")
    m = (((c - b) % BASE) * inverse(a)) % BASE
    return chr(m + ord("a"))

def encrypt(message, k):
    ciphertext = ""
    for m in message:
        ciphertext += E(m, k)
    return ciphertext

def decrypt(ciphertext, k):
    message = ""
    for c in ciphertext:
        message += D(c, k)
    return message

if __name__ == "__main__":
    ciphertext = "fmxvedkaphferbndkrxrsrefmorudsdkdvshvufedkaprkdlyevlrhhrh"

    possible_as = [a for a in range(1, BASE + 1) if gcd(a, BASE)[0] == 1]
    possible_bs = [b for b in range(1, BASE + 1)]

    # Exhausive key search
    # Decrypts the ciphertext for all possible keys so that a human can find the right one
    for a in possible_as:
        for b in possible_bs:
            k = (a, b)
            print(str(a) + "\t" + str(b) + "\t" + decrypt(ciphertext, k))

    # The key and plaintext are:
    key = (3, 5)
    plaintext = "algorithmsarequitegeneraldefinitionsofarithmeticprocesses"

    print(decrypt(ciphertext, (3, 5)))

    assert encrypt(plaintext, key) == ciphertext
    assert decrypt(ciphertext, key) == plaintext
    assert decrypt(encrypt(plaintext, key), key)
