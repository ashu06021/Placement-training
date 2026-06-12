#basic decorator code 

def my_deco(say_hello):
    def wrapper():
       print("before calling hello")
       say_hello()
       print("after calling hello")
    return wrapper
@my_deco


def say_hello():
 print("Hello Team")

say_hello()

#addition of two number decorator 

# def maths(add):
#     def addition(a, b):
#         add(a + b)
#     return addition

# @maths
# def add(result):
#     print(result)

# # Call it
# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))
# add(a, b)


#addition of two number method 1 
# def add_decorator(func):
#    def wrapper(a ,b):
#       print("before performing addition")
#       result = func(a , b)
#       print("after performing addition")
#       return result 
#    return wrapper

# @add_decorator
# def add_numbers(a , b):
#    return a + b
# print("result:", add_numbers(a=5, b=2))


#decorator for lowercase to uppercase
def uppercase(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper


@uppercase
def greet(name):
    return f"hello, {name}"


print(greet("aryan"))  

#method 2 
# def to_upper(greet):
#          def wrapper():
#             result = greet()
#             print(result.upper())
#         return wrapper
# @to_upper
# def greet():
#     return "hello world"
# print(greet())

