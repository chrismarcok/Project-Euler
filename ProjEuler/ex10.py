import math
sum = 0

def isPrime(x) -> bool:
    if x == 2:
        return True
    if x % 2 == 0 or x == 1 or x == 0:
        return False
    largestNum = x ** 0.5
    for y in range(3, math.trunc(largestNum) + 1, 2):
        if x % y == 0:
            return False
    return True

for x in range(2000000):
    if isPrime(x):
        sum += x

print(sum)
