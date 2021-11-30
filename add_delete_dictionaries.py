# add and delete data
user = {'name':'Beenash',
'age': 20, 
'fav_Books':['Khuda aur Muhbaat','The Holy Book'],
'fav_movies':['ABC2','Saaho']
}
#how to add data in dictionaries?
user['fav_game'] = ['hockey','cricket']
print(user)

#pop method to delete add
popped_item = user.pop('fav_movies')#we must pass a key inside pop method other error came
print(f"popped item is {popped_item}")
print(user)

# popitem method
popped_item1 = user.popitem()#remove the item from last
print(f"popped item is {popped_item1}")
print(type(popped_item1))
print(user)

