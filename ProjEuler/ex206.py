import math
big = 1929394959697989990
small = 1020304050607080900
a = 0
for x in range(math.trunc(small ** 0.5), math.trunc(big ** 0.5) + 1, 10):
    s = x ** 2
    s = str(s)
    print(s)
    if s[0] == "1" and \
        s[2] == "2" and \
        s[4] == "3" and \
        s[6] == "4" and\
        s[8] == "5" and \
        s[10] == "6" and \
        s[12] == "7" and \
        s[14] == "8" and \
        s[16] == "9" and \
        s[18] == "0":
        a = x
        break
print(a)
