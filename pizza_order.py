import datetime
import time
import pandas as pd

class Pizza():
    # Toplam ücreti, sipariş özetini tutan ve bu bilgilere erişimi sağlayan metodlar bulunduran Pizza sınıfı.
    cost = 0.0
    description = ""

    def get_cost(self):
        return f"{self.cost:.2f} TL"

    def get_description(self):
        return f"{self.description}"

class Klasik(Pizza):
    # Klasik pizza sınıfı.
    def __init__(self, boyut):
        self.aciklama = "Klasik Pizza"
        self.fiyatlar = {
            "küçük": 94.90,
            "orta": 119.90,
            "büyük": 174.90}
        fiyat = self.fiyatlar[boyut]
        Pizza.cost += fiyat
        ozet = f"{self.aciklama}({boyut}) : "
        Pizza.description += ozet

class Margherita(Pizza):
    # Margherita pizza sınıfı.
    def __init__(self, boyut):
        self.aciklama = "Margarita Pizza"
        self.fiyatlar = {
            "küçük": 94.90,
            "orta": 119.90,
            "büyük": 174.90}
        fiyat = self.fiyatlar[boyut]
        Pizza.cost += fiyat
        ozet = f"{self.aciklama}({boyut}) : "
        Pizza.description += ozet

class Turk(Pizza):
    # Türk pizza sınıfı.
    def __init__(self, boyut):
        self.aciklama = "Türk Pizza"
        self.fiyatlar = {
            "küçük": 109.90,
            "orta": 134.90,
            "büyük": 189.90}
        fiyat = self.fiyatlar[boyut]
        Pizza.cost += fiyat
        ozet = f"{self.aciklama}({boyut}) : "
        Pizza.description += ozet

class Dominos(Pizza):
    # Dominos pizza sınıfı.
    def __init__(self, boyut):
        self.aciklama = "Dominos Pizza"
        self.fiyatlar = {
            "küçük": 119.90,
            "orta": 159.90,
            "büyük": 219.90}
        fiyat = self.fiyatlar[boyut]
        Pizza.cost += fiyat
        ozet = f"{self.aciklama}({boyut}) : "
        Pizza.description += ozet

class Decorator(Pizza):
    # Pizza soslarını içeren sınıf.
    def add_cost(fiyat):
        Pizza.cost+=fiyat
    def add_description(description):
        Pizza.description+=description

class Zeytin(Decorator):
    # Zeytin sos sınıfı.
    def __init__(self):
        self.aciklama = "Zeytin"
        self.fiyat = 18
        Decorator.add_cost(self.fiyat)
        Decorator.add_description((self.aciklama + ", "))

class Mantar(Decorator):
    # Mantar sos sınıfı.
    def __init__(self):
        self.aciklama = "Mantar"
        self.fiyat = 23
        Decorator.add_cost(self.fiyat)
        Decorator.add_description((self.aciklama + ", "))

class KeciPeyniri(Decorator):
    # Keçi peyniri sos sınıfı.
    def __init__(self):
        self.aciklama = "Keçi Peyniri"
        self.fiyat = 21
        Decorator.add_cost(self.fiyat)
        Decorator.add_description((self.aciklama + ", "))

class Et(Decorator):
    # Et sos sınıfı.
    def __init__(self):
        self.aciklama = "Et"
        self.fiyat = 29
        Decorator.add_cost(self.fiyat)
        Decorator.add_description((self.aciklama + ", "))

class Sogan(Decorator):
    # Soğan sos sınıfı.
    def __init__(self):
        self.aciklama = "Soğan"
        self.fiyat = 13
        Decorator.add_cost(self.fiyat)
        Decorator.add_description((self.aciklama + ", "))
        
class Misir(Decorator):
    # Mısır sos sınıfı.
    def __init__(self):
        self.aciklama = "Mısır"
        self.fiyat = 15
        Decorator.add_cost(self.fiyat)
        Decorator.add_description((self.aciklama + ", "))

def boyut_secimi():
    # Müşterinin pizza boyutunu seçmesini sağlayan fonksiyon.
    while True:
        boyut = input("Pizza boyutunu 'küçük','orta' yada 'büyük' olacak şekilde seçiniz:")
        boyut = boyut.lower()
        data=["küçük","orta","büyük"]
        if boyut in data:
            break
        else:
            print("\nYanlış giriş yaptınız. Lütfen tekrar deneyiniz!")
    return boyut

def secilen_pizza(boyut):
    # Secilen pizza boyutunu giridi olarak alan ve müşterinin pizza seçimini yapmasını sağlayan fonksiyon.
    while True:
        secim = input("Pizza seçiminizi yapınız:")
        if secim == "1":
            pizza = Klasik(boyut)
            break
        elif secim == "2":
            pizza = Margherita(boyut)
            break
        elif secim == "3":
            pizza = Turk(boyut)
            break
        elif secim == "4":
            pizza = Dominos(boyut)
            break
        else:
            print("\nYanlış bir değer girdiniz. Lütfen tekrar deneyiniz!")
    return pizza

def secilen_sos():
    # Müşterini sos seçimini yapmasını sağlayan fonksiyon.
    sos = object
    sos_secimleri = []
    while True:
        secim = input("\nEklemek istediğiniz sosun yanında bulunan numarayı giriniz:\nSeçim işlemini tamamlamak için 'q' tuşuna basınız:")
        secim=secim.lower()
        if secim in sos_secimleri:
            print("\nBu seçimi daha önce yaptınız!")
        else:
            if secim == "1":
                sos = Zeytin()
                sos_secimleri.append(secim)
            elif secim == "2":
                sos = Mantar()
                sos_secimleri.append(secim)
            elif secim == "3":
                sos = KeciPeyniri()
                sos_secimleri.append(secim)
            elif secim == "4":
                sos = Et()
                sos_secimleri.append(secim)
            elif secim == "5":
                sos = Sogan()
                sos_secimleri.append(secim)
            elif secim == "6":
                sos = Misir()
                sos_secimleri.append(secim)
            elif secim == "q":
                break
            else:
                print("\nYanlış bir değer girdiniz. Lütfen tekrar deneyiniz!")
                continue
    return sos

def kimlik_bilgi():
    # Müşterinin ismini ve TC kimlik numarasını alan ve kontrol eden fonksiyon.
    isim = input("Lütfen isminizi giriniz:")
    while True:
        try:
            kimlik_no = int(input("Lütfen TC Kimlik numaranızı tuşlayınız:"))
        except ValueError:
            print("TC kimlik numarası yalnızca rakamlardan oluşmalıdır! Lütfen yeniden giriş yapınız!")
            continue
        if len(str(kimlik_no)) != 11:
            print("TC Kimlik numarası 11 haneden oluşmalıdır. Lütfen tekrar deneyiniz!")
            continue
        else:
            break
    return isim, kimlik_no

def kredi_karti():
    # Kredi kartı bilgilerini alıp, kontrol eden ve ödemeyi alan fonksiyon.
    while True:
        try:
            kredi_karti_no = int(input("Lütfen kredi kartı numaranızı tuşlayınız:"))
        except ValueError:
            print("Kredi kartı numarası yalnızca rakamlardan oluşmalıdır. Lütfen yeniden giriş yapınız!")
            continue
        if len(str(kredi_karti_no)) != 16:
            print("Kredi kartı numarası 16 haneden oluşmalıdır. Lütfen tekrar deneyiniz!")
            continue
        else:
            break

    while True:
        try:
            cvc = int(input("Üç haneli kredi kartı CVC kodunu tuşlayınız:"))
        except ValueError:
            print("CVC kodu yalnızca rakamlardan oluşmalıdır. Lütfen yeniden giriş yapınız!")
            continue
        if len(str(cvc)) != 3:
            print("CVC kodu 3 haneden oluşmalıdır. Lütfen yeniden giriş yapınız!")
            continue
        else:
            break

    while True:
        try:
            sifre = int(input("Kredi kartı şifrenizi giriniz:"))
        except ValueError:
            print("Kredi kartı şifresi yalnızca rakamlardan oluşmalıdır. Lütfen yeniden giriş yapınız!")
            continue
        if len(str(sifre)) != 4:
            print("Şifre 4 haneden oluşmalıdır. Lütfen yeniden giriş yapınız!")
            continue
        else:
            break

    print("Bilgiler kontrol ediliyor")
    for i in range(15):
        time.sleep(0.3)
        print(".", end="", flush=True)
    print("\nÖdeme işlemi tamamlandı.")

    return kredi_karti_no, cvc, sifre

def siparis():
    # Sipariş için gerekli sınıfları ve fonksiyonları çağıran ana fonksiyon.
    pizza = Pizza()
    sos = Decorator()
    print("Pizza sipariş sistemine hoş geldiniz.")
    while True:
        karar = input("Sipariş işleminden çıkmak için 'q' ya devam etmek için 'enter' tuşuna basınız:")
        karar=karar.lower()
        if karar == "q":
            break
        elif karar == "":
            dosya1 = open("Pizza.txt", "r", encoding="utf-8")
            dosya2 = open("Sos.txt", "r", encoding="utf-8")
            print(dosya1.read())
            dosya1.close()
            boyut = boyut_secimi()
            pizza = secilen_pizza(boyut)
            print(dosya2.read())
            dosya2.close()
            sos = secilen_sos()
            Pizza.description += "+"
        else:
            print("Tanımlanamayan bir giriş yaptınız. Lütfen tekrar deneyiniz!")
    isim = ""
    kimlik_no = 0
    kredi_karti_no = 0
    cvc = 0
    sifre = 0
    zaman = ""

    cost = Pizza().get_cost()
    description = Pizza().get_description()
    print("\nSiparişin toplam tutarı:", cost)
    print("Sipariş içeriği:\n", description, sep="")
    if cost != "0.00 TL":
        isim, kimlik_no = kimlik_bilgi()
        kredi_karti_no, cvc, sifre = kredi_karti()
        zaman = datetime.datetime.now()
        zaman = datetime.datetime.ctime(zaman)

    bilgiler = pd.DataFrame(data=[isim, kimlik_no, kredi_karti_no, cvc, sifre, description, zaman, cost],
                            index=["İsim", "TC Kimlik No", "Kredi Kartı Numarası", "CVC", "Kredi Kartı Şifresi",
                                   "Sipariş Özeti", "Sipariş Zamanı", "Toplam Tutar"])
    bilgiler = bilgiler.T

    return bilgiler

bilgiler = siparis()
try:
    df = pd.read_csv("Orders_Database.csv")
    df2=pd.concat([bilgiler,df])
    df2.to_csv("Orders_Database.csv",index=False,encoding="utf-8")
except FileNotFoundError:
    bilgiler.to_csv("Orders_Database.csv", index=False, encoding="utf-8")

print(bilgiler)

input("Sonlandırmak için herhangi bir tuşa basınız:")
