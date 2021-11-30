#number to the string
#define a function
#input----> [True,False,[1,2,3],1,3,5,3.4]
#output---> [1,3,5,3.4]

list = [True,False,[1,2,3],1,3,5,3.4]

def num_to_string(l):
    return [str(i) for i in l if type(i) == int or type(i) == float] 

print(f"from list convert the integer and float into string and print on the screen: {num_to_string(list)}")