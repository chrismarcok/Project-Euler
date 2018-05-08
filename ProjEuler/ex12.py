import math

def triangle1(n) -> int:
    return int((n*(n+1)) / 2)

def divisorsOf(num: int) -> int:
    """
    >>> divisorsOf(2)
    2
    >>> divisorsOf(59)
    2
    >>> divisorsOf(15)
    4
    >>> divisorsOf(16)
    5
    """
    count = 0

    if num**0.5 % 1 == 0: # if num is a perfect square
        count = -1

    for x in range(1, math.trunc(num**0.5) + 1):
        if num % x == 0:
            count += 2
    return count


i = 1
while divisorsOf(triangle1(i)) <= 500:
    i += 1
print(triangle1(i))
