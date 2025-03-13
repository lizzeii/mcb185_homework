import random

rolls = 1000
success = 0
failure = 0
death = 0
stable = 0
revive = 0

for i in range(rolls):
    d20 = random.randint(1, 20)
    if d20 == 1:
        print(d20, '+2 Failures')
        failure += 2
    elif d20 == 20:
        print(d20, 'You have Revived')
        revive += 1
    elif d20 < 10:
        print(d20, '+ 1 Failure')
        failure += 1
    elif d20 >= 10:
        print(d20, '+1 Success')
        success += 1
    if failure == 3:
        print(failure, 'Failures, You are Dead')
        failure = 0
        success = 0
        death += 1
    if success == 3:
        print(success, 'Successes, You are Stable')
        success = 0
        failure = 0
        stable += 1
outcomes = death + stable + revive
print('Death Probability: ', death / outcomes)
print('Stabilizing Probability: ', stable / outcomes)
print('Revival Probability: ', revive / outcomes)
##is it better to break the loop after each death, stablize, and revival?

## health < 0 = unconsciousness / death
## roll d20
## d20 < 10 = failure
## d20 >= 10 = success
## d20 = 1 = 2 failure
## d20 = 20 = gain 1 health and revive
## 3 failure = death
## 3 success = stable, but unconscious