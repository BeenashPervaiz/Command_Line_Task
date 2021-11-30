winning_number = 15
gussed_number = input("Enter your number ")
gussed_number = int(gussed_number)
if winning_number == gussed_number:
    print("your win")
else:
    if winning_number < gussed_number:
        print("gussed number above than winning number ")
    else:
        print("gussed number less than winning number ")