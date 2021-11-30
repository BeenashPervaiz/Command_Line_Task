#dictionary comprehension with if else

#dic = {1:'odd',2:'even',3:'odd',...}

odd_even = {i:('even' if i%2==0 else 'odd')for i in range(1,11)}
print(f"odd and even values dictionary: {odd_even}")