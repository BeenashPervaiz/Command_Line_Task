# Looping and in keyword in dictionaries
user = {'name':'Beenash',
'age': 20, 
'fav_Books':['Khuda aur Muhbaat','The Holy Book'],
'fav_movies':['ABC2','Saaho']
}

#checking if key exist in dictionary
if 'name' in user: #in  keyword only see the key(name, age, fav_books etc)
    print('Present')
else:
    print('Not Present')
#checking if value exist in dictionary--->Values methods
if '20' in user.values():
    print('Present')
else:
    print('Not Present')
# also check the list
if ['Khuda aur Muhbaat','The Holy Book'] in user.values():
    print('Present')
else:
    print('Not Present')

#Looping in dictionary
#for i in user: #print the all keys
 #   print(i)
for i in user.values(): #print the all values
    print(i)
#2nd method to print values
for i in user: #print the all values
    print(user[i])
#keys method
user_key = user.keys()
print(user_key)
print(type(user_key))
#values method
user_values = user.values()
print(user_values)
print(type(user_values))
######
#item method is most important in dictionaries
user_item = user.items()
print(user_item)
print(type(user_item))
#useful method in dictionary
for key, value in user.items():
    print(f"key is: {key} values is: {value}")


