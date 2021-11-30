#introduction to the sets
#Unordered collection of unique items
#string = {1,2,3} We cannot repeat the one element again and again.
# we cannot store the list, Tuples, Dictionaries in the sets
s = {1,2.4,'string','integer','character','float','cannot store in sets List, Tuples, Dictionaries'}
print(f"That data we can store inside the set and are not:  {s}")
list1 = {1,2,3,4,5,6,5,5,5,3,3,3,8,7}
#remove the duplicate element

set2 = set(list1)
print(f"output in set form: {set2}")

s = list(set(list1))
print(f"output in list form: {s}")
#sets methods
#add a item inside the set
set2.add(9)
set2.add(5)
set2.add(0)
print(f"Add element inside the set: {set2}")

#how to remove elements from sets
#remove method
set2.remove(5)
#set2.remove(10)#give the error because in set 10 not present

#dicard method is used for remove the element if element is not present thst give the error like remove method
set2.discard(8)
set2.discard(10)
print(f"remove element a from the set: {set2}")
#copy method
set3 = set2.copy()
print(f"copy the all data from the set: {set3}")
#clear method
set2.clear()
print(f"clear the all data from the set: {set2}")
