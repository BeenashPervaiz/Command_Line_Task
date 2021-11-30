#string slicing 
String = "University"
#syntax variable_name[start argument: stop argumrnt -1]
print(String[4:8])
print(String[-2:7])# not working 
# this statement print the full string if we can't give start and stop argument. 
print(String[:])
#if i cannot write the stop argument then string print from given index to end index.
print(String[4:])
print(String[:5])