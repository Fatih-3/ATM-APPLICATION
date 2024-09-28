hesaplar = [
    {
        "ad": "Fatih Güloğlu",
        "HesapNo": "12345",
        "bakiye": "20000",
        "ekHesap": "3000",
        "ekHesapLimiti": "5000",
        "username": "fatih",
        "password": "1234"
    },
    {
        "ad": "Hamza Aşan",
        "HesapNo": "12345",
        "bakiye": "20000",
        "ekHesap": "2000",
        "ekHesapLimiti": "5000",
        "username": "HAMZA",
        "password": "1234"
    }
]

def ParaYatırma(hesap):
    miktar = float(input("Yatırmak istediğiniz miktarı giriniz: "))
    ekHesapLimiti = float(hesap["ekHesapLimiti"])
    mevcutEkHesap = float(hesap["ekHesap"])

    if mevcutEkHesap < ekHesapLimiti:
        ekHesapEksik = ekHesapLimiti - mevcutEkHesap

        if miktar >= ekHesapEksik:
            hesap["ekHesap"] = ekHesapLimiti
            hesap["bakiye"] = float(hesap["bakiye"]) + (miktar - ekHesapEksik)
            print(f"{ekHesapEksik} TL ek hesaba yatırıldı, kalan {miktar - ekHesapEksik} TL ana bakiyeye eklendi.")
        else:
            hesap["ekHesap"] = mevcutEkHesap + miktar
            print(f"Tüm para ({miktar} TL) ek hesaba yatırıldı.")
    else:
        hesap["bakiye"] = float(hesap["bakiye"]) + miktar
        print(f"{miktar} TL ana bakiyeye yatırıldı.")

    print(f"Güncel bakiye: {hesap['bakiye']} TL")
    print(f"Güncel ek hesap: {hesap['ekHesap']} TL")
    print("\n")

def BakiyeSorgulama(hesap):
    print(f"Bakiye: {hesap['bakiye']} TL")
    print(f"Ek Bakiye: {hesap['ekHesap']} TL")
    print("\n")

def ParaCekme(hesap):
    miktar = float(input("Çekmek istediğiniz miktarı giriniz: "))

    if float(hesap["bakiye"]) >= miktar:
        hesap["bakiye"] = float(hesap["bakiye"]) - miktar
        print("Paranızı alabilirsiniz.")
    else:
        toplam = float(hesap["bakiye"]) + float(hesap["ekHesap"])
        if toplam >= miktar:
            EkHesapIzni = input("Ek hesap kullanılsın mı? (e/h): ")
            if EkHesapIzni == "e":
                KullanilacakMiktar = miktar - float(hesap["bakiye"])
                hesap["bakiye"] = 0
                hesap["ekHesap"] = float(hesap["ekHesap"]) - KullanilacakMiktar
                print("Paranızı alabilirsiniz.")
            else:
                print("Üzgünüz, bakiyeniz yetersiz.")
        else:
            print("Yetersiz bakiye.")
    print("\n")

def menu(hesap):
    while True:
        print(f"Merhaba, {hesap['ad']}")
        print("1- Bakiye Sorgulama")
        print("2- Para Çekme")
        print("3- Para Yatırma")
        print("4- Çıkış Yap")
        
        islem = input("Yapmak istediğiniz işlemi seçiniz: ")
        print("\n")
        if islem == "1":
            BakiyeSorgulama(hesap)
        elif islem == "2":
            ParaCekme(hesap)
        elif islem == "3":
            ParaYatırma(hesap)
        elif islem == "4":
            print("Çıkış yapılıyor...")
            break
        else:
            print("Yanlış işlem seçtiniz. Tekrardan deneyiniz.")
        print("\n")

def login():
    username = input("Username: ")
    password = input("Password: ")
    isLoggedIn = False
    for hesap in hesaplar:
        if hesap["username"] == username and hesap["password"] == password:
            isLoggedIn = True
            menu(hesap)
            break

    if not isLoggedIn:
        print("Username ya da password yanlış girilmiştir. Tekrar deneyiniz.")
    print("\n")

login()
