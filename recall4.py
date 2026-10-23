def count_evens(numbers):

    counter = 0

    for num in numbers:
        if num % 2 == 0:
            counter += 1
    return counter

print(count_evens([4, 9, 2, 7]))     # 2
print(count_evens([1, 3, 5]))        # 0
print(count_evens([0, -2, -3]))      # 2