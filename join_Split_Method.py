#split Method
#convert string into list
User_Name = 'Beenash 20'.split()
print(User_Name)
User_Name = 'Beenash$20'.split('$')
print(User_Name)
name, age = input("enter user name and age: ").split()
print(name)
print(age)
#join Method
#convert list into string
Student = ['Beenash', '20']
print(','.join(Student))