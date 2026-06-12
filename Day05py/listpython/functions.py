# def my_function():
# print("Hello From my functions")

# my_function()

    #default fucntions
def great(name="User"):
    print(name)
    print(f"hello, {name}!")

great()

# #question of interview find the odd even number using functions
# def Evenodd(number):
#     if(number%2==0):
#         return "Even"
#     else: 
#         return "Odd"
    
# number = int(input("enter the number "))
# print(Evenodd(number))

#questions return the string without using inbuild function
str1 = "Aashish"

rev = ""

for ch in str1:
    rev = ch + rev

print(rev)
        

#swap two variables
# def swap(a,b):
#     a, b = b, a 
#     return a,b

# a, b = swap(a:10, b:20)
# print("a =",a ,"b=",b)


#fibonacci series
n = 10

a = 0
b = 1

print("Fibonacci Series:")

for i in range(n):
    print(a, end=" ")
    
    c = a + b
    a = b
    b = c

#     #fibonacci series with input users
# n = int(input("Enter number of terms: "))

# a = 0
# b = 1

# for i in range(n):
#     print(a, end=" ")
    
#     c = a + b
#     a = b
#     b = c

#*args
def add(*args):
    total = 0

    for num in args:
        total += num

    print("Sum =", total)

add(10, 20)
add(10, 20, 30)
add(1, 2, 3, 4, 5)

#**kwargs

def student(**kwargs):
    print(kwargs)

student(name="Aashish", age=20, city="Pune")

#lambda functions 
#add of using lambda functions 

add = lambda a , b : a + b
print(add(10,20))

#find even odd function using lambda
even = lambda n :n % 2 == 0
print(even(8))

# Pass in functions 
def greet():
    pass

print("Program Running")

#Palindrome using functions
str1 = input("Enter a string: ")

rev = ""

for ch in str1:
    rev = ch + rev

if str1 == rev:
    print("Palindrome")
else:
    print("Not Palindrome")


#upper to lower in functions
to_lower = lambda s: ''.join(
    chr(ord(ch) + 32) if 'A' <= ch <= 'Z' else ch
    for ch in s
)

print(to_lower("AASHISH"))

#Lowercase to Uppercase using Lambda
to_upper = lambda s: s.upper()

print(to_upper("aashish"))

#local variable 
def display():
    name = "Aashish"   # Local Variable
    print(name)

display()

#global Variable
name = "Aashish"   # Global Variable

def display():
    print(name)

display()

#global password 
user_id = input("Enter User ID : ")
password = input("Enter Password : ")

def success(user_id, password):
    if user_id == "admin" and password == "1234":
        print("Login Successful")
    else:
        print("Invalid User ID or Password")

success(user_id, password)

#global banking 
balance = 1000

def withdraw(amount):
    global balance
    if amount <= balance:
        balance -= amount
        print(f"Withdrawal successful. Remaining balance: {balance}")
    else:
        print(f"Insufficient Balance.")

withdraw(200)
print(f"Balance outside function: {balance}")

#vowel 
string = input("Enter String : ")

def vowel(string):
    count = 0

    for ch in string.lower():
        if ch in "aeiou":
            count += 1
    
    return count

print("Number of vowels:", vowel(string))

#leetcode questions
def sort_list(arr):
    n = len(arr)

    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

numbers = [5, 2, 8, 1, 9]

print(sort_list(numbers))