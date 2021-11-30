#scope 
x = 5 #global variable
def func():
    global x
    x = 7  #local variable
    return x

print(x)
print(func())
print(x)
#not right x is the variable of func() not func2().
#def func2():
#    print(x)