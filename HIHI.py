#vi bygger upp data och ger dom olika värde för 3 olika personer

akmalÅlder = 16
akmalLängd = 190
akmalSkola = True

#person2
lukaÅlder = 16
lukaLängd = 177 #cm
lukaSkola = True
#person3
hamodiÅlder = 55
hamodiLängd = 176 #cm
hamodiSkola = False
#våran startmeny där vi kan kolla data
def visaPersonData(person):
  if person == "1":
    print("Ålder:", akmalÅlder, "År")
    print("Längd:", akmalLängd, "cm")
    print("Går i skola:", akmalSkola)
  elif person == "2":
    print("Ålder:", lukaÅlder, "År")
    print("Längd:", lukaLängd, "cm")
    print("Går i skola:", lukaSkola)
  elif person == "3":
    print("Ålder:", hamodiÅlder, "År")
    print("Längd:", hamodiLängd, "cm")
    print("Går i skola:", hamodiSkola)
  else:
    print("Ogiltigt val")

while True:
  print("Hi and welcome to the menu, please browse in our database")
  print("1. Akmal")
  print("2. Luka")
  print("3. Hamodi")
  val = input("Välj en person: ")
  visaPersonData(val)


