class User:
  __login = ''
  __passwd = ''
  __logged = False
  
  def _init_(self, login, passwd):
    self.__login = login
    self.__passwd = hash(passwd)
  
  def SignUp(self):
    # save login and password to database
    print(self.__login)
    print(self.__passwd)
  
  def LogIn(self):
    # get login and password from database
    login = 'root'
    passwd = hash('root')
    if self._login == login and self._passwd == passwd:
      self.__logged = True
      print('User is logged')
  
  def LogOut(self):
    self.__login = ''
    self.__passwd = ''
    self.__logged = False
    print('User is logout')
  
  def isLogged(self):
    return self.__logged

menu = """1. Qeydiyyatdan keçmək üçün [1] yazın
2. Sistemə daxil olmaq üçün [2] yazın
3. Ana menyuya qayıtmaq üçün [3] yazın
4. Sistemdən çıxmaq üçün [4] yazın
5. Proqramdan çıxmaq üçün [5] yazın
"""
user = None

while(True):
  print(menu)
  k = int(input())
  
  if k == 1 or k == 2:
    print('- İstifadəçi adınız: ', end='')
    login = input()
    print('- Parolunuz: ', end='')
    passwd = hash(input())
    user = User(login, passwd)
  
  if k == 1:
    if user: user.SignUp()
  elif k == 2:
    if user and not user.isLogged(): user.LogIn()
  elif k == 3:
    continue
  elif k == 4:
    if user: user.LogOut()
  elif k == 5:
    break
  else: print('Naməlum seçim')
  print()