#define a function which will take list containing numbers as input and return list containing square of every elements.
#example number_list = [1,2,3,4]
#square_list = [1,4,9,16]

Number_List = list(range(1,11))
print(f"List of the number is: {Number_List}")
def square_list(number):
    square = []
    for i in number:
        square.append(i**2)
    return square
print(f"Square of the list number is:  {square_list(Number_List)}")