def find_smallest(numbers):
    if numbers == []:
        return "List should not be empty"

    smallest = numbers[0]
    
    for num in numbers:
        if num < smallest:
            smallest = num
    return smallest

print(find_smallest([4, 9, 2, 7]))   # 2
print(find_smallest([4, 9, 2, 1]))   # 1
print(find_smallest([]))             # your message