import math

#calculates sum from 1 to n
def triangular(n):
    tri = 0
    ##holds the sum at 0
    for i in range(n + 1):
        tri = tri + i
        ##each iteration of the loop adds the current value of the loop variable
    return tri
print(triangular(4))

#calculates factorial of a number
def factorial(n):
    if n == 0:
        return 1
    ##not sure if needed, already returns 1
    fac = 1
    for i in range(1, n + 1):
        ##will always get 0 if you initialize at 0, must initialize at 1
        fac = fac * i
    return fac
print(factorial(5))

#probability of k events occuring
def poisson(n, k):
    kf = 1
    for i in range(1, k + 1):
        kf = kf * i
    return (n**k * math.e**(-n)) / kf
print(poisson(3, 4))

##OR##
def poissone(n, k):
    return n**k * math.e**-n / factorial(k)
        ##uses the factorial function
print(poissone(3, 4))

#solving n choose k
def nchoosek(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))
    ##functions can be reused in other functions
    ##not sure how (n - k) works?
print(nchoosek(3, 4))

#estimating Euler's number
def euler(n):
    e = 0
    for i in range(n):
        e = (e + 1) / factorial(n)
        ##infinite sum of 1 over n!
        ##e + 1 likely adds the previous calculation to the current loop
    return e
print(euler(10))

#determine if a number is prime
def is_prime(n):
    for i in range(2, n//2 + 1):
        ##loop ends because number cannot be divided by more than half of itself
        if n % i == 0:
            ##divides the number by i (0, 1, 2, ...) each loop
            return n, False
    return n, True
    ##1 is not needed in the loop because it is prime
print(is_prime(1))

#estimating pi with nilakantha series
##pi = 3 + 4/(2 * 3 * 4) - 4/(4 * 5 * 6) + 4/(6 * 7 * 8) - ...
def nilakantha(n):
    pi = 3
    ##equation starts with 3
    for i in range(1, n + 1):
        n = 2 * i
        ##n can only start in even numbers?
        d = n * (n + 1) * (n + 2)
        ##allows multiplying in groups of 3 (2 * 3 * 4)
        if i % 2 == 0:
            pi = pi - 4 / d
        else:
            pi = pi + 4 / d
        ##alternates between + and - with each loop
    return pi
print(nilakantha(6))

import random

#monty pi-thon
#while True:
#    in_cir = 0
#    out_cir = 0
#    for i in range(100):
#        x = random.random()
#        y = random.random()
#        d = x ** 2 + y ** 2
#        if d < 1:
#            in_cir += 1
#            out_cir += 1
#            #why is out_cir also incremented?
#        else:
#            out_cir += 1
#    pi = 4 * (in_cir / out_cir)
#    print(pi)

#d&d stats
##roll 3 six-sided dice
dice = 3
for i in range(dice):
    print(random.randint(1, 6))

##roll 3 six-sided dice, reroll any 1s
dice = 3
for i in range(dice):
    roll = random.randint(1, 6)
    if roll == 1:
        print(roll)
    else:
        print(roll)

##roll pairs of six-sided dice 3 times, taking the maximum each time
dice = 3
for i in range(dice):
    roll1 = random.randint(1, 6)
    roll2 = random.randint(1, 6)
    if roll1 > roll2:
        print(roll1)
    else:
        print(roll2)

##roll 4 six-sided dice, dropping the lowest roll
dice = 4
for i in range(dice):
    roll = random.randint(1, 6)
    print(roll)
##not sure how to remove without having long lines of code

print(6 % 5)