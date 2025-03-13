import random

rolls = 100
dc = 5
success = 0

#normal probability
for i in range(rolls):
    d20 = random.randint(1, 20)
    if d20 > dc:
#        print(d20, 'Success')
        success += 1
#    else:
#        print(d20, 'Fail')
print('Normal Probability: ', success / rolls)

## roll a d20 (20 sided die)
## is the roll higher than the dc (5, 10, 15)?
## calculate the probability = adding up successes

#advantage
## take highest of two rolls
rolls = 100
dc = 5
success = 0

for i in range(rolls):
    d201 = random.randint(1, 20)
    d202 = random.randint(1, 20)
    if d201 > dc and d201 > d202:
#        print(d201, 'Success')
        success += 1
    elif d202 > dc and d202 > d201:
#        print(d202, 'Success')
        success += 1
#    else:
#        print('Fail')
print('Advantage Probability: ', success / rolls)

#disadvantage
## take lowest of two rolls
rolls = 100
dc = 5
success = 0

for i in range(rolls):
    d201 = random.randint(1, 20)
    d202 = random.randint(1, 20)
    if d201 > dc and d201 < d202:
#        print(d201, 'Success')
        success += 1
    elif d202 > dc and d202 < d201:
#        print(d202, 'Success')
        success += 1
#    else:
#        print('Fail')
print('Disadvantage Probability: ', success / rolls)
        