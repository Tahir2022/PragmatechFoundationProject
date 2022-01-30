# 1. Bir mesajı dəyişəndə saxlayın və sonra mesajı çapa verin

#txt = 'Today is Pi day'
#print(txt)

#2. ad və soyad dəyişkənləri yaradın və onlara istədiyiniz kiçik hərflərdən ibarət dəyər verin. Sonra tam_ad adlı dəyərdə ad və soyadın ilk hərflərini böyük şəkildə çapa verərək həmin şəxsə Salam verin.
#Nümunə: Salam, Arif Dadaşov! (Ekrana bu yazı çıxsın)

#ad = 'elon'
#soyad = 'musk'
#tam_ad = f"Salam, {ad.capitalize()} {soyad.capitalize()}!"

#print(tam_ad)

#3. sep parametrindən istifadə edərək 4 müxtəlif şəhər adını * işarəsi ilə ayırın

#print('Baku', 'Moscow', 'Istanbul', 'Berlin', sep='*')

#4. “Macarıstan” sözünü tərsinə çapa verin

#country = 'Macarıstan'[::-1]

#print(country)


#5. Bir sətir koddan istifadə edərək aşağıdakı yazını göründüyü kimi çapa verin. Languages: Python C JavaScript

#print('Python', 'C', 'Javascript', sep='\n')

#6.Istenilen bir mətnin tam yarısını çap edin

#txt = 'I will try print a half of this text'

#print(txt[0:18])


#7. x = 10, y = 55 “and”-dən istifadə edərək x və y müqayisə edərək boolen dəyərləri çapa verin.

#x = 10
#y = 55

#print(x < y and y > x)


#8. inputdan boshluqla ayrilmish iki eded daxil edin. Birinci ededi ikinci eded qeder quvvete yukseldin ve ashagidaki kimi ekrana yazdirin (f stringden istifade ederek)

#Ededleri daxil edin: 2 5

#Netice: 2 üstü 5 32-dir.

#import math

#a = input('Ededleri daxil edin: ')
#b = a.split('ustu')
#result = int(b[0] ) **int(b[1])

#txt = f'Netice: {b[0]} ustu {b[1]} beraberdir -  {result}'
#print(txt)

# 10. 65 ədədinin 22 ədədinə olan qalığı ilə nisbətinin hasilini çapa verin.

#first_num = 65
#second_num = 22
#rem =first_num % second_num
#div = first_num / second_num
#print(rem * div)

#11. x-ə istənilən bir ədəd mənimsədin, sonra isə şərt verərək yoxlayın. X 10-dan böyükdürsə və cüt ədədirsə, ekrana “OKAY” yazılsın, əgər yuxarıdakı iki şərtdən biri ödənirsə “NOT OKAY” yazılsın, heç bir şərt ödənməzsə, “BAD” yazılsın

#x = 2
#if (x > 10) and (x % 2==0):
#    print('OKAY')
#elif (x > 10) or (x % 2 !=0):
#    print('NOT OKAY')
#else:
#    print('BAD') 


#12. iki ədəd götürüb dəyişkənlərə mənimsədin. Əgər ədələrin fərqi bir-birlərinə olan nisbətin tam hissəsindən böyükdürsə, ekrana “Greater”, bərabərdirsə, “EQUAL” yox əgər kiçikdirsə, “SMALLER” yazılsın.

# num1 = 100
# num2= 10
# subs = num1 - num2
# div = int(float(num1 / num2))

# if (subs > div):
#     print('GREATER')
# elif (subs == div):
#     print('EQUAL')
# elif (subs < div):
#     print('SMALLER')

#13. String data tipi yaradın və dəyərini 5.567-yə bərabər edin. Sonra bu dəyişkənin dəyərin 10- luqlara qədər yuvarlaqlaşdırın.

# import math

# string = '5.567'
# convert_str = float(string)
# convert_str = round(convert_str, 1)

# print(convert_str)

#14. my_string = ‘f4.3989ts’. my_stringin ədədə bərabər olan hissəsin ilə özündən sonra gələn ən kiçik tam ədədə olan qüvvətini tapın

#my_string = 'f4.3989ts'
#b = float(my_string[1:7])
#a = int(b) + 1
#print(b **a)


#17. x = “5.89” stringinin tam hissəsinin kubunu tapın.

# import math

# x = '12.63'
# y = int(float(x))
# print(pow(y, 3))


#18. y = “4.92” stringini integere cast edin.

#y = '4.92'
#x = int('4.92')

#print(x)


#HackerRank 30/01

#1.Task
# Given an integer, n, perform the following conditional actions:

# If n is odd, print Weird
# If n is even and in the inclusive range of  to , print Not Weird
# If n is even and in the inclusive range of  to , print Weird
# If n is even and greater than , print Not Weird
# Input Format

# A single line containing a positive integer, .

# Constraints

# Output Format

# Print Weird if the number is weird. Otherwise, print Not Weird.


# import math
# import os
# import random
# import re
# import sys


# if __name__ == '__main__':
#     n = int(input().strip())
# if n % 2 == 1: print('Weird')
# else:
#     if 2 <= n <= 5: print('Not Weird')
#     elif n <= 20: print('Weird')
#     else: print('Not Weird')


#2.Task
# The provided code stub reads two integers, a and b, from STDIN.
# Add logic to print two lines. The first line should contain the result of integer division,  a//b. The second line should contain the result of float division,  a/b.
# No rounding or formatting is necessary.
#Example
#a = 3
#b = 5
#The result of the integer division 3//5 =0.
#The result of the float division is 3/5 =0.6.

# if __name__ == '__main__':
#     a = int(input())
#     b = int(input())
#     print(a//b)
#     print(a/b)


#3.Task
#The provided code stub reads and integer, n, from STDIN. For all non-negative integers i<n, print i**2.

# n = int(input())
# for i in range(n):    print(i ** 2)


#4.Task


# def check_leap(year):
#     if (year % 4 ==0) and (year % 100 !=0) or (year % 400 ==0):print('Leap year')
#     else: print('Not leap year')

# year = int(input('Add year:'))
# check_leap(year)

# def check_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0: return True
#         else: return True
#     return False

# year = int(input)
# print(check_leap(year))

# def check_leap(year):
#     if year % 4: return False
#     if not year % 100:
#         if not year % 400: return True
#         else: return False
#     return True
# year = int(input())
# print(check_leap(year))

#5.123...5

# n = int(input())
# for i in range(1,n+1): print(i,end ="")


#6.# Task find string
# You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.
# Function Description
# Complete the split_and_join function in the editor below.
# split_and_join has the following parameters:
# string line: a string of space-separated words
# Returns
# string: the resulting string
# Input Format
# The one line contains a string consisting of space separated words.

# sentence = input('Add any sectence:')#first one
# sentence = sentence.split(" ")
# sentence = "-".join(sentence)
# print(sentence)

# def str_method(str): #second one
#     return "-".join(str.split())

# str = input("Add ant sentence: ")
# print(str_method(str))