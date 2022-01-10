# list - to store multiple items in a variable
empname = "rahul"
print(empname[2])

list_of_empids = [121, 122, 135, 123, 137, 150]
#print(type(list_of_empids))
#print(len(list_of_empids))
#print(list_of_empids[2])
#print(list_of_empids[0:4:2])

#lists are mutable
list_of_empids[0] = 150
#print(list_of_empids)

list_of_empids.append(138)
print(list_of_empids)

list_of_empids.insert(1,151)
print(list_of_empids)

list_of_empids.insert(2,152)
print(list_of_empids)

list_of_empids.pop()
print(list_of_empids)

list_of_empids.pop(3)
print(list_of_empids)

list_of_empids.remove(152)
print(list_of_empids)

list_of_empids.sort()
print(list_of_empids)

list_of_empids.reverse()
print(list_of_empids)

print(list_of_empids.count(150))

#len
#type
#append
#insert
#pop
#remove
#sort
#reverse
#count