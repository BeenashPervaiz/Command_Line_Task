#more method to add data in list
#insert method
#how to join two list
# extend method
#differnce between append and extend method
print("Insert Method")
furit = ['Mango', 'Orange']
#insert method is used for add data at specific position. 
furit.insert(1,"Grapes")
print(furit)
#if we give index number more than list length than data add at the end of list
furit.insert(11,"Apple")
print(furit)

#join two string
print("join two string")
furit1 = ['Banana','Apple']
furits = furit + furit1
print(furits)

#extend method: it add the data of second list in first list
print("Extend Method")
furit.extend(furit1)
print(furit)
print(furit1)

#append method: this is used for create list inside the list
print("Append Method")
furit.append(furit1)
print(furit)
print(furit1)