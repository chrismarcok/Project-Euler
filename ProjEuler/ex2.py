def fibonnaci(x, d: dict):
    if x in d:
        return d[x]
    else:
        d[x] = fibonnaci(x-1, d) + fibonnaci(x-2, d)
        return d[x]

d = {1: 1, 0: 1}

sum = 0
i = 1

while fibonnaci(i, d) < 4000000:
    if fibonnaci(i, d) % 2 == 0:
        sum += fibonnaci(i, d)
    i += 1
print(sum)
