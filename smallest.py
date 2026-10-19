def find_smallest(numbers):
    if not numbers:
        return "List should not be empty"

    smallest = numbers[0]
    
    for num in numbers:
        if num < smallest:
            smallest = num
    return(smallest)

print(find_smallest([])) 
print(find_smallest([4, 9, 2, 7]))   # should be 2
print(find_smallest([4, 9, 2, 1]))   # should be 1
print(find_smallest([1, 5, 3]))      # should be 1