#min and max function
#[start:stop:find] that is for range.....

Number = [14,56,60]

print(f"Maxmium number is: {max(Number)}")
print(f"Minmium number is: {min(Number)}")
def greatest_diff(n):
    return max(n) - min(n)
print(f"Greatest difference is: {greatest_diff(Number)}")