lst = []
for y in range(999, 99, -1):
    for x in range(999, 99, -1):
        lst.append(y*x)

def largest_pal(lst: list) -> int:
    largest = -1
    for x in range(len(lst)):
        if isPalendrome(lst[x]) and lst[x] > largest:
            largest = lst[x]
    return largest


def isPalendrome(num: int) -> bool:
    """
    >>> isPalendrome(1001)
    True
    >>> isPalendrome(101)
    True
    >>> isPalendrome(11)
    True
    >>> isPalendrome(1)
    True
    >>> isPalendrome(1021)
    False
    """
    num = str(num)
    for x in range(len(num)):
        if num[x] != num[-1-x]:
            return False
    return True


print(largest_pal(lst))
