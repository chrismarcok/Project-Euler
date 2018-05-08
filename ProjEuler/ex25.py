d = {1: 1, 2: 1}

def fib(n: int, d: dict) -> int:
    """
    >>> d = {1: 1, 2: 1}
    >>> fib(10, d)
    55
    >>> fib(12, d)
    144
    """
    if n in d:
        return d[n]
    d[n] = fib(n-1, d) + fib(n-2, d)
    return d[n]

i = 1

def num_digits(n: int) -> int:
    s = str(n)
    return len(s)

while num_digits(fib(i, d)) != 1000:

    i += 1
print(i)
