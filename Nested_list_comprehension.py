#list comprehension in Nested if else
#example
#Numbers = [[1,2,3],[1,2,3],[1,2,3]]
#by list comprehension
Nested_compre = [[i for i in range(1,6)]for j in range(3)]
print(f"print the list with nested list: {Nested_compre}")

#by simple method
new_list = []
for j in range(3):
    new_list.append([i for i in range(1,6)])
print(f"print the list with nested list: {new_list}")