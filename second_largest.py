def second_largest(numbers):
    largest1 = numbers[0]
    largest_list1 = []

    for num in numbers:
        if num > largest1:
            largest1 = num

    for num in numbers:
        if num != largest1:
            largest_list1.append(num)

    largest2 = largest_list1[0]
    for num in largest_list1:
        if num > largest2:
            largest2 = num
    return largest2

# def second_largest(numbers):
#     return sorted(numbers)[-2]

print(second_largest([4, 9, 2, 7]))     # 7
print(second_largest([1, 5, 3, 8]))     # 5
print(second_largest([10, 3, 7]))       # 7
print(second_largest([9, 2, 7]))        # 7
print(second_largest([-5, -2, -9]))     # -5