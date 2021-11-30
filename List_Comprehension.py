#list comprehension
#we can create the list in only one line with the help of comprehension

#create a list square from 1 to 10
print("1st example")
square = []
for i in range(1,11):
    square.append(i**2)
print(f"by simple way: {square} ")

#by list comprehension
square2 = [i**2 for i in range(1,11)]
print(f"by list comprehension: {square2} ")

print("2nd example")
#simple way
negative = []
for i in range(1,11):
    negative.append(-i)
print(f"by simple way: {negative} ")

#by list comprehension
negative2 = [-i for i in range(1,11)]
print(f"by list comprehension: {negative2} ")

print("3rd example")
#simple way
names = ['Beenash','Pervaiz','Iqbal']
#new_list = ['B','P','I']
new_list= []
for name in names:
    new_list.append(name[0])
print(f"by simple way: {new_list} ")

#by list comprehension
new_list2 = [name[0] for name in names]
print(f"by list comprehension: {new_list2} ")
