import math

##function that returns the minimum value of a list
vals = [1, 2, 3, 4]
print(vals)

def minimum(vals):
    mini = vals[0]
    ##minimum for 1 item is that item
    for val in vals[1:]:
        if val < mini:
            mini = val
            ##replaces the minimum with each iteration if there is a smaller number
    return mini
print(minimum(vals))

##function that returns both the minimum and maximum values of a list
def minmax(vals):
    mini = vals[0]
    maxi = vals[0]
    for val in vals:
        if val < mini:
            mini = val
        if val > maxi:
            maxi = val
    return mini, maxi
print(minmax(vals))

##function that returns the mean of the values in a list
def mean(vals):
    total = 0
    for val in vals:
        total += val
        ##adds each item onto the total
    return total / len(vals)
    ##mean formula
print(mean(vals))

##function that computes the entropy of a probability distribution
def entropy(probs):
    h = 0
    for p in probs:
        h -= p * math.log2(p)
        ##entropy formula
    return h
print(entropy([0.2, 0.3, 0.5]))
    ##manually inputting list

##function that computes the Kullback-Leiber distance between two sets of probability distributions
def dkl(P, Q):
    ##P and Q represent probability distributions
    d = 0
    for p, q in zip(P, Q):
        ##p and q represent individual values
        ##zip() retrieves probabilities from P and Q
        d += p * math.log2(p / q)
    return d
p1 = [0.4, 0.3, 0.2, 0.1]
##list
p2 = (0.1, 0.3, 0.4, 0.2)
##tuple
print(dkl(p1, p2))