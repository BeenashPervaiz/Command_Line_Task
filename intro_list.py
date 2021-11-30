#list ----> we store int,float,string..
#ordered collection of item --->DAta structure
numbers = [1, 2, 3, 4, 5]
print(numbers)
print(numbers[2])#we can also access by indexing

words = ["Beenash", 'Pervaiz', "Hanan"]
print(words)
print(words[:2]) # by slicing

mixed = [1, 2, 3, 4, "five", "six",2.5, None]
print(mixed)
print(mixed[-1])# negative indexing

#change the data of the list
mixed[1] = 'two'
print(mixed)
#if we change the almost total data of list
numbers[:5] = ['one', 'two','three','four','five']
print(numbers)