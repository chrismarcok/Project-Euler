lst = []

for x in range(365 * 100 + 25): #365 days * 100 years + 25 leap year days
    lst.append((x+2) % 7) # first day is a tuesday, # 0 = sun, 1 = mon, 2 = tues ... 6 = sat.

lst2 = []
for x in range(1901, 2001): # for each year
    for y in range(12):
        days = -1
        if y == 0 or y == 2 or y == 4 or y == 6 or y == 7 or y == 9 or y == 11: # 31 days
            days = 31
        elif y == 1: #feb
            if x % 4 == 0:
                days = 29
            else:
                days = 28
        else:
            days = 30
        for z in range(1, days + 1):
            lst2.append(z)




count = 0
for x in range(len(lst)):
    if lst[x] == 0 and lst2[x] == 1:
        count += 1
print(count)
