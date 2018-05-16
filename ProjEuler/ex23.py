def is_abundant(n: int) -> bool:
    """
    >>> is_abundant(12)
    True
    """
    divisors = [x for x in range(1, n//2 + 1) if n % x == 0]
    return sum(divisors) > n

# abundant_list = [x for x in range(1, 28124) if is_abundant(x)]
file = open("abundant_nums23.txt", "r") # file of [x for x in range(1, 28124) if is_abundant(x)]
abundant_list = eval(file.read())


lst = []
for x in abundant_list:
    for y in abundant_list:
        if x + y > 28123:
            break
        lst.append(x+y)
        print(x)
lst = set(lst)
nums = [x for x in range(1, 28124)]
nums = set(nums)
nums = nums - lst
print(sum(nums))
