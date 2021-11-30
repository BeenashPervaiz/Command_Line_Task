#list comrehension with if else
numbers = list(range(1,11))
print(f"Number in the list is:  {numbers}")
#if number is odd than multiple with minu and if number is odd than multiple with 2
#new_list = [-1,4,-3,8,.....]

#by simple method
new_list = []
for i in numbers:
    if i%2 == 0:
        new_list.append(i*2)
    else:
        new_list.append(-i)
print(f"Output of the list is: {new_list}")
#by list comrehension method
new_list2 = [i*2 if( i%2 == 0) else -i for i in numbers]
print(f"Output of the list is: {new_list2}")
