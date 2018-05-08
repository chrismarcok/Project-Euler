d = {0: "", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: 'seven', 8: "eight", 9: "nine",
     10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 17: "seventeen", 19: "nineteen",
     15: "fifteen", 16: "sixteen", 18: "eighteen",
     20: "twenty", 30: "thirty", 40: "forty",
     50: "fifty", 60: "sixty", 70: "seventy", 80: 'eighty', 90: 'ninety', 1000: "onethousand"}

def num_to_letters(x) -> str:
    if x in d:
        return d[x]

    if x < 100:
        tens = x //10
        ones = x % 10
        return d[tens*10] + d[ones]

    else:
        hundreds = x // 100
        tens = (x % 100) // 10
        ones = x % 10
        if tens == 0 and ones == 0:
            return d[hundreds] + "hundred"
        if tens == 1:
            return d[hundreds] + "hundredand" + d[10 + ones]
        return d[hundreds] + "hundredand" + d[tens*10] + d[ones]

s = ""
for x in range(1, 1001):
    s += num_to_letters(x)

print(len(s))
