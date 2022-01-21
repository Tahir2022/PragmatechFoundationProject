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
