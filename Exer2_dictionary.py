#take the input from m  user in dictionary
user_info ={}

name = input("Enter the name of user: ")
age = int(input("Enter the age of user: "))
fav_Books = input("Enter the Fav books of the user and separated by comma: ").split(',')
Hobbies = input("Enter the hobbies of the user and separated by comma: ").split(',')

user_info['name'] = name
user_info['age'] = age
user_info['fav_Books'] = fav_Books
user_info['Hobbies'] = Hobbies

print(f"print all the information of the user: {user_info}")
