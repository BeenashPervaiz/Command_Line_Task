#function practice
print("print the last character of my string: ")
def last_char(name):
    return name[-1]

print(last_char("Beenash")) 
print("function is odd or even: ")
num = int(input("Enter a number: "))
def odd_even(num):
    if num%2 == 0:
        return "Even Number"
    #else:
    return "odd NUmber"
print(odd_even(num))

print("short method for odd or even number")
Num = int(input("Enter a number: "))
def is_even(Num):
    if Num%2 == 0:
        return True
    else:
        return False
print(odd_even(Num))
print("3 very short method for odd or even number")
number = int(input("Enter a number: "))
def is_even(number):
    return number%2 == 0 #true
  
print(is_even(number))

def song():
    return("happy birthday song")
print(song())