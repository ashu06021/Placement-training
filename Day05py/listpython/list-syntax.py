a = {"a", "b", "c", "d", "e"} #list of set for printing unique values
print(a)

#add element into set using append method
a = ["a", "b", "c", "d", "e"] 
a.append("f")
print(a)


#add element into set using insert method
#a = ["a", "b", "c", "d", "e"]
#a.insert("f")
#print(a)

#add element into specified index using insert method
a = ["a", "b", "c", "d", "e"]
a.insert(6, "f")
print(a)

#add element into set using extend method
a = ["a", "b", "c", "d", "e"]   
b = ["f", "g", "h", "i", "j"]
a.extend(b)
print(a)

#delete element from set using remove method
a = ["a", "b", "c", "d", "e"]
a.remove("c")
print(a)

#delete element from set using pop method
a = ["a", "b", "c", "d", "e"]   
a.pop(2)
print(a)

# calculate the average of a list of numbers
numbers = [1, 2, 3, 4, 5]
average = sum(numbers) / len(numbers)
print(average)
