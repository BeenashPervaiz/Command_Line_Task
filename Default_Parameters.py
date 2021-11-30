#default parameters
#you can make default parameter(last_name= 'unknown') in last like after age 
#if we make all parameters defalut than ouput is unknowndef user_info(first_name='unknown', last_name= 'unknown',age = None)
# None is used for numbers
#'unknown' is used for string
def user_info(first_name, last_name,age): #None is a special in python
    print(f"Your First name is: {first_name} ")
    print(f"Your last name is: {last_name} ")
    print(f"Your age is: {age} ")

user_info("Beenash","Pervaiz", 20)