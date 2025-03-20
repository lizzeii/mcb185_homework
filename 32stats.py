import math

num = [1, 2, 3, 4]

##number of values in the list
print(len(num))

##minimum value in the list
def minimum(num):
    mini = num[0]
    ##minimum for 1 item is that item
    for n in num[1:]:
        if n < mini:
            mini = n
            ##replaces the minimum with each iteration if there is a smaller number
    return mini
print(minimum(num))

##maximum value in the list
def maximum(num):
    maxi = num[0]
    ##maximum for 1 item is that item
    for n in num[1:]:
        if n > maxi:
            maxi = n
            ##replaces the maximum with each iteration if there is a smaller number
    return maxi
print(maximum(num))

##mean of the list
def mean(num):
    total = 0
    for n in num:
        total += n
        ##adds each item onto the total
    return total / len(num)
    ##mean formula
print(mean(num))

#standard deviation of the list
def std(num):
    sum = 0
    for n in num:
        sum = n + mean(num)
    return (sum ** 2) / (len(num) - 1)
print(std(num))

##median of the list
def median(num):
    if len(num) % 2 == 0:
        for n in num:
            n1 = n / 2
            n2 = n1 + 2
        return (n1 + n2) / 2
    else:
        for n in num:
            n += 1
        return n / 2
print(median(num))