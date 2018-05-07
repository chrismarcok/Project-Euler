def sum_of_multiples(num: int) -> int:
    i = 0
    sum = 0
    while i < num:
        if i % 3 == 0 or i % 5 == 0:
            sum += i
        i+=1
    return sum

if __name__ == "__main__":
    print(sum_of_multiples(1000))
