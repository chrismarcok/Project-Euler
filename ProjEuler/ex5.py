def isDivisible(num: int) -> bool:
    for x in range(1, 21):
        if num % x != 0:
            return False
    return True

i = 20
while not isDivisible(i):
    i += 20
print(i)
