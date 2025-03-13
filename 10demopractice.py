import math
import random

def circle_area(r):
    return math.pi *r**2
print(circle_area(3))

def rectangle_area(w, h):
    return w * h
print(rectangle_area(2, 3))

def triangle_area(w, h):
    return rectangle_area(w, h) / 2
print(triangle_area(2, 3))

#celcius to farenheit
def tempf(c):
    return (c * (9 / 5)) + 32
print(tempf(25))

#farenheit to celcius
def tempc(f):
    return (f - 32) * (5 / 9)
print(tempc(77))

#mph to kph
def mph(k):
    return k / 1.609
print(mph(100))

#kph to mph
def kph(m):
    return m * 1.609
print(kph(65))

#DNA concentration?


#arithmetic mean of 3 numbers
def meana(a, b, c):
    return (a + b + c) / 3
print(meana(1, 2, 3))

#geometric mean of 3 numbers
def meang(a, b, c):
    return math.sqrt(a * b * c)
print(meang(1, 2, 3))

#harmonic mean of 3 numbers
def meanh(a, b, c):
    return 3 / ((1 / a) + (1 / b) + (1 / c))
print(meanh(1, 2, 3))

#distance between 2 points in a graph
def dist(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(dist(1, 2, 3, 4))

#if number is an integer
print(type(3.2))
def isinteger(x):
    if x % 1 == 0:    return True
    return False
print(isinteger(3.2))
#with random numbers
#either random.random() or random.randint(,)
def isintegerrand(x):
    if type(x) == type(3.2):    return False
    return True
print(random.randint(1, 10))
print(isinteger(random.randint(1, 10)))
##what are ways to identify nonintegers?

#if number is a valid probability
def prob(x):
    if x <=100: return 'valid probability'
    return 'not a valid probability'
print(prob(99.9))

#molecular weight of a DNA letter
def molbp(n):
    A = 267
    G = 151
    T = 126
    C = 111
    if n == A:      return 'this is adenine'
    elif n == G:    return 'this is guanine'
    elif n == T:    return 'this is thymine'
    elif n == C:    return 'this is cytosine'
    else:           return None
print(molbp(100))

#complementary DNA base pairs
def compbp(n):
    a = 'A'
    g = 'G'
    t = 'T'
    c = 'C'
    if n == a:      return 'G'
    elif n == g:    return 'C'
    elif n == t:    return 'A'
    elif n == c:    return 'G'
    else:           return None
print(compbp('C'))

#maximum of three numbers
def max(x, y, z):
    if x > y and x > z:     return 'x is largest'
    elif y > x and y > z:   return 'y is largest'
    elif z > x and z > y:   return 'z is largest'
    return None
print(max(5, 5, 3))

#f1 score
def f1score(tp,fp,fn):
    p = tp / (tp + fp)  #precision
    r = tp / (tp + fn)  #recall/sensitivity
    return 2 / ((1 / p) + (1 / r))
print(f1score(1, 4, 4))

#shannon entropy of nucleotides
def shaen(a, c, g, t):
    e = (-(0.25) * math.log(0.25))
    return (a * e) + (c * e) + (g * e) + (t * e)
print(shaen(5, 3, 4, 5))