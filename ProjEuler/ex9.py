for a in range(3, 1000):
    for b in range(4, 1000):
        c = 1000 - b - a
        if a**2 + b**2 == c**2:
            print(a*b*c)
