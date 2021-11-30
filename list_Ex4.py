#filter odd even
#define a function
#list--->[1,2,3,4,5,6,7]
#output: [[1,3,5,7],[2,4,6]]

List = list(range(1,8))
print(f"print the elements of the list: {List}")
def filter_odd_even(number):
    odd_number =  []
    even_number = []
    for i in number:
        if i % 2 == 0:
            even_number.append(i)
        else:
            odd_number.append(i)
    output = [odd_number, even_number]
    return output

print(f"Separate list of odd and even number is: {filter_odd_even(List)}")