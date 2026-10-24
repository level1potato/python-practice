# def fizzbuzz(numbers):

#     result = []

#     for n in numbers:
#         if n % 3 == 0 and n % 5 == 0:
#             result.append("FizzBuzz")
#         elif n % 3 == 0:
#             result.append("Fizz")
#         elif n % 5 == 0:
#             result.append("Buzz")
#         else:
#             result.append(n)
#     return result
    
# print(fizzbuzz(range(1, 16)))

def fizzbuzz():
    for n in range(1, 16):
        if n % 15 == 0:
            print("FizzBuzz")
        elif n % 3 == 0:
            print("Fizz")
        elif n % 5 == 0:
            print("Buzz")
        else:
            print(n)

fizzbuzz()
