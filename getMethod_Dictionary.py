#more about get method two same keys in dictionary
#use for to access the keys
user = {'name':'Beenash', 'age': 34  }
print(user.get('name'))
print(user.get('names','not Found!'))# if our key is not found then return not found
print(user)#same key has not the two value it override the pervious value