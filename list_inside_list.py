#list inside the list
matrix = [[1,2,3],[4,5,6],[7,8,9]]
#3 list inside in list
#print the [1,2,3] list
print(matrix[0])
print("print from 1 to 9 numbers: ")
#for loop
for sublist in matrix:
    for i in sublist: #for loop
        print(i)
print("only sublist of the list: ")
#for loop
for sublist in matrix:
    print(sublist)
#how to access the value of sublist or 2d list
print("i want to print the element '7' ")
print(matrix[2][0])#matrix[row][column]

#type function tell what type of data
string = "string"
print(type(string))
print(type(matrix))