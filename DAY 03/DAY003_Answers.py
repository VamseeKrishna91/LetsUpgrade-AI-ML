"""Question 1 :
Write a program to subtract two complex numbers in Python."""
a = 5+6j
b = 7-4j
print('Type of element a is ',type(a),'while type of element b is ',type(b))
print('result of subtraction is ',(a-b))


#------------------------------------------------------------------

'''Question 2 :
Write a program to find the fourth root of a number'''
a = 16
print('Fourth root of a is ',(a)**(1/4))


#------------------------------------------------------------------


'''Question 3:
Write a program to swap two numbers in Python with the help of a temporary variable.
'''
a = 1
b = 2
print('a is ',a,'b is ',b)
c=a
a=b
b=c
print('Now a is',a,'b is ',b)


#------------------------------------------------------------------

'''Question 4:
Write a program to swap two numbers in Python without using a temporary variable.'''
a = 5
b = 8
print('Value of a is ',a,'Value of b is',b)
a = a+b
b = a-b
a = a-b
print('Now Value of a is ',a,'Value of b is',b)



#------------------------------------------------------------------

'''Question 5:
Write a program to convert fahrenheit to kelvin and celsius both.'''

Temp = 68
print('Temperature in Celsius is ' ,((Temp-32)/(1.8)),'Degree Celcius')
print('Temperature in Kelvin is',((Temp+459.67)*(5/9)))

#-----------------------------------------------------------------

'''Question 6:
Write a program to demonstrate all the available data types in Python. Hint: Use type() function.'''
a=1
b=1.0
c='Hello'
d=5+5j
print('Different Data types are : \n')
print(type(a))
print(type(b))
print(type(c))
print(type(d))


#----------------------------------------------------------------

'''Question 7:
Create a Markdown cell in jupyter and list the steps discussed in the session by Dr. Darshan
Ingle sir to create Github profile and upload Githubs Assignment link.
1. Navigate to https://github.com/
2. Click on "Sign In" if you already have an account .Else user needs to Sign Up first
3. Create a New Repository by clicking on 'New' button.
4. Enter the repository name as LetsUpgrade AI/ML
5. Click on Create Repository
6. Click on Upload an existing file
7. Drop the day wise assignment folder which contains python file
8. Click on Commit Changes
9. Copy the URL
10. Fill the google form provided by LetsUpgrade with the copied URL
11. Submit the form'''

