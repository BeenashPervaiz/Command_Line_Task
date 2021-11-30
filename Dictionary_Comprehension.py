#dictionary comprehension
#as like list but we also give key value
#example square = {1:1,2:4,3:9}
print("1st Example of Dictionary Comprehension ")
square = {f"square of {num} " :num**2 for num in range(1,11)}
for i,j in square.items():
    print(f"{i} : {j}")

print("2nd Example of Dictionary Comprehension ")
string = "Beenash"
word_count = {char:string.count(char) for char in string}
print(word_count)
