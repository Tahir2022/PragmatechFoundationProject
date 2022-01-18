#1. Write a program to create a function show_employee() using the following conditions.
# It should accept the employee’s name and salary and display both. If the salary is missing in the function call then assign default value 9000 to salary

# expected result: showEmployee("Ben", 12000) showEmployee("Jessa") Name: Ben salary: 12000 Name: Jessa salary: 9000

# def show_employee(name, salary = 9000):
#     print(f'Name: {name} Salary: {salary}')

# show_employee('Ben', 12000)
# show_employee('Tahir')

#2. 'test' adinda function yaradin, funksiyaya parametrleri key value shekline gonderin istenilen sayda, funksiya gonderilen ededlerden cut olanlarin sayini tapsin
#expected result: test(a=4, b=1, c=2) result=2

# import math
# def test(a):
#     for i in a.values():
#         if i % 2 ==0:
#             print(i)


# r = {'a':1, 'b':2, 'c':3, 'd':6, 'e':9, 'g':10}
# test(r)


#3. math.ceil funksiyasini ozunuz yazin

# import math
# def my_ceil(x):
#     a = int(x)
#     if a == x:
#         return float(a)
#     else:
#         return float(a + 1)

# print(my_ceil(5))

#4. stringlerin index metodunu ozunuz yazin


# def my_index(x, str1):
#     s = len(str1)
#     for i in range(s):
#         if str1[i] == x: return i 
#         else: return - 1
            

# str1 = "salam"
# print(my_index('a', str1))



#5. Natural ədədin onluq yazılışında rəqəmləri eyni olan və bu ədədin onluq yazılışının mərkəzinə nəzərən simmetrik yerləşən cütlüklərin sayını həmin ədədin simmetriya dərəcəsi adlandıracağıq. Əgər ədəddə hər hansı rəqəm onluq yazılışda ortada yerləşirsə, onu da özü ilə bir cütlük kimi saymaq lazımdır. n ədədinin simmetriya dərəcəsini tapın.

# def simmetric(x):
#     s = 0
#     ls = len(x) - 1
#     mid = ls // 2
#     for i in range(mid, -1, -1):
#         if x[i] == x[ls - i]:
#             s+=1
#         return s

# x = input()
# print(simmetric(x))

#6. ni 1 olan və hər iki tərəfə sonsuz uzanan zolaq 1x1 ölçülü damalara bölünmüşdür. Bu damaların birində dayanan robot (şəkildə həmin robot kvadratla işarə edilmişdir) bir damadan digərinə hərəkət edə bilər.

# Robotun yerdəyişməsi hər bir əmri latın əlifbasının 3 böyük hərfinə - L, R, S hərflərinə uyğun proqramla müəyyənləşir. L əmri icra edildikdə robot bir dama sola, R əmrində bir dama sağa hərəkət edir, S əmrində isə olduğu damada qalır.

# Proqramın icrası dedikdə orda yazılan bütün əmrlərin ardıcıl yerinə yetirilməsi başa düşülür.

# def cubic(s):
#     x = 0
#     min = 0
#     max = 0
#     for i in s:
#         if i == 'R':
#             x+=1
#         elif i == 'L':
#             x-=1
#         if x < min: min = x
#         if x > max: max = x
#     return max-min + 1

# s = input()
# print(cubic(s))