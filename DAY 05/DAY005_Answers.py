'''Question 1 :
Write a Python program to find the first 20 non-even prime natural numbers.'''


print('List of Non-even prime numbers are :')

def prime():
    count = 0
    for i in range(2,1000):
        if count <=20:
            for x in range(2,i):
                if (i % x) == 0 :
                    break
            else:

                if (i%2)!=0:
                    print(i, end=",")
                count = count + 1



prime()

#--------------------------------------------------------------------------------------
'''Question 2 :
Write a Python program to implement 15 functions of string.'''

str = 'Hello world'
str1 = 'hi'
print(str.upper())
print(str.lower())
print(str[::-1].upper())
print(str.split(sep=" "))
print(str.title())
print(str.count('l'))
print(str.index('l'))
print(str.join(str1))
print(str.isupper())
print(str.islower())
print(str.find('e'))
print(str.replace('hello','hi'))
print(str.istitle())
print(str.isspace())
print(str.isalpha())





#------------------------------------------------------------------------------

'''Question 3:
Write a Python program to check if the given string is a Palindrome or Anagram or None of them.
Display the message accordingly to the user.'''

choice = int(input(print('please select which option do you want to proceed with : \n','1.Panlindrome \n','2.Anagram \n'+'3. Both')))

def palindrome():
    word1 = input(print('Please enter your  word'))
    word2 = word1[::-1]
    print('reversal of the word is ',word2)
    if word2 == word1:
        print('Its a palindrome')
    else:
        print('Not a Palindrome..')

def anagram():

    word1  = input(print('Please enter your  1st word'))  #abcd
    word2 = input(print('Please enter your  2nd word'))    #daab
    word2 = sorted(word2.replace(' ',''))
    word1 = sorted(word1.replace(' ',''))  #aadb
    if len(word1) == len(word2):
        if word1 != word2:
            print('Not a  Anagram')
        else:
            print('Its a anagram')
    else:
        print('Not a anagram')


def both():
    word1  = input(print('Please enter your  1st word'))  #abcd
    word2 = input(print('Please enter your  2nd word'))    #daab
    option = int(input(print('Please select which word do you wish to check for palindrome \n'+'1. Word1 \n'+'2. Word2')))
    if option == 1:
        word3 = word1[::-1]
        if word3 == word1:
            print('Its a palindrome')
        else:
            print('Not a Palindrome..')
    word2 = sorted(word2.replace(' ',''))
    word1 = sorted(word1.replace(' ',''))  #aadb
    if len(word1) == len(word2):
        if word1 != word2:
               print('Not a  Anagram')
        else:
               print('Its a anagram')
    else:
        print('Not a anagram')


if choice == 1:
    palindrome()
elif choice ==2:
    anagram()
else:
    both()


#---------------------------------------------------------------------------------

'''Question 4:
Write a Python's user defined function that removes all the additional characters from the string
and converts it finally to lower case using built-in lower(). eg: If the string is "Dr. Darshan Ingle
@AI-ML Trainer", then the output be "drdarshaningleaimltrainer".'''

sentence = input(print('please enter a string'))
l = list()
for i in sentence:
    if i.isalnum() == False:
        l.append(i)
for i in sentence:
    for j in l:
        if i ==j:
            sentence=sentence.replace(i,'')

print(sentence)
