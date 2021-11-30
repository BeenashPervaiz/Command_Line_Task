#take 3 numbers from user and find the greatest number using function
a =  int(input("Enter the integer number: "))
b =  int(input("Enter the integer number: "))
c =  int(input("Enter the integer number: "))

def Greatest_Number(a,b,c):
    if a > b and a > c:
        return "a is greater than b and c "
    elif b > a and b > c:
        return "b is greater than a and c "
    else:
        return "c is greater than a and b "

print(Greatest_Number(a,b,c))
         