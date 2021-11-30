#if_elif_else statement(used for multiple statement)
# Ticket show
# 1 to 3 year(free ticket)
# 4 to 10 year(150 ticket)
# 11 to 60 year(250 ticket)
# above 60 year(200 ticket)

age = input("Enter your age ")
age = int(age)
if age==0 or age < 0:
    print("you can't watch")
elif 0<age<=3:
    print("Ticket Price: free")
elif 3<age<=10:
    print("Ticket Price: 150")
elif 10<age<=60:
    print("Ticket Price: 250")
else:
    print("Ticket Price: 200")    