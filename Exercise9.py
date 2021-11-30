# user enter your name and count the each character of their name how many times came.

Name = input("User enter your name ")
i = 0
while i < len(Name):
    print(f"{Name[i]} : {Name.count(Name[i])}")
    i += 1
    # if we are not want to calculate a character then use a temp variable
    temp_var = ""
while i < len(Name):
      if Name[i] not in temp_var:
          temp_var
          print(f"{Name[i]} : {Name.count(Name[i])}")
          i += 1  