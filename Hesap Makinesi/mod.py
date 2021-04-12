def toplama(a,b):
    c = a + b
    return c
def carp(a,b):
    c = a * b
    return c
def bol(a,b):
    c = a / b
    return c
def cikar(a,b):
    c = a - b
    return c
def p(a,b):
    p = 1
    while b > 0:
        if a < b:
            break
        else:
            p*=a
            a-=1
            b-=1
            if b == 0:
                return p
def faktoriyel(a):
    f = 1
    i = 1
    while i < a:
        f*=a
        a-=1
        if i == a:
            return f
def c(a,b):
        c = (p(a,b)) / (faktoriyel(b))
        return c
def kokbul(a,b):
    c = a ** (1 / b)
    return c
def usbul(a,b):
    c = a ** b
    return c