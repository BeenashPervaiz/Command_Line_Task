#generate list with range function
#something about pop() method
#index method
#pass list to a function

print("generate list with range function")
number = list(range(1,11))
print(number)

print("pop() method")
popped_item = number.pop() # pop method also return the value that it remove
print("pop method also return the value that it remove")
print(popped_item)
print(number)

list = [1,2,3,4,5,6,7,8,9,10,11,2,5,16,1,2]

print("index method")
#tell the index number
print(list.index(2))#it tell the index number of 2 at the start but we want to know the position of 2 that next of 11 than syntax is that
print(list.index(2,10))
#list.index(number_name_that_find,number_next_from_that,index_number)

print("pass list to a function")
def negative_list(n):
    negative = []
    for i in n:
        negative.append(-i)
    return negative

print(negative_list(number))