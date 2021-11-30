#commonn method to delete data
furit = ['orange', 'Mango', 'banana', 'Apple','Pear','pineapple', 'Grave']
print(furit)
#pop method :pop() by default delete data from the end of list
furit.pop()
print(furit)
#if we give position than delete from position
furit.pop(2)
print(furit)

# delete operator
del furit[0]
print(furit)

#remove method
#we are not know the position than remove method used
furit.remove('Apple')
print(furit)





