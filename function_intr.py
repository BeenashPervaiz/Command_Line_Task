#fuction
name = "Beenash"
print(len(name)) #use for calculate the length of string
#how we define function 
#function define for add two numbers

def add_two(a,b):
    return a+b
#print(add_two(5,4))  correct
First_name = input("Enter the first name : ")
Last_name = input("Enter the last name : ")
print(add_two(First_name, Last_name))
num1 = int(input("enter the numbers : "))
num2 = int(input("enter the numbers : "))
total = add_two(num1, num2)
print(f"Sum of the numbers: {total}")