def find_sum(numbers):
    total = 0

    for num in numbers:
        total += num
    return(total)

print(find_sum([4, 9, 2, 7]))