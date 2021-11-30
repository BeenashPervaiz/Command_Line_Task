#1st method:  fromkey methods(used to create dictionary)
#dic = {'name':'unknown','age':'unknown'}
#dic1 = dict.fromkeys(['name','age','height'],'unknown')#we also here write tuples dict.fromkeys(('name','age','height'),'unknown')
#print(dic1)
#dic2 = dict.fromkeys(range(1,11),'unknown')
#print(dic2)
#2nd method is get method (useful method)
dic = {'name':'unknown','age':'unknown'}
#print(dic['names'])#not in dictionary
print(dic.get('name'))
print(dic.get('names'))

if 'name' in dic:
    print('present')
else:
    print('Not present')

if dic.get('names'):
    print('present')
else:
    print('Not present')

#copy method
dic3 = dic #that is also the way to copy the data
dic2 = dic.copy()
print(dic2)
print(dic2.popitem())
print(dic)
print(dic == dic2)
print(dic3.popitem())
print(dic)
print(dic == dic3)

#clear method clear the data of dictionary
dic.clear()
print(dic)




