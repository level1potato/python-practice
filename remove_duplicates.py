def remove_duplicates(items):
    result = []

    for item in items:
        if item not in result:
            result.append(item)
    return result

print(remove_duplicates([1, 2, 2, 3, 1]))    # [1, 2, 3]
print(remove_duplicates(["a", "b", "a"]))    # ['a', 'b']
print(remove_duplicates([]))                 # []
