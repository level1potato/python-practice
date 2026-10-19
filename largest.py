def find_largest(numbers):
    if numbers == []:
        return("N/A")
        
    biggest = numbers[0]

    for num in numbers:
        if num > biggest:
            biggest = num
            
    return(biggest)
    
print(find_largest([4, 9, 2, 7]))
print(find_largest([1, 5, 3, 8]))
print(find_largest([10, 3, 7]))
print(find_largest([]))