#list comprehension with if statement
numbers = list(range(1,11))
print(f" List of the numbers : {numbers}")
print("  1st example ")
#by simple method
even_num = []
for i in numbers:
    if i % 2 == 0:
        even_num.append(i)
print(f"even number by list simple: {even_num} "  )

#by list comprehension
even_num2 = [i for i in numbers if i%2 == 0 ]
print(f"even number by list comprehension: {even_num2}")
#so simple method
print("very simple method of list comprehension: ")
even_num3 = [i for i in range(11,30) if i%2 == 0]
print(f"even number by list comprehension: {even_num3}")

print("  2nd example ")  
#by simple method
odd_num = []
for i in numbers:
    if i % 2 != 0:
        odd_num.append(i)
print(f"odd number by list simple: {odd_num} "  )

#by list comprehension
odd_num2 = [i for i in numbers if i%2 != 0 ]
print(f"odd number by list comprehension: {odd_num2}")

#so simple method
print("very simple method of list comprehension: ")
odd_num3 = [i for i in range(11,30) if i%2 != 0]
print(f"odd number by list comprehension: {odd_num3}")