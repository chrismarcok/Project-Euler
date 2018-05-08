
def sum_proper_divisors(n: int) -> int:
    """
    >>> sum_proper_divisors(220)
    284
    >>> sum_proper_divisors(284)
    220
    >>> sum_proper_divisors(16) # 1, 2, 4, 8, = 15
    15
    """
    return sum([x for x in range(1, n//2 + 1) if n % x == 0])

d = {}
amicable_nums = []


for x in range(10000):
    d[x] = sum_proper_divisors(x)

for key in d:
    for other_key in d:
        if key == other_key:
            continue
        if d[key] == other_key and d[other_key] == key:
            amicable_nums.append(d[key])

print(sum(amicable_nums))
