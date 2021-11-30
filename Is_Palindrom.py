#def a function of palindrom
word = input("Enter a word or string of numbers: ")
def is_palindrom(word):
    #reversed_word = word[::-1]
    #if word == reversed_word:
    if word == word[::-1]:
        return True
    #else:
    return False
print(is_palindrom(word))
print("Third method")
Word = input("Enter a word or string of numbers: ")
def palindrom(Word):
    return Word == Word[::-1]
print(palindrom(Word))