#define a function which will take list as a argument and this function will return the reversed list
# example [1,2,3,4]
#ouput [4,3,2,1]

List = list(range(1,11))
print("***Simple Method***")
print(f"print the list of the number: {List}")
def reverse_list(l):
    l.reverse()
    return l
print(f"Output of the reversed List:  {reverse_list(List)} "  )

print("***String Slicing Method***")
List1 = ['word1', 'word2', 'word3']
print(f"print the list of the numbers:  {List1}")
def reverse_List1(list):
    return list[::-1]
print(f"output of reversed 2nd list is: {reverse_List1(List1)} ")