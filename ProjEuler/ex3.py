import math
def isPrime(n) -> bool:
    if n == 2:
        return True
    if n == 1 or n == 0 or n % 2 == 0:
        return False
    largestNum = n**0.5
    for x in range(2, math.trunc(largestNum) + 1):
        if n % x == 0:
            return False
    return True

i = 600851475143
lst = []
while i != 1:
    for x in range(600851475143):
        if isPrime(x) and i % x == 0:
            i = i // x
            lst.append(x)
            break
print(max(lst))
