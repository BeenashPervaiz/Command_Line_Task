#common element finder function
#define a function which take 2 list as a input and return common elements of both list
#example list1 = [1,2,3,4,5] list2 = [3,2,7,8]
#output: [2,3]

List1 = [1,2,4,7,8,9]
List2 = [2,4,6,0,5]
print(f"Elements of the List1: {List1}")
print(f"Elements of the List2: {List2}")

def common_finder(list1,list2):
    output = []
    for i in list1:
        if i in list2:
            output.append(i)
    return output

print(f"common elements of both list is: {common_finder(List1, List2)}")