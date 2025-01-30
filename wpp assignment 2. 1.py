# Write a program that asks the user to enter a word and then capitalizes every other letter of 
# that word. So, if the user enters rhinoceros, the program should print rHiNoCeRoS.

word = input("enter a word : ")
word =list(word)
for i in range(1,len(word),2):
    word[i]=word[i].upper()
    
print(word)
word = ''.join(word)       # directly convert list into string
print(word)



