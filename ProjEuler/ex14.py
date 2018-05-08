largest_x = 0
largest = 0


def collatz_len(x) -> int:
    """
    >>> collatz_len(1)
    1
    >>> collatz_len(13)
    10
    """
    i = 1

    while x != 1:
        if x % 2 == 0:
            x = x/2
        else:
            x = 3*x + 1
        i += 1
    return i

for x in range(1000, 1000000):
    length = collatz_len(x)
    print("x: " + str(x) + "     |        len: " + str(length))
    if length > largest:
        largest = length
        largest_x = x

print(largest_x)
