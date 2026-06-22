# Question:
# Create a list of square numbers using list comprehension.
#
# Concept:
# List Comprehension is a short way to create lists.

numbers = [1, 2, 3, 4, 5]

squares = [num * num for num in numbers]

print("Original List:", numbers)

print("Square List:", squares)

even_numbers = [num for num in numbers if num % 2 == 0]

print("Even Numbers:", even_numbers)