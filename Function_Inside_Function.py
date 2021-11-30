a =  int(input("Enter the integer number: "))
b =  int(input("Enter the integer number: "))
c =  int(input("Enter the integer number: "))

def greater(a,b):
    if a > b:
        return a
    return b

def Greatest_Number(a,b,c):
    if a > b and a > c:
        return a 
    elif b > a and b > c:
        return b
    else:
        return c

def new_greatest(a,b,c):
    bigger = greater(a,b)
    return greater(bigger, c)
print("Greatest number is ")
print(new_greatest(a,b,c))