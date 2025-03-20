import sys
import math

##turns words on the command line into probabilities
probs = []
##container to hold probabilities
for arg in sys.argv[1:]:
    ##[1:] skips over the first argument (31entropy.py)
    f = float(arg)
    ##converts argument into a float
    if f <= 0 or f >= 1:
        sys.exit('error: not a probability')
    probs.append(f)

##check if the probabilities sum up to 1.0
total = 0
for p in probs:
    total += p
if not math.isclose(total, 1.0):
    sys.exit('error: probs must sum to 1.0')

##calculates entropy
h = 0
for p in probs:
    h -= p * math.log2(p)
print(f'{h:.4f}')

##type python 31entropy.py with values in the command line