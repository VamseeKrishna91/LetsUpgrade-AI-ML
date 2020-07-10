'''Question 1 :
Research on whether addition, subtraction, multiplication, division, floor division and modulo
operations be performed on complex numbers. Based on your study, implement a Python
program to demonstrate these operations.'''
a= 2+3j
b = 5-2j
print('Addition of 2 complex numbers is ' ,(a+b))
print('Subtraction of 2 complex numbers is ',(a-b))
print('Multiplication of 2 complex numbers is ',(a*b))
print('Division of 2 complex numbers is ',(a/b))



#-----------------------------------------------------------------------------------------
'''Question 2 :
Research on range() functions and its parameters. Create a markdown cell and write in your own
words (no copy-paste from google please) what you understand about it. Implement a small
program of your choice on the same.'''

'''Answer:
Range is a function which generates series of integer numbers from a start point to a end point.
User can also decide step over size . For eg :'''

x = range(2,10,2)
for i in x :
    print(i)

#------------------------------------------------------------------------------------------

'''Question 3:
 Consider two numbers. Perform their subtraction and if the result of subtraction is greater than
25, print their multiplication result else print their division result.'''
a=28
b = 4
if (a-b) >25:
    print('Multiplication of the numbers is ',(a*b))
else:
    print('Division of numbers is ',int(a/b))

#------------------------------------------------------------------------------------------

'''Question 4:
Consider a list of 10 elements of integer values. If the number in the list is divisible by 2, print the
result as "square of that number minus 2".'''
l = [1,2,3,4,5,6,7,8,9,10]

for i in l:
    if (i%2) ==0:
        print((i**2)-2)


#----------------------------------------------------------------------------------------

'''Question 5:
Consider a list of 10 elements. Print all the elements in the list which are greater than 7 when that
number is divided 2.'''

l = [10,11,12,13,14,15,16,17,18,19,20]

for i in l:
    if (i/2)>7:
        print(i)



