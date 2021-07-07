# -*- coding: utf-8 -*-
"""
Created on Sun May  9 20:13:14 2021
@author: Rahul 18BCE0018
"""

import time
from random import randrange
from hashlib import md5
from gmpy2 import xmpz, invert, powmod, is_prime

def generate_g(p, q):
    while True:
        h = randrange(2, p - 1)
        exp = xmpz((p - 1) // q)
        g = powmod(h, exp, p)
        if g > 1:
            break
    return g


def generate_keys(g, p, q):
    x = randrange(2, q)  # x < q
    y = powmod(g, x, p)
    return x, y


def sign(M, p, q, g, x):
    if not validate_params(p, q, g):
        raise Exception("Invalid Parameters")
    while True:
        k = randrange(2, q)  # k < q
        r = powmod(g, k, p) % q
        m = int(md5(M).hexdigest(), 16)
        try:
            s = (invert(k, q) * (m + x * r)) % q
            return r, s
        except ZeroDivisionError:
            pass


def verify(M, r, s, p, q, g, y):
    if not validate_params(p, q, g):
        raise Exception("Invalid Parameters")
    if not validate_sign(r, s, q):
        return False
    try:
        w = invert(s, q)
    except ZeroDivisionError:
        return False
    
    print('\nMessage Recieved: ',M)
    m = int(md5(M).hexdigest(), 16)
    print("H'(M): ",m)
    u1 = (m * w) % q
    u2 = (r * w) % q
    v = (powmod(g, u1, p) * powmod(y, u2, p)) % p % q
    print("w:  ",w)
    print("u1: ",u1)
    print("u2: ",u2)
    print("v:  ",v)
    if v == r:
        return True
    return False


def validate_params(p, q, g):
    if is_prime(p) and is_prime(q):
        return True
    if powmod(g, q, p) == 1 and g > 1 and (p - 1) % q:
        return True
    return False


def validate_sign(r, s, q):
    if r < 0 and r > q:
        return False
    if s < 0 and s > q:
        return False
    return True


if __name__ == "__main__":
    p=23
    q=11
    g=generate_g(p,q)
    f = open("rahul_doc.txt", "r")
    x, y = generate_keys(g, p, q)
    text=f.read()
    M = str.encode(text, "ascii")
    r, s = sign(M, p, q, g, x)
    
    print("\nSENDER'S SIDE\n")
    print("P: ",p)
    print("Q: ",q)
    print("g: ",g)
    print("x: ",x)
    print("y: ",y)
    print("r: ",r)
    print("s: ",s)
    print("Digital Signature:({r},{s})".format(r=r,s=s))
    print("Message Sent: ",M)
    print('Hash, H(M): ',int(md5(M).hexdigest(), 16))
    
    #I am doing this to give myself time to modify the document before verifying
    time.sleep(7)   
    
    print("\n\nRECEIVER'S SIDE")
    f.seek(0,0)
    text=f.read()
    new_M=str.encode(text, "ascii")
    if verify(new_M, r, s, p, q, g, y):
        print('Signature Matched, Authenticity Verified!')
    else:
        print('Digital Signature does not Match! , File modified')