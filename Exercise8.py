#ask user to input a number containing more digits
# calculate the sum of the digit and print there sum

Number = input("Enter the more than 4 digit into and not change into integer ")
i = 0
sum = 0
while i < len(Number):
    sum = sum +  int(Number[i])
    i = i + 1
print("Sum of the numbers")
print(sum)