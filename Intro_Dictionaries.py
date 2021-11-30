#dictionaries 
#unordered collection of data in key:  value pair.  
#first way to representing the dictionaries
user1 = {'name':'Beenash','age' :20}
print(user1)
print(type(user1))
#second method to representing the dictionaries/dict method
user2 = dict(name = 'Pervaiz',age = 42)
print(user2)
print(type(user2))
#how to access data from dictionaries
print(user1['name'])
print(user2['age'])
#which type of data dictionaries can store?
# anything we can store 
user3 = {'name':'Beenash',
'age': 20, 
'fav_Books':['Khuda aur Muhbaat','The Holy Book'],
'fav_movies':['ABC2','Saaho']
}
print(user3)
print(user3['fav_Books'])
#how to add data to empty dictionary?
user4 = { }
user4['name'] = 'Samar'
user4['age'] = 24
print(user4)
