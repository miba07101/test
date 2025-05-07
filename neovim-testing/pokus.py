# import numpy as np
#
# arr = np.array([1, 2, 3, 4])
# print(arr)
#
# arr2 = np.array([5, 6, 7, 8])
# print(np.append(arr, arr2))


# n = int(input("enter number: "))

# %%
n = 10


def factorial(n: int):
    if n< 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result=1
    for i in range(1, n + 1):
        result *= i
    return result


print(factorial(n))

# %%
print("hello")
ano = 3


def fun():
    print(f"hello {ano}")


# hello
# %%
def foo():
    print("foo")


# %%
print("I am the first cell")
# akos sa mas
print("I am still the first cell")

# %%

print("I am the first cell")
print("I am still the first cell")

# %% anything can follow
print("I am the second cell")
print("I am still the second cell")
print("I am still, still the second cell")

# %%
print("I am the third cell")
