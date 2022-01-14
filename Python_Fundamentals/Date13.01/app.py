#1. Kvadrat yaratmaq olarsa daxil edilən 4 ədəddən, ekrana kvadratın sahəsini, olmazsa, həmin ədədlərin cəmini verin.

# import math

# def square ():
#     a = int(input('Add pls first number: '))
#     b = int(input('Add pls second number: '))
#     c = int(input('Add pls thrid number: '))
#     d = int(input('Add pls fourth number: '))

#     if (a == b == c == d):
#         print(pow(a, 2))
#     else:
#         print(a + b + c + d)

# square()


#2. Dörd ədəd daxil edin. Onlardan ən böyüyünü çapa verin.

# def check_max():
#     num1 = input('Add pls first number: ')
#     num2 = input('Add pls second number: ')
#     num3 = input('Add pls thrid number: ')
#     num4 = input('Add pls fourth number: ')

#     if (num1 > num2) and (num1 > num3) and (num1 > num4):
#         print(num1)
#     elif (num2 > num1) and (num2 > num3) and (num2 > num4):
#         print(num2)
#     elif (num3> num1) and (num3 > num2) and (num3 > num4):
#         print(num3)
#     elif (num4 > num1) and (num4 > num2) and (num4 > num3):
#         print(num4)
# check_max()

#3. Proqram run olunanda, istifadəçiyə meyvələr menyusu təqdim olunsun. Userdən menyunuzdakı meyvələrdən birinin adını daxil etməsini tələb edin və ekrana meyvənin qiymətini yazdırın. (İstədiyiniz qiyməti yazdırın). Əgər menyuda olmayan meyvə daxil edilsə, ekrana error mesajı verin.

# def find_fruits ():
#     fruits = ['apple', 'cherry', 'watermelon', 'orange']
#     print(fruits)

#     a = input('Write any fruit: ')
#     if a in fruits:
#         print(input(f'{a} nin qiymetini yazin: '))
#     elif a not in fruits:
#         print('ERROR')

# find_fruits()


#4. Qeydiyyat formu düzəldin. İstifadəçi adını daxil etsin. Adın uzunlu 3-dən kiçik 11-dən böyük ola bilməz.Əgər adını düzgün daxil edərsə, soyadının daxil etməsini istəyin. Soyad 5 hərfdən kiçik, 15 hərfdən uzun olmasın. Əgər soyad düzgün daxil edilsə, Daha sonra doğulduğu ili daxil etsin. Doğum ilinin uzunluğu 4 simvoldan ibarət olmalıdır. Sonra email daxil etməsini tələb edin. Emailin uzunluğu 10 hərifdən qısa 22 hərfdən uzzun olmasın, tərkibində @gmail.com olsun və bu hissə daxil etdiyi emailin sonunda olsun. Ardınca parol axil etsin. Parol 6-13 simvol aralığında olmalıdır. Sonra parolu təsdiqləməyini tələb edin. Təsdiqlədiyi parol birinci yazdığı parol ilə eyni olmalıdır. Bütün bunlar düzgün daxil edilərsə, Qeydiyyat tamamlandı mesajı verilsin və istifadəçidən qeydiyyatın detallarına baxmaq istəyib-istəməməsi soruşulsun. Əgər hə desə, aşağıdakı görüntü çapa verilsin: (Qeyd: Yuxarıda sizin verdiyiniz şərtlərə uyğun istifadəçi input daxil etmsəsə, hər verdiyibiz şərtə uyğun error tipli mesaj verin. Məsələn doğum ilini 5 simvoldan ibarət daxil etsə, mesaj verilsin ki 4 simvol daxil edin. Yəni hər şərti müvafiq mesajlar ilə userə izah edin. ============================================= Ad: Murad Soyad: Əliyev Yaş: 22 Email: muradaliyev1996@gmail.com Parol: 123456789 ============================================= Əgər yox desə, Murad Əliyev, Uğurlar! Yazılsın.



from os import name


def login ():
    name = input('Pls add your name: ')
    if 3 < len(name) < 11:
        surname = input('Pls add your surname: ')
        if 5 < len(surname) < 15:
            year = input('')

    
  












