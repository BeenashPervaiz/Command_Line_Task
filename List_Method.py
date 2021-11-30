furit = ['orange', 'Mango', 'banana', 'Apple','Pear','pineapple', 'Grave','Apple']
print("count Method")
print(furit.count('Apple')) #count method
print("Sort  Method")
furit.sort()# sort method
print(furit)

Number = [2,5,6,9,4,1]
# ("Sorted function ")
print(sorted(Number))#it sorted our list for show output only
#("Sorted Method ")
Number.sort()#sort our list orginal
print(Number)   #both are correct
#("Copy Method")
Number_copy = Number.copy() #copy the data 
print(Number_copy)
#("reverse Method")
Number_copy.reverse()
print(Number_copy)
#("Clear Method")
Number.clear()#clear our list/empty
print(Number) 