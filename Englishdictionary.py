#program to check word is in a dictonary 
#ishan Hambir

import enchant
dict = enchant.Dict("en_US")
word = input("Enter the word: ")
print(dict.check(word))