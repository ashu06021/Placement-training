# A dictionary 

#exaxmple of dictionary
#my_dict = {}

#methos of dict

## 1 accessing values
my_dict = {'name':'ashish', 'age':18, 'City' : 'Pune'}
print(my_dict['name'])
print(my_dict['City'])

# 2 Adding or updating items
my_dict = {'name': "Aryan", 'age': 30, 'city': "Pune"}
print(my_dict)

# Change values
my_dict['name'] = "Aashish"
my_dict['age'] = 25
my_dict['city'] = "Mumbai"

print(my_dict)

#3 updating an existing item
my_dict={'name': 'amish' ,'age':32}
my_dict['name'] = 'ashish'
print(my_dict)

# How to remove key-value pair from dictionary

my_dict = {'name': "Aryan", 'age': 30, 'city': "Pune"}
print(my_dict)

my_dict.pop('age')
print(my_dict)

del my_dict['city']
print(my_dict)

# nested dictionary
nested_dict = {
    'Person': {'name': 'Ashish' , 'age':32},
    'address' : {'city' : 'Pune ', 'Zip': '1001'} # type: ignore

}  
print(nested_dict)

# Update value
nested_dict['Person']['name'] = "Aryan"
print(nested_dict)

#Dictionary comprehension
squared_dict ={ x: x**2 for x in range(1,6)}
print(squared_dict)

#method 2 
dict = {"a " : 2, "b" : 3, "c":4}
for key in dict:
    dict[key] **=2

print(dict)

# Print squares greater than or equal to 4
squared_dict = {x: x**2 for x in range(1, 5)}

for key, value in squared_dict.items():
    if value >= 9:
        print(key, ":", value)