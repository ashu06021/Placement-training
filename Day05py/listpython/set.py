#Print Set 
myset = {"apple", "banana", "cherry"}
print(myset)

#duplicate values in set
myset = {"apple", "banana", "cherry", "apple"}
print(myset)

#empty set print 
a=set()
print(type(a))
a={'Ashish',10,10.5,True}
print(a)

# set with list inside it
#myset = {"apple", "banana", "cherry", ["a", "b", "c"]} # this will give error because set cannot store list inside it
#print(myset)

#delete element from Set
# Use remove() when you're sure the element exists.
# Use discard() when you're not sure and want to avoid errors. 
# Randomly deletes element from set
a = {1, 2, 3, 4, "Aryan", "Aashish"}
print(type(a))

a.pop()      # Removes an arbitrary element from the set
print(a)

a.remove(2) # Removes the specified element (2)
print(a)

# Discard 
b = {1, 2, 3, 4}
b.discard(2)
print(b)

