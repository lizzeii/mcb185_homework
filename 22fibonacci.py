x = 0
print(x)
##first number in seq
y = 1
print(y)
##second number in seq

for i in range(8):
    z = x + y
    ##creates third number in seq
    x = y
    y = z
    ##shifts second number to first and third to second
    print(z)
##how do i put the first two numbers in the loop?