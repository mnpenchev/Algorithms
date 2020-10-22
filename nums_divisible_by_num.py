def divisible_by(numbers, divisor):
    lis = []
    for n in numbers:
        if n % divisor == 0:
            lis.append(n)


print(divisible_by([1,2,3,4,5,6], 2))
