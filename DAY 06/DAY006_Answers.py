
'''Question 1:
Assuming that we have some email addresses in the "username@companyname.com" format, please write program
to print the company name of a given email address. Both user names and company names are composed of letters
only.
Input Format:
The first line of the input contains an email address.
Output Format:
Print the company name in single line.
Example;
Input:
john@google.com
Output:
google'''

database = {}
details = int(input(print('Please enter how many details of users do you wish to save in Database?')))

def store(details):
    for i in range(details):
        username = input(print('Please enter ',i+1,' Username.')).upper()
        email = input(print('Please enter his/her Email ID.'))
        database={username:email}
    name = input(print('Please enter the user name for which you would wish to find the company')).upper()
    for i in database.keys():
        if i != name:
            print('There is no such user in our Database !')
        else:
            getdetails(database,name)
def getdetails(database,name):
    email = database[name]
    splt = email.split('@')
    domain = splt[1]
    lst = domain.split('.')
    company = lst[0]
    prntdetails(name,email,company)
def prntdetails(name,email,company):
    print('Details are as following \n','Name :',name,'\n Email :',email,'\n Company :',company)



store(details)

#---------------------------------------------------------------------------------------------------------

'''Question 2:
Write a program that accepts a comma-separated sequence of words as input and prints the words in a comma
separated sequence after sorting them alphabetically.
Input Format:
The first line of input contains words separated by the comma.
Output Format:
Print the sorted words separated by the comma.
Example:
Input:
without,hello,bag,world
Output:
bag,hello,without,world'''

words = input(print('please enter the words seperated by comma'))

listofwords = words.split(',')
print('List of sorted values is as following : \n')
sortedwords = []
for i in sorted(listofwords):
    sortedwords.append(i)
srt = ''
print(','.join(map(str, sortedwords)))


#---------------------------------------------------------------------------------------
'''Question 3:
Create your own Jupyter Notebook for Sets.
Reference link: https://www.w3schools.com/python/python_sets.asp'''
list1 = [1,2,3,4,1,2,3,4]
list2 = [5,6,7,8,5,6,7,8,9,2]
set1 = set(list1)
set2 = set(list2)
print(set1,set2)
print(set1-set2)
set1.update(set2)
print(set1)
set1.add(10)
print(set1)
set1.remove(10)
set1.pop()
print(set1)






#--------------------------------------------------------------------------------------

'''Question 4:
Given a list of n-1 numbers ranging from 1 to n, your task is to find the missing number. There are no duplicates.
Input Format:
The first line contains n-1 numbers with each number separated by a space.
Output Format:
Print the missing number
Example:
Input:1 2 4 6 3 7 8
Output:5
Explanation:
In the above list of numbers 5 is missing and hence 5 is the input'''


lno =[]
for i in range(5):
    lno.append(int(input(print('please enter numbers'))))
print('you have entered :',lno)

maxno = int(max(lno))
minno =int(min(lno))
final =[]
for i in range(minno,maxno+1):
    final.append(i)
print('Main Set of elements are ',final)
print('missing elements are :' , list((set(final)-set(lno))))







#------------------------------------------------------------------------------------


'''Question 5:
With a given list L, write a program to print this list L after removing all duplicate values with original order reserved.
Example:
If the input list is
12 24 35 24 88 120 155 88 120 155
Then the output should be
12 24 35 88 120 155
Explanation:
Third, seventh and ninth element of the list L has been removed because it was already present.
Input Format:
In one line take the elements of the list L with each element separated by a space.
Output Format:
Print the elements of the modified list in one line with each element separated by a space.
Example:
Input: 12 24 35 24
Output:
12 24 35'''


numbers = [12,24,35,24,88,120,155,88,120,155]
final = []
for i in numbers:
    if i not in final:
        final.append(i)
print(final)