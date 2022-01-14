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



from datetime import date

def login ():
    todays_date = date.today()
    email = '@gmail.com'
    divide = email.split('@')
    name = input('Please add your name: ')
    if (len(name) > 3) and (len(name) < 11):
        surname = input('Please add your surname: ')
        if (len(surname) > 5) and (len(surname) < 15):
            year = input('Please add your birth year: ')
            if len(year) == 4:
                old = int(todays_date.year - int(year))
                print('You are ', old, 'years old')
                mail = input('Add your mail adress: ')
                if (len(mail) > 10) and (len(mail) < 22) and email in mail and divide[1] == 'gmail.com':
                    password = input('Define any password: ')
                    if (len(password) > 6) and (len(password) < 13):
                        submit_password = input('Submit your password: ')
                        if password == submit_password:
                            print('Registration completed successfully!')
                            check = input('Wanna look at infos? ')
                            if check == 'yes':
                                print(f' Name: {name}\n Surname: {surname}\n Year: {year}\n Mail address: {mail}')
                            elif check == 'no':
                                print(f'{name} {surname}, Good luck!')
                        else:
                            print('Please try again')
                    else:
                        print('Please add correct password')
                else:
                    print('Your mail addres is not correct')
            else:
                print('ERROR')
        else:
            print('Please type your surname correct')
    else:
        print('Please type your name correct')  

login()
