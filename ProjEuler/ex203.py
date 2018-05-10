import math

def nCr(n,r):
    if r == 0 or n == r:
        return 1
    f = math.factorial
    return f(n) // f(r) // f(n-r)

def isPrime(n)->bool:
    if n == 2:
        return True
    elif n == 1 or n == 0 or n % 2 == 0:
        return False
    largestNum = n**0.5
    for x in range(2, math.trunc(largestNum) + 1):
        if n % x == 0:
            return False
    return True

def squareFree(n: int) -> bool:
    """
    >>> squareFree(1)
    True
    >>> squareFree(2)
    True
    >>> squareFree(4)
    False
    >>> squareFree(35)
    True
    >>> squareFree(20)
    False
    >>> squareFree(21)
    True
    """
    for x in range(1, math.trunc(n**.5) + 1):
        if isPrime(x):
            if n % x**2 == 0:
                return False
    return True

lst = []

for x in range(51):
    for y in range(x + 1):
        var = nCr(x, y)
        if var not in lst and squareFree(var):
            lst.append(nCr(x, y))
        print("x: " + str(x) + "     |     y: " + str(y) + "/" + str(x))

print(sum(lst))
