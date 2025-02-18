import math

#distance between two points in a graph
def dist(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(dist(2, 3, 4, 5))

#complement DNA letter
def compdna(nt):
    if nt == 'A':
        return 'T is the compliment base pair'
    elif nt == 'G':
        return 'C is the compliment base pair'
    elif nt == 'T':
        return 'A is the compliment base pair'
    elif nt == 'C':
        return 'G is the compliment base pair'
    return None
print(compdna('%'))

#maximum of 3 numbers
def max3(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    elif c > a and c > b:
        return c
    return None
print(max3(4, 5, 1))

#question 4
##i'm not sure why PHRED quality values are -10*log10 instead of -log2
##i would change the equation to -log2 if i thought it was better?