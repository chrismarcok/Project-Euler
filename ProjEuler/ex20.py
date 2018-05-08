prod = 1
for x in range(1, 101):
    prod *= x

def sum_digits(n) -> int:
    """
    >>> sum_digits(123)
    6
    >>> sum_digits(1234567)
    28
    """
    sum = 0
    for x in range(len(str(n))):
        sum += (n % 10)
        n = n // 10
    return sum

print(sum_digits(prod))
