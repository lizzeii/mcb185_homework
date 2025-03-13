#tuples
t = 1, 2
print(t)
print(type(t))

person = 'Steve', 21, 57891.50  #name, age, yearly income
print(person)

def midpoint(x1, y1, x2, y2):
    x = (x1 + x2) / 2
    y = (y1 + y2) / 2
    return x, y
print(midpoint(1, 2, 3, 4))
m = midpoint(1, 2, 3, 4)
mx, my = midpoint(1, 2, 3, 4)
print(mx, my)
print(m[0], m[0])

#iteration
##while
i = 0
while True:
    i = i + 1
    print('hey', i)
    if i == 3: break

i = 0
while i < 3:
    i = i + 1
    print('hey', i)

i = 1
while i < 10:
    print(i)
    i = i + 3
print('final value of i is', i)

##for i in range()
for i in range(1, 10, 3):   #initial value, end-before limit, increment
    print(i)

for i in range(0, 5):   #increment is not necessary
    print(i)

for i in range(5):  #initial value is not necessary
    print(i)

for i in range(4, -1, -1):
    print(i)

##for item in container
basket = 'milk', 'eggs', 'bread'
for thing in basket:
    print(thing)

for i in range(len(basket)):
    print(basket[i])

#nesting
for i in range(7):
    if i % 2 == 0:
        print(i, 'is even')
    else:
        print(i, 'is odd')

#random numbers
import random

for i in range(5):
    print(random.random())
    ##random.random generates a number 0 <= x < 1
    ##loop runs 5 times

for i in range(3):
    print(random.randint(1, 6))
    ##random.randint generates an integer between two inclusive end points

random.seed(1)
print(random.random())
print(random.random())
random.seed(2)
print(random.random())
random.seed(1)
print(random.random())
random.seed(2)
print(random.random())
##all random numbers can be called as long as you set the seed ahead of times

#compound assignment
## += specifies for increments
### i += 1 replaces i = i + 1
## -= specifies for decrement
## *= specifies for multiply and assign