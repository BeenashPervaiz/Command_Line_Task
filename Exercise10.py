#for loop example#01
Number = input("Enter any number ")
Number = int(Number)
sum = 0
for i in range(1,Number+1):
    sum += i
print(f"Sum of the Numbers: {sum}")