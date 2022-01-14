#1. Listin elementlerini toplayan alqoritm yazin. Sum funksiyasindan istifade etmeyin.

# my_list = [1, 5, 100, 78]
# total = 0
# for i in my_list:
#     total+=i
# print(total)

# x=[1,2,3,4,5]
# sum=0
# for s in range(0,len(x)):
#    sum=sum+x[s]
# print(sum)

#2. Listin en boyuk elementini max funksiyasini istifade etmededen tapan alqoritm yazin.

# my_list = [5, 6, 9, 10]
# maximum = my_list[0]
# for i in my_list:
#     if i > maximum:
#         maximum = i
# print(maximum)


#3. Listin en kicik elementini min funksiyasini istifade etmededen tapan alqoritm yazin.

# my_list = [5,7,69,74,3]
# minimum = my_list[0]
# for i in my_list:
#     if i < minimum:
#         minimum = i
# print(minimum)


#4. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. Sample List : ['abc', 'xyz', 'aba', '1221'] Expected Result : 2



# my_list = ['abc', 'xyz', 'aba', '1221']

# for i in my_list:
#     if (len(i) > 2) and i[0] ==i[-1]:
#         print(i)


# 5. Write a Python program to check a list is empty or not.

# my_list = [ ]
# if len(my_list) == 0:
#     print('It is empty!')

#6. my_text = “Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.” my_text stringindeki sozler elifba sirasi ile duzub string formatinda ekrana yazdirin.

import string

my_text = '''Write a Python program to count the number of strings where the string length is 2 or more  and the first and last character are same from a given list of strings.'''
say = 0
new_txt = my_text.split(' ')
for i in new_txt:
    if (len(i) > 2) and i[0] == i[-1]:
        print(i)
        print(my_text.ascii_lowercase)



#7. Write a Python program to select the odd items of a list


# my_list = [2, 5, 8, 9, 99, 11]
# for i in my_list:
#     if (i % 2!=0):
#         print('Odds are: ', i)
