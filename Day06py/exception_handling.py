# Exception Handling
# Used to handle runtime errors gracefully.
# Keywords: try, except, else, finally

try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Please enter a valid number")

finally:
    print("Program Ended")