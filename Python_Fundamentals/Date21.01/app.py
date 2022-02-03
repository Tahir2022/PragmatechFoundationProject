#1. Bir dənə Restoran classı yaradın. Bu classa init() metdou bu classın adını (restaurant_name) və mətbəx növü (cuisine_type) adlı iki atribitunu saxlamalıdır. describe_restaurant() adlı bir metod yaradın hansı ki restoranın adını və mətbəxin növünü ekrana print etsin. Restoranın açıq olmasını mesaj verən open_restaurant() adlı başqa bit metdi yaradın. Sonra restoran adlı obyekt yaradın bu class-dan və restotanın adını, mətbəxinin növünü, restoran haqqında məlumatları və açıq olmasını çapa verin. Bu Restoran classından daha iki obyek yaradın və describe_restaurant metodunu yeni yaratdığınız hər iki obyekt üçün tətbiq edin.

# class Restoran:
#     def __init__(self, restaurant_name, cuisine_type): 
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type

#     def describe_restaurant(self):
#         print(f'Restoran adi: {self.restaurant_name} \nMenu novu: {self.cuisine_type}')

#     def open_restaurant(self):
#         print('Restoran açıqdır!')
        

# restoran1 = Restoran('Domino’s Pizza','Pizza')
# restoran1.describe_restaurant()
# restoran1.open_restaurant()

# restoran2 = Restoran('McDonald’s','Fast Food')
# restoran2.describe_restaurant()
# restoran2.open_restaurant()

# restoran3= Restoran('KFC', 'Fast Food')
# restoran3.describe_restaurant()
# restoran3.open_restaurant()


#2. User adlı yeni class yaradın. first_name, last_name və age atributları verin bu class-a. describe_user metdou yaradın user haqqında məlumatları çapa vermək üçün. greet_user adlı başqa bir metod yaradın hansı ki userin ad və soyadına salam verən bir mesaj ekrana yazdırsın. Bir neçə obyekt yaradın bu User class-ndan və hər birinin atribut və metodlarını istifadə edin. Ardinca login_attempts adlı bir atribut verin User classına. increment_ login_attempts adlı metod yaradın hansı ki hər dəfə işə düşəndə login_attempts 1 vahid artırır. reset_login_attempts adlı bir metod yaradın hansı ki login_attemptsləri sıfırlayır. Sonra bir user obyekti yaradın bu class-dan və increment_ login_attemptsi bir neçə dəfə istifadə etdikdən sonra userin neçə dəfə cəhd etdiyini çapa verin. Daha sonra cəhdlərin sayını sıfırlayın və yenidən cəhdlərin sayını çapa verin


# class User:
#     def __init__(self, first_name, last_name, age, login_attempts = 0):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.count = login_attempts

    
#     def describe_user(self):
#         print(f'First name: {self.first_name} \nLast name: {self.last_name} \nAge: {self.age}')

    
#     def greet_user(self):
#         print(f'Hello {self.first_name} {self.last_name}')


#     def increment_login_attempts(self):
#         self.count+=1
#         print(self.count)
        
        


# admin = User('Tahir','Abbasov',24)
# # admin.describe_user()
# # admin.greet_user()
# admin.increment_login_attempts()

# # admin1 = User('Elon','Musk',51)
# # admin1.describe_user()
# # admin1.greet_user()


# Tələblər
# addToTuple metodunun vəzifəsi tpl strukturunun içinə yeni bir element əlavə edilə bilməsini təmin etməkdir.Metod icra olunduğu zaman nəticə olaraq yeni element əlavə edilmiş formada ekranda çap olunmalıdır.


# tpl=(23,45,12,67)

# def addToTuple(element):
#     l = list(tpl)
#     l.append(element)
#     t = tuple(l)
#     print(t)
    
# addToTuple(535)

# import os
# from os import path

# def main():
#     if path.exists('tural.txt'):
#         src = path.realpath('tural.txt')
#     os.rename('tural.txt', 'sahib.txt')

# main()

# import os
# from os import rename
# path = input()
# old_name = input()
# new_name = input()
# old_name = path + '/' + old_name
# new_name = path + '/' + new_name
# rename(old_name, new_name)


# from re import I
# from countries import olkeler

# def FindCity(cityname):
#   # seher adi daxil edildiyi zaman o seherin aid olduğu ölkəni göstərsin
#   for i in olkeler:
#       if cityname in olkeler.get(i):
#           print(i)

      
# def FindCountry(countryname):
#   # olke adi daxil edildiyi zaman o olkeye aid olan seherlerin adlarini ekranda gostersin
#   print("\n".join(olkeler.get(countryname)))


# def CityCountMax():
#   # ek cox sehere sahib olan olkeni gostersin
#     say=0
#     for i in olkeler:
#         if len(olkeler.get(i))>say:
#             more_city=i
#             say=len(olkeler.get(i))
#     print(more_city)


# def CountAllCities():
#   # butun seherlerin sayini ekranda gostersin
#     say=0
#     for i in olkeler:
#         say+=len(olkeler.get(i))
#     print(say)

# # FindCity("Shar")
# # FindCountry("Afghanistan")
# CityCountMax()
# CountAllCities()

'''
1.	Qeydiyyatdan keçmək üçün [1] yazın
- İstifadəçi adınız :
- Parolunuz :
2.	Sistemə daxil olmaq üçün [2] yazın
3.	Ana menyuya qayıtmaq üçün [3] yazın
4.	Sistemdən çıxmaq üçün [4] yazın
- Sərtlər
Class və obyektlərdən istifadə olunaraq yazılmalıdır.
- İstifadəçi daxil olduğu zaman daha öncədən qeydiyyatdan keçib keçmədiyini yoxlamalısınız.
Parol daxil edildikdən sonra parol şirfrələnmiş şəkildə sistemə düşməlidir.Bunun üçün python encript araşdırması edə bilərsiniz. Ana menuye qayitmaq yuxarıdakı menyunun görünməsi, proqramdan çıx isə ümümən proqramın dayanması mənasına gəlir 
'''


# class User:
#   __login = ''
#   __passwd = ''
#   __logged = False
  
#   def _init_(self, login, passwd):
#     self.__login = login
#     self.__passwd = hash(passwd)
  
#   def SignUp(self):
#     # save login and password to database
#     print(self.__login)
#     print(self.__passwd)
  
#   def LogIn(self):
#     # get login and password from database
#     login = 'root'
#     passwd = hash('root')
#     if self._login == login and self._passwd == passwd:
#       self.__logged = True
#       print('User is logged')
  
#   def LogOut(self):
#     self.__login = ''
#     self.__passwd = ''
#     self.__logged = False
#     print('User is logout')
  
#   def isLogged(self):
#     return self.__logged

# menu = """1. Qeydiyyatdan keçmək üçün [1] yazın
# 2. Sistemə daxil olmaq üçün [2] yazın
# 3. Ana menyuya qayıtmaq üçün [3] yazın
# 4. Sistemdən çıxmaq üçün [4] yazın
# 5. Proqramdan çıxmaq üçün [5] yazın
# """
# user = None

# while(True):
#   print(menu)
#   k = int(input())
  
#   if k == 1 or k == 2:
#     print('- İstifadəçi adınız: ', end='')
#     login = input()
#     print('- Parolunuz: ', end='')
#     passwd = hash(input())
#     user = User(login, passwd)
  
#   if k == 1:
#     if user: user.SignUp()
#   elif k == 2:
#     if user and not user.isLogged(): user.LogIn()
#   elif k == 3:
#     continue
#   elif k == 4:
#     if user: user.LogOut()
#   elif k == 5:
#     break
#   else: print('Naməlum seçim')
#   print()