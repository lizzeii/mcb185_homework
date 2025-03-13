import random

##loop all variables to get each possibility
for a in range(1, 100):
    for b in range(1, 100):
        for c in range(1, 100):
            ##can change the end range? no specifications
            c1 = c ** 2
            c2 = a ** 2 + b ** 2
            if c1 == c2 and a < b:
                ##a < b prevents repeats
                print(a, b, c)
    
## want valid triples
## not necessarily a random number generator
## divide all a, b, and c to get their least common multiple?

#while True:
#    a = random.randint(1, 100)
#    b = random.randint(1, 100)
#    c = random.randint(1, 100)
#    c1 = c ** 2
#    c2 = a ** 2 + b ** 2
#    if c1 == c2 and a < b:
#        print(a, b, c)
