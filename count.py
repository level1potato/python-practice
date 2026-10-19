# count function
def count_evens(numbers):
    count = 0

    for num in numbers:
        if num % 2 == 0:
            count += 1
    return(count)

print(count_evens([4, 9, 2, 7]))     # mixed: should be 2
print(count_evens([1, 3, 5]))        # all odd: should be 0
print(count_evens([2, 4, 6]))        # all even: should be 3
print(count_evens([]))               # empty list: should be 0
print(count_evens([0, -2, -3]))      # zero and negatives: should be 2