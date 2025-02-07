# 10demo.py by Elizabeth K.

print('hello, again')   # greeting
print("""hello,
again""")

#function practice
print(1.5e-2)

print(abs(-6))
print(pow(2,3))
print(round(2.95423, ndigits=3))

import math
print(math.ceil(2.438))
print(math.factorial(4))
print(math.inf)
print(math.nan)

print(0.1 * 1)
print(0.1 * 3)

#computes hypotenuse
a = 3                       #integer
b = 4                       #integer
c = math.sqrt(a**2 + b**2)  #float
print(c)
print(type(a), type(b), type(c),  sep=', ', end='!\n')

#functions
def pythagoras(a, b):
    c = math.sqrt(a**2 + b**2)
    return c
hyp = pythagoras(3, 4)
print(hyp)

#simplified function
def pythagoras(a,b):
    return math.sqrt(a**2 + b**2)
print(pythagoras(3, 4))

#strings
s = 'hello world'
print(s, type(s))

#conditionals
##if
a = 2
b = 3
if a == b:
    print('a equals b')
    print(a, b)

def is_even(x):
    if x % 2 == 0: return True
    return False
print(is_even(2))
print(is_even(3))

##boolean
c = a == b
print(c)
print(type(c))

##if-elif-else
if a < b:
    print('a < b')
elif a > b:
    print('a > b')
else:
    print('a == b')

##chaining
if a < b or a > b:  print('all things are equal, a and b are not')
if a < b and a > b: print('you are living in a strange world')
if not False: print(True)

##floating point warning
print(abs(a - b))
if abs(a - b) > 1e-9:
    print('close enough')

if math.isclose(a, b):
    print('close enough')

##string comparison
s1 = 'A'
s2 = 'B'
s3 = 'a'
if s1 < s2: print('A < B')
if s2 < s3: print('B < a')

#none type
def silly(m, x, b):
    y = m * x + b
print(silly(2, 3, 4))

