# import numpy as np
#
# arr = np.array([1, 2, 3, 4])
# print(arr)
#
# arr2 = np.array([5, 6, 7, 8])
# print(np.append(arr, arr2))


n = int(input("enter number: "))


def factorial(n: int):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


print(factorial(n))

print("hello")
