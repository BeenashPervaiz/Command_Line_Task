list = ['abc','uvw', 'xyz']
print(f"input is: {list}")

#By simple Method
element = []
def reverse_list(l):
    for i in list:
        element.append(i[::-1])
    return element
print(f"By simple Method: {reverse_list(list)}")

#By comprehension Method
new_element = [i[::-1] for i in list]
print(f"By comprehension Method: {new_element}")