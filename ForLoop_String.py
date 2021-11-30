# print each character of the string
# 1st method
print("1st Method")
name = "University"
for i in range(len(name)):
    print(name[i])
#2nd method
print("2nd Method")
for i in "Beenash": # you can write here string or variable name
    print(i)
# sum of the number 1234 = 1+2+3+4=10
sum = 0
number = input("Enter the more than 2 digit ")
print("Sum of the number ")
for i in number:
    sum += int(i)
print(sum)