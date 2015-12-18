def sum_mul(math, *arg):
    if math == "sum":
        sum = 0
        for i in arg:
            sum = sum + i
        return sum

    elif math == "mul":
        mul = 1
        for i in arg:
            mul = mul * i
        return mul


result = sum_mul('sum', 1, 2, 3, 4, 5)
print(result)

result = sum_mul('mul', 1, 2, 3, 4, 5)
print(result)
