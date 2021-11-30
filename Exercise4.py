#take comma separated input from user(user_name, single character)
User_Name, char = input("Enter the input: ").split(",")
print("User name is "+User_Name)
print("User grade is "+char)

#user' name length
# count the character that user input without space in output give correct answer.
# use the strip methods
print(f"length of the string is {len(User_Name)}" )
#name = User_Name.lower()
#print("total char are "name.count(char))
print(f"total char are :{User_Name.strip().lower().count(char.strip().lower())}" )