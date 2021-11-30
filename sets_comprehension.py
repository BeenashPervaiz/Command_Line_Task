#sets comprehension
#that is not use 

print("stes always give the output in unordered ways")
print("1st Example of sets comprehension")
sets = {key**2 for key in range(1,11)}
print(f"square of numbers: {sets}")

print("2nd Example of sets comprehension")
names = ['Beenash','Pervaiz','Iqbal']
first_letter = {name[0] for name in names}
print(f"print the first letter of the name: {first_letter}")