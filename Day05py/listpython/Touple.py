#Key Characteristics of Tuple
#1. Ordered: Tuples maintain the order of elements as they were defined.   
#2. Immutable: Once a tuple is created, its elements cannot be modified, added, or removed. This means that you cannot change the contents of a tuple after it has been defined.
#3 Allows duplicate - tuples can contain deuplicate values.
#4 Heterogeneous - tuples can contain different types of data, such as integers, strings, and floats.
#5 Indexing and slicing - tuples support indexing and slicing, allowing you to access specific elements or subsets of the tuple.


#type casting of tuple to list
a = (1,2,3,4,5) 
b =list(a)
print(type(b))
print(b)

# tuple with a list inside it
list_tuple = (1,2,3,4,5,[6,7,8,9,10])
print(list_tuple)

# Nested tuple
nested_tuple = (1,2,3,(4,5,6),7,8,9)
print(nested_tuple)

#difference between list and tuple
a = [1,2,3,4,5] 
a[0]=10
print(a)

#b = (2,3,4) this will give error because tuple is immutable and we cannot change the values of tuple after creating it
#b[0]=10
#print(b)

#Printing indes of elements
a = (1,2,3,4,5)
print(a.index(3))
print(a.index(5))
print(a.index(1))
print(a.index(2))

#
a = [1,2,3,4,5,6,7,8,9,10]

#count function
a = [1,2,3,4,5,6,7,8,9,10]
count1 = a.count(2)
print(count1)

#printing the slice of the list
a = [1,2,3,4,5,6,7,8,9,10]
sliced_list = a[2:-1]
print(sliced_list)
 