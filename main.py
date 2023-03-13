#Modülleri içeri aktardım.

import csv
from datetime import datetime

class Pizza():
    def __init__(self,desc,cost):
        self._desc = desc
        self._cost = cost
      
    def get_cost(self):
        return self._cost
    def get_desc(self):
        return self._desc

#Alt sınıflar:
class TurkPizza(Pizza):
    def __init__(self):
        
        desc = "Kalın tabanıyla doyurucu pizza."
        cost = 75
        super().__init__(desc,cost)
    
class DominosPizza(Pizza):
    def __init__(self):
        
        desc = "İnce tabanlı pizza."
        cost = 69
        super().__init__(desc,cost)
      
class SpecialPizza(Pizza):
    def __init__(self):
        
        desc = "Özel tabanıyla orijinal lezzetli pizza."
        cost = 100
        super().__init__(desc,cost)

#Decorator sınıfı:
class Toppings():
    def __init__(self,component):
        self.component = component
    def get_desc(self):
        return self.component.get_desc() + ' ' + Pizza.get_desc(self)
    
    def get_cost(self):
        return self.component.get_cost() + Pizza.get_cost(self)
    
class Zeytin(Toppings):
    def __init__(self,component):
        super().__init__(component)
        self.desc = "10 adet zeytin ekler."
        self.cost = 5

class Mantarlar(Toppings):
    def __init__(self, component):
        super().__init__(component)
        self.desc = "10 adet mantar ekler."
        self.cost = 5

class KeciPeyniri(Toppings):
    def __init__(self, component):
        super().__init__(component)
        self.desc = "10 dilim keçi peyniri ekler."
        self.cost = 8

class Et(Toppings):
    def __init__(self, component):
        super().__init__(component)
        self.desc = "50 gram et ekler"
        self.cost = 10

class Sogan(Toppings):
    def __init__(self, component):
        super().__init__(component)
        self.desc = "1 adet dilimlenmiş soğan ekler."
        self.cost = 3

class Misir(Toppings):
    def __init__(self, component):
        super().__init__(component)
        self.desc = "Ekstra mısır ekler."
        self.cost = 5

#Müşterinin seçim yapabilmesi için main fonksiyonunu oluşturdum:
    
def main():
    with open("menu.txt" , "r") as file:
        print(file.read())

    pizza_choice = int(input("Lütfen pizza tabanını seçiniz (1-3): "))
    while True:
        if pizza_choice == 1:
            pizza = TurkPizza()
            break
        elif pizza_choice == 2:
            pizza = DominosPizza()
            break
        elif pizza_choice == 3:
            pizza = SpecialPizza()
            break
        else:
            print("\nYanlış seçim")
            return main()
        
    toppings_choice = input("Lütfen eklemek istediğiniz malzemeleri seçiniz (Çıkış için 'q' tuşuna basınız.)(11-16).  ")
    toppings = []
    while toppings_choice != 'q':
      toppings_choice = int(toppings_choice)
      if toppings_choice in [11, 12, 13, 14, 15, 16]:
        toppings.append(toppings_choice)
      else:
        print("Yanlış tuşladınız. Tekrar deneyiniz.")
      toppings_choice = input("Lütfen eklemek istediğiniz malzemeleri seçiniz (Çıkış için 'q' tuşuna basınız.)(11-16).  ")
    #Kullanıcının seçtiği sosların fiyatları
    toppings_price = {
            11: 5,    #Zeytin
            12: 5,    #Mantarlar
            13: 8,    #Keçi Peyniri
            14: 10,   #Et
            15: 3,    #Soğan
            16: 5     #Mısır
            }
    toppings_sum = sum(toppings_price[i] for i in toppings)
    print("Toplam fiyat: ", pizza.get_cost() + toppings_sum)



#Kullanıcının sipariş bilgilerini girmesi
    name = input("İsim: ")
    id_number = input("TC Kimlik Numarası: ")
    credit_card_number = input("Kredi Kartı Numarası: ")
    credit_card_password = input("Kredi Kartı Şifresi: ")

#Siparişin kaydedilmesi
    order_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    order_description = pizza.get_desc()

    with open('Orders_Database.csv', mode='a', newline='') as orders_file:
        fieldnames = ['Name', 'ID Number', 'Credit Card Number', 'Credit Card Password', 'Order Description', 'Order Time']
        writer = csv.DictWriter(orders_file, fieldnames=fieldnames)
        writer.writerow({'Name': name, 'ID Number': id_number, 'Credit Card Number': credit_card_number, 
                         'Credit Card Password': credit_card_password, 'Order Description': order_description,
                         'Order Time': order_time})
    print("Siparişiniz alınmıştır.")
main()
