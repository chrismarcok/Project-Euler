def f(n)->int:
    """
    >>> f(3)
    25
    >>> f(5)
    101
    >>> f(7)
    261
    """
    sum = 1
    modifier = 2
    for x in range((n-1) // 2):
        for y in range(4):
            #print("sum: {}, modifier: {}".format(sum, modifier))
            sum += (1 + modifier)
            if y == 3:
                modifier += 2 * (x + 2)
            else:
                modifier += 2*(x + 1)
            #print(sum)

    return sum
print(f(1001))
