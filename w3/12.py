thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist) #The pop() method removes the specified index.

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist) #The del keyword also removes the specified index:

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist) #The clear() method empties the list.