file = open("sum13.txt", "r")
data = file.read()
data = data.split("\n")

for x in range(len(data)):
    data[x] = int(data[x])

print(str(sum(data))[:10])
