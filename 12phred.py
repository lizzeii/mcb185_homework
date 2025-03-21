import math

#letter to probability error
##letter > ASCII > Q score > phred
###ord converts letter to ASCII
###q score = ASCII - 33

def perror(l):
    print(type(l))
    if type(l) == type('A'):
        return math.pow(10, (-(ord(l) - 33) / 10))
    elif type(l) != type('A'):
        return None
    return None
print(perror('A'))

#probability error to letter
##phred > Q score > ASCII > letter
b = 65
q = chr(b)
##chr converts ASCII to a letter
print(q)
###chr needs valid <int> not <float>

def lett(p):
    print(type(p))
    if type(p) == type(1.0):
        return chr(math.ceil(-10 * math.log10(p) + 33))
    elif type(p) != type(1.0):
        return None
    return None
print(lett(1.0))

#how to make it so that I don't have to put in variables without error?

#assessment
def chrtoerror(a):
    return 2 ** (64 - ord(a))
print(chrtoerror('F'))

def errortochr(n):
    return chr(math.ceil(-math.log2(n)) + 64)
print(errortochr(0.4))