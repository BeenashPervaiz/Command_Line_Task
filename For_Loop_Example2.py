#for loop example 2
#ask user to enter the more than 1 digit number
#calculate sum of digit

Number = input("Enter the number  ")
sum = 0
for i in range(0,len(Number)):
    sum += int(Number[i]) 
print(f"Sum of the Number {Number}: {sum}")