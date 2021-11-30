# for loop example3
# ask user their name and count each character of their name
Name = input("Enter your name ")
temp_var = ""
for i in range(len(Name)):
    if Name[i] not in temp_var:
        print(f"{Name[i]}: {Name.count(Name[i])}")
        temp_var += Name[i]
