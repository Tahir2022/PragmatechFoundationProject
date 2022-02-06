from re import I
from countries import olkeler # (shorturl.at/lxD15)

def FindCity(cityname):
  # seher adi daxil edildiyi zaman o seherin aid olduğu ölkəni göstərsin
  for i in olkeler:
      if cityname in olkeler.get(i):
          print(i)

      
def FindCountry(countryname):
  # olke adi daxil edildiyi zaman o olkeye aid olan seherlerin adlarini ekranda gostersin
  print("\n".join(olkeler.get(countryname)))


def CityCountMax():
  # ek cox sehere sahib olan olkeni gostersin
    say=0
    for i in olkeler:
        if len(olkeler.get(i))>say:
            more_city=i
            say=len(olkeler.get(i))
    print(more_city)


def CountAllCities():
  # butun seherlerin sayini ekranda gostersin
    say=0
    for i in olkeler:
        say+=len(olkeler.get(i))
    print(say)

FindCity("Shar")
FindCountry("Afghanistan")
CityCountMax()
CountAllCities()