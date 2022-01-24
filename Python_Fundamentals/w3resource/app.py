#1. Write a Python program to print the following string in a specific format (see the output). 
#Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder #what you are" .

# print("Twinkle, twinkle, little star,\n\tHow I wonder what you are!\n\t\tUp above the world so high,\n\t\tLike a diamond in the sky.\nTwinkle, twinkle, little star,\n\tHow I wonder what you are!")


#2. Write a Python program to get the Python version you are using. 

# import sys
# print(sys.version_info)

#3. Write a Python program to display the current date and time.
# Sample Output : 
# Current date and time : 
# 2014-07-05 14:34:14

# import datetime

# from time import time

# print('Current date and time:')
# time = datetime.datetime.now()
# print(time)


#4. Write a Python program which accepts the radius of a circle from the user and compute the area.
# Sample Output : 
# r = 1.1
# Area = 3.8013271108436504

# from math import pi

# r = float(input('Add radius of circle: '))
# area = (r ** 2 * pi)
# print(f'Radius of circle is:{r} \nArea of circle is:{area}')


#5.  Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.

# name = input('Add your name:')
# surname = input('Add your surname:')
# print(name[::-1],surname[::-1])

#6. Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers. 

# Sample data : 3, 5, 7, 23
# Output : 
# List : ['3', ' 5', ' 7', ' 23'] 
# Tuple : ('3', ' 5', ' 7', ' 23')

# a = input('numbers:')
# print(list(a.split(' ')))
# print(tuple(a.split(' ')))

#7. Write a Python program to accept a filename from the user and print the extension of that.
# Sample filename : abc.java 
# Output : java

# filename = input('Add filename:')
# print(filename.split('.')[1])

#8. Write a Python program to display the first and last colors from the following list.
#color_list = ["Red","Green","White" ,"Black"]

# color_list = ["Red","Green","White" ,"Black"]
# print(color_list[0],color_list[-1])


#9. Write a Python program to display the examination schedule. (extract the date from exam_st_date)
# exam_st_date = (11, 12, 2014)
# Sample Output : The examination will start from : 11 / 12 / 2014

# exam_st_date = (11, 12, 2014)
# print('The examination will start from: %i / %i / %i '%exam_st_date)

#10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. 
# Sample value of n is 5 
# Expected Result : 615

# num = input('add number: ')
# a = int('%s' % num)
# b = int('%s%s' %(num,num))
# c = int('%s%s%s' %(num,num,num))
# print(a + b + c)


#11. Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s). 
# Sample function : abs()
# Expected Result : 
# abs(number) -> number
# Return the absolute value of the argument.

# print(abs.__doc__)
# print(map.__doc__)
# print(sorted.__doc__)


#12. Write a Python program to print the calendar of a given month and year.
#Note : Use 'calendar' module. 

# import calendar

# year = 2022
# month = 2
# print(calendar.month(year,month))