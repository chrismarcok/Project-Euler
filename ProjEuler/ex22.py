f = open("p022_names.txt", "r")
s = f.read().split(",")

for x in range(len(s)):
    s[x] = s[x].strip('"')

s.sort()
total = 0

def name_to_score(var: str) -> int:
    """
    >>> name_to_score("COLIN")
    53
    """
    sum = 0
    for char in var:
        sum += (ord(char) - 64)
    return sum

for x in range(len(s)):
    total += ((x + 1) * name_to_score(s[x]))
print(total)
