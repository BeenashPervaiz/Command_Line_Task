#more about set methods
#in keyword in sets and for loop
set = {'a','b','c'}
#in keyword to check if item is present or not in set
if 'a' in set:
    print("Present")
else:
    print("Not Present")
#for loop
for item in set:
    print(item) #data print the unorder way

#set maths main use
s1 = {1,2,3,4,5}
s2 = {2,5,7,9}

#union (all element in both set)
union_set = s1 | s2
print(f"Union of the both  set s1 and s2: {union_set}")
#intersection (same element of both set)
intersection_set = s1 & s2
print(f"intersection of the both  set s1 and s2: {intersection_set}")