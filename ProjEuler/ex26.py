from decimal import *
largest = 0
largest_item = None

lst = []
for x in range(1, 1000):
    num = str(1/Decimal(x))
    if len(num) < 19:
        continue
    else:
        lst.append(num)
#print(lst)

def repeats(substring: str, s:str) -> int:
    """
    >>> repeats("abc", "abcabcabc")
    3
    >>> repeats("a", "aaaaa") # 0 1 2 3
    5
    >>> repeats("ABRA", "ABRACADABRA")
    2
    """
    c = 0
    for x in range(len(s) - len(substring) + 1):
        if substring == s[x:x + len(substring)]:
            c += 1
    return c

def repeating(input: str) -> int:
    """
    >>> repeating("0.3333333333333333")
    1
    >>> repeating("0.16666666666666666")
    1
    >>> repeating("0.14285714285714285")
    6
    """
    for x in range(len(input)):
        for y in range(len(input)):
            if y <= x:
                continue
            else:
                substring = input[x:y]
                num = repeats(substring, input)

# for item in lst:
#     i = repeating(item)
#     if i > largest:
#         largest = i
#         largest_item = item
#
# for x in range(1, 1000):
#     num = str(1/Decimal(x))
#     if num == largest_item:
#         print(x)
#         break
