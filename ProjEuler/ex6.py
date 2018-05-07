def sum_of_squares(num: int)-> int:
    return sum([x**2 for x in range(1, num+1)])

def square_of_sums(num: int) -> int:
    return sum([x for x in range(1, num+1)])**2

print(square_of_sums(100) - sum_of_squares(100))
