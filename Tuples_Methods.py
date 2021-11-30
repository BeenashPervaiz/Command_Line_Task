#looping in Tuples
#tuple with one element
#tuple unpacking
#list inside tuple
#some function that you can use with tuple

Mixed = (1,2,3,4.0)

#for loop and tuple
for i in Mixed:
    print(i)
#you can use while loop too
#tuple with one element
num1 = (1) #that is the class of integer
num2 = (1,) #that is the class of tuple
words = ('word1',)
print(type(num1))
print(type(num2))
print(type(Mixed))
print(type(words))

#tuple without parenthesis
furit = 'Apple', 'Grapes', 'Mango'
print(type(furit))

#tuple unpacking
furits = ('Apple','Mango','Peach','Orange')
furit1, furit2, furit3,furit4 = furits
#if we have n element inside the tuple than we shoul(d n variables for tuples.
#  if we have n elements in the tuple and variable are n-1 than error is occured.
print(furit1)
print(furit2)
print(furit4)
print(furits)

#lisde inside the tuple
countries = ('USA', 'India',['Pakistan','Panjab'] )
#we can change our list not tuples
countries[2].pop()
countries[2].append('Sindh')
print(countries)

#some function that you can use with tuple
#min(), max(), sum()
print(min(Mixed))
print(max(Mixed))
print(sum(Mixed))