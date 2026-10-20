def find_largest(numbers):
    if not numbers:
        return "List should not be empty"
    largest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num
    return(largest)

print(find_largest([4, 9, 2, 7]))    # 9
print(find_largest([10, 3, 7]))      # 10
print(find_largest([]))              # your message