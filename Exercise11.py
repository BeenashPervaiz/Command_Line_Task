# define a function and calculate that who number is greatest than other.
a = int(input("Enter the a vlaue "))
b = int(input("Enter the b vlaue "))
def greater_number(a,b):
    if a < b:
        return "b is greater number "
    return  "a is greater number "

print(greater_number(a,b))