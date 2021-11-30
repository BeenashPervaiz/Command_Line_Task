# word counter dictionary
#Beenash
#dic = {'a':1,'h'=1}
#temp = " "
#in dictionary two keys are not same
#dic = {'h ':1, 'a':1,'h':2}#in dictionary order is not same in output that is not 
#print(dic)
string = input("Enter the your string: ")
def word_counter(s):
    count = {}
    for i in s:
        count[i] = s.count(i)
    return count
print(word_counter(string))
