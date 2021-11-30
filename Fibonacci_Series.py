#fibonacci series
# 0 1 fix number(add the pervious number and get next number)
# 0 1 1 2 3 5 8 13 21 34
# print number 1 ---->0 
#              2 ----> 0 1
#              n ----> 0 1 2 3......
n = int(input("Enter the any number for print Fibonacci series: "))
def Fibonacci_Series(n):
    a = 0 #first number
    b = 1 # second number
    if n == 1:
        print(a)
    elif n == 2:
        print(a,b)
    else:
        print(a, b, end = " ")
        for i in range(n-2):
            c = a + b
            a = b
            b = c
            print(b, end = " ")
Fibonacci_Series(n)