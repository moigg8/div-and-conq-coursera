#!/usr/bin/env python3

def karatsuba( number1, number2 ):
    len1 = len(number1)
    len2 = len(number2)
    diff = abs(len1 - len2)
    if diff > 0:
        zeroes = getZeroes(diff)
        if len1 < len2:
            number1 = zeroes + number1
            len1 += 1
        else:
            number2 = zeroes + number2
            len2 += 1
    if len1 == 1 and len2 == 1: 
        return int(number1) * int(number2)
    if len1 % 2 != 0:
        number1 = "0" + number1
        len1 += 1

    if len2 % 2 != 0:
        number2 = "0" + number2
        len2 += 1
    
    n = len1
    
    a, b = number1[:len(number1)//2], number1[len(number1)//2:]
    c, d = number2[:len(number1)//2], number2[len(number1)//2:]

    p = int(a) + int(b)
    q = int(c) + int(d)
    ac = karatsuba(a,c)
    bd = karatsuba(b,d)
    pq = karatsuba(str(p), str(q))
    adbc = pq - ac - bd

    return int(str(ac)+getZeroes(n)) + int(str(adbc)+getZeroes(n/2)) + bd

def getZeroes( n ):
    n = int(n)
    zeroes = ""
    for x in range(n):
        zeroes = zeroes + "0"
    return zeroes

n1 = "12"
n2 = "111"
k = str(karatsuba(n1,n2))
t = str(int(n1)*int(n2))
print ("TEST: " + n1 + " * " + n2 + " = " + t +", KARATSUBA: " + k + ", " + str(k == t))
n1 = "123"
n2 = "993"
k = str(karatsuba(n1,n2))
t = str(int(n1)*int(n2))
print ("TEST: " + n1 + " * " + n2 + " = " + t +", KARATSUBA: " + k + ", " + str(k == t))
n1 = "12"
n2 = "12"
k = str(karatsuba(n1,n2))
t = str(int(n1)*int(n2))
print ("TEST: " + n1 + " * " + n2 + " = " + t +", KARATSUBA: " + k + ", " + str(k == t))
n1 = "99998789465465416465165"
n2 = "85754354354365436541551"
k = str(karatsuba(n1,n2))
t = str(int(n1)*int(n2))
print ("TEST: " + n1 + " * " + n2 + " = " + t +", KARATSUBA: " + k + ", " + str(k == t))

n1 = "3141592653589793238462643383279502884197169399375105820974944592"
n2 = "2718281828459045235360287471352662497757247093699959574966967627"
k = str(karatsuba(n1,n2))
t = str(int(n1)*int(n2))
print ("TEST: " + n1 + " * " + n2 + " = " + t +", KARATSUBA: " + k + ", " + str(k == t))
