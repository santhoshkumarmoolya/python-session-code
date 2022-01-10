#if elif else

a = 30
b = 30

if a < b:
    print("a is less than b")
    print("This is an if statement")
elif a == b:
    print("a and b are equal")
    print("This is an else-if statement")
else:
    print("a is greater than b")
    print("This is an else statement")

print("im outside if")

# for loops in python
# many objects in python are iterable
# you can iterate over that object
list_of_empids = [121,122,123,125]
#print(list_of_empids[0])
#print(list_of_empids[1])
#print(list_of_empids[2])
#print(list_of_empids[3])

for x in list_of_empids:
    print(x)

string_alphabets = "abcdefgh"

string_reverse = ""
for ch in string_alphabets[::-1]:
    string_reverse += ch
    print(string_reverse)

tup = (1,2,3)
sum = 0
for num in tup:
    sum = sum + num

print(sum)

#tuple unpacking
mylist = [("santhosh","manager",30), ("rahul","vp",28), ("sravan","tester",25)]

for name, desig, age in mylist:
    print(age)

#dictionary with for loop

dict_emps = {"emp1":"santhosh", "emp2":"rahul", "emp3":"sunil"}
for item, value in dict_emps.items():
    print(item +" "+ value)

for key in dict_emps.keys():
    print(key)

for value in dict_emps.values():
    print(value)


a = 0
while(a<10):
    print(a)
    a = a + 1







