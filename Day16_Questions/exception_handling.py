# Question:
# Write a Python program to handle division by zero error.
#
# Concept:
# Exception Handling is used to prevent program crashes.
# try -> code that may cause error
# except -> handles error
# finally -> always executes

try:
    num = int(input("Enter a number: "))

    result = 100 / num

    print("Result:", result)

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Invalid Input")

finally:
    print("Program Ended")