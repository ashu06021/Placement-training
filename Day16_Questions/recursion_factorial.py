# Question:
# Write a Python program to find factorial using recursion.
#
# Concept:
# Recursion means a function calls itself.

def factorial(n):

    if n == 1:
        return 1

    return n * factorial(n - 1)

num = int(input("Enter Number: "))

print("Factorial =", factorial(num))