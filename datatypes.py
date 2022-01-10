#int - 10 20 30 40
#float - 10.25 20.12 30.52
#str - "rahul" "sunil"
#boolean - True False
#list - [10,20,30] ["hello", 10, [1,23]]
#dictionary - {"key":"value", "age":30 }
#set - {10,20,30}
#tuple - (10,20,30)

# casting

a = "hello"
b = " world"
sum = str(a) + str(b)

#String

# r a h u l
# 0 1 2 3 4

# r  a  h  u  l
# 0 -4 -3 -2 -1

name = "rahul"
age = "30"
#print(name)
#print(age)
#print(len(age))

#indexing in strings
#print(name[3])

#slicing in strings
characters = "abcdefgh"
#print(characters[1:4])
#print(characters[2:5])
#print(characters[0:8:3])

# string is immutable
name = "Sam"
# name[0] = 'P'
new_name = 'P' + name[1:]
#print(new_name)

# To concatenate two strings use +
sum = 10 + 20
print(sum)

sum = "10" + "20"
print(sum)

sum = str(10) + "20"
print(sum)

first_name = "sam"
last_name = "mathew"

print(first_name.capitalize())
print(last_name.capitalize())

message = "How !are:yo:u:rahul"
print(message.split('!'))

emailid = "rahul@gmail.com"
print(emailid.split('@'))

emailid = "rahul@gmail.com.com"
print(emailid.replace("."," "))


#indexing
#slicing
#len
#split
#replace

name = "kunal"
age = 30

# print formating
print("Hello world")

# using string concatenation +
print("Hello " + name)

# using print format method
print("my name is {} and my age is {}".format(age, name))

#using f-string literal
print(f'my name is {name} and my age is {age}')

# this is a comment
# this is second line
# this is third line

"""
this is first line
this is second line
this is third line
"""
a = 10
print(type(a))
a = "kunal"
print(type(a))

# variables - container for data, rules for variable names
# data types - int, float, str, boolean, list, tuple, set, dictionary
# string indexing and slicing - [index] [start:stop:step]
# string methods - len, upper, lower, capitalize, split, replace
# print formatting - using +, using format method, using f-string literal


