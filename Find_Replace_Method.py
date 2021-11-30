#replace() method
#find() method
string = "I am Beenash and I am in 5th Semester"
#replace space with " _ "
print(string.replace(" ","_"))
print(string.replace("am","was",2))
print(string.find("am"))
#print(string.find("is",4))
#position is a number
am_position1 = string.find("am")
am_position2 = string.find("am" , am_position1+1)
print (am_position2)