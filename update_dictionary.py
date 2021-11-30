# update dictionary

# add and delete data
user = {'name':'Beenash',
'age': 20, 
'fav_Books':['Khuda aur Muhbaat','The Holy Book'],
'fav_movies':['ABC2','Saaho']
}
more_info = {'state': 'Punjab', 'Hobbies':['reading','Gradening']}
#update dictionary
user.update(more_info)
print(user)
#same key in the dictionaries is not add it only change the same key name like this example 
name = {'name': 'Beenash Pervaiz'}
user.update(name)
print(user)
