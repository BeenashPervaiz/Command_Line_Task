#Break and Continue keyword
# 1 to 10 print
# output: 1,2,3,4 
print("Break Keyword")
for i in range(1,11):
    if i == 5:
        break  #when i equal to 5 then loop jump on print/next statement not for loop/pervious statement
    print(i)
#continue
#output: 1,2,3,4,6,7,8,9,10
print("Continue Keyword")
for i in range(1,11):
    if i == 5: 
        continue # when i equal to 5 then loop jump to loop/pervious statement not print/next statement
    print(i)
