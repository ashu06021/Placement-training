def even_numbers(n):
    for i in range(n+1):
      if i % 2 == 0:
         yield i
g=even_numbers(10)
print(next(g))
print(next(g))
print(next(g))


#sqaure using generator 
def square_generator(n):
    for i in range(1, n + 1):
        yield i * i

n = 5

for square in square_generator(n):
    print(square)

#Generator for Odd Numbers / even numbers
def even_generator(n):
    for i in range(1, n + 1):
        if i % 2 == 0:
            yield i

n = 10

for even in even_generator(n):
    print(even)

def odd_generator(n):
    for i in range(1, n + 1):
        if i % 2 != 0:
            yield i

n = 10

for odd in odd_generator(n):
    print(odd)


#prime_number using generator
def prime_generator(n):
    for num in range(2, n + 1):
        is_prime = True

        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            yield num

n = int(input("Enter a number: "))

print("Prime Numbers:")

for prime in prime_generator(n):
    print(prime)