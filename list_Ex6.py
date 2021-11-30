#define a function that tell us our list has how many sub list 
#[1,2,3,[1,2],[3,6]]  ---> input
#output: 2 list inside the list
List = [1,2,4,[6,7,],[8,9,0]]
print(f"Print the elements of the list: {List}")
def Sublist_counter(l):
    count = 0
    for i in l:
        if type(i) == list:
            count += 1
    return count
print(f"Total list in a list is: {Sublist_counter(List)}")