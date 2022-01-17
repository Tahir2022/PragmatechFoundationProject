#1. Write a Python program to select the odd items of a list.


# number = [3, 2, 7, 98, 1]

# for i in number:
#     if (i % 2 != 0):
#         print('It is odd number: ', i)


#2. Write a Python function to sum all the numbers in a list.

# def sums():
#     numbers = [3, 5,7,9, 1]
#     sumofnums = sum(numbers)
#     print(sumofnums)

# sums()


#3. Sample List : (8, 2, 3, 0, 7) Expected Output : 20

# my_list = (8, 2, 3, 10)
# print('Output is: ', sum(my_list))


#4. Write a Python function to multiply all the numbers in a list.


# def multiple(num):
#     a = 1
#     for i in num:
#         a = a * i
#     return a

# test = (2, 4, 6, 9, 10)
# print(multiple(test))

#5. Sample List : (8, 2, 3, -1, 7) Expected Output : -336

# def returnDay(a):
#     a = {1:'Sunday', 2:'Monday', 3:'Tuesday', 4:'Wednesday', 5:'Thursday', 6:'Friday', 7:'Saturday'}
#     print(a)

# returnDay(a.get(2))





#7. Make a list of five or more usernames, including the name 'admin' . Imagine you are writing code that will print a greeting to each user after they log in to a website. Loop through the list, and print a greeting to each user: • If the username is 'admin' , print a special greeting, such as Hello admin, would you like to see a status report? • Otherwise, print a generic greeting, such as Hello Eric, thank you for logging in again.


# my_list = ['Elon', 'Max', 'Johannes', 'Julia', 'admin']
# def greetings(any):
#     for i in any:
#         if i == 'admin':
#             print('Hello admin. Would you like to see your status?')
#         else:
#             print(f'Hello {i}, thanks')

# greetings(my_list)





#9. len() funksiyasini ozunuz yazmaga calishin

# def count_word(any):
#     count = 0
#     for i in any:
#         count+=1
#     return count

# example = [2, 5, 8, 7]
# print(count_word(example))

#10. funksiya yazin ededlerden ibaret list qebul etsin ve eger listin birinci ve sonuncu elementleri beraberdise return True qaytarsin. Mes: [1,2,3,1] bu halda True qaytaracag

# def nums(a):
#     for i in a:
#         if a[0] == a[-1]:
#             return True
#         else:
#             return False

# my_list = (2, 9, 5, 2)
# print(nums(my_list))


#11. Funksiya yazin parameter olaraq list,ve dict qebul etsin. Funksiya yoxlamalidi listin icindeki reqemler dictioneryde yoxdusa onlari silmelidi ve sonda listi return etmelidi. (mes : [27,22,34,44],{"tural": 27,"soltan": 22} funksiyaya gonderirsen o sene [27,22] qaytarir.



