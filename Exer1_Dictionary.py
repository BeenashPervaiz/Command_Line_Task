#make a function
#that give the cube of give numbers
num = int(input("Enter the nnumber for cube: "))
def cube_finder(n):
    cube = {}
    for i in range(1,n+1):
        cube[i] = i**3
    return cube
print(cube_finder(num))