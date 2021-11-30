#define a function that take list of words as a argument and this function will return the reverse of every element in that list
#exapmle: ['abc','tuv','xyz']
#output:  ['cba','vut','zyx']

List = ['abc', 'tuv', 'xyz']
print(f"List is:  {List}")

def reverse_List(list):
    element = []
    for i in list:
        element.append(i[::-1])
    return element
print(f"reverse of each element in list: {reverse_List(List)}")