import math

def isPrime(n)->bool:
    """
    >>> isPrime(1)
    False
    >>> isPrime(13)
    True
    >>> isPrime(25)
    False
    >>> isPrime(36)
    False
    >>> isPrime(59)
    True
    >>> isPrime(199)
    True
    >>> isPrime(2)
    False
    >>> isPrime(149)
    True
    """
    if n == 2:
        return True
    elif n == 1 or n == 0 or n % 2 == 0:
        return False
    largestNum = n**0.5
    for x in range(2, math.trunc(largestNum) + 1):
        if n % x == 0:
            return False
    return True

def nextLargestPrime(lst) -> int:
    biggest = max(lst)
    biggest += 1
    while not isPrime(biggest):
        biggest += 1
    return biggest

lst = [2]
while len(lst) < 10001:
    lst.append(nextLargestPrime(lst))

print(lst[-1])
