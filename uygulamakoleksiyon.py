import random
import time

def tümislemler():
    a = input('A Harfine Değer Ver; ')
    b = input('B Harfine Değer Ver; ')
    c = input('C Harfine Değer Ver; ')
    toplama=(float(a)+float(b)+float(c))
    cikarma=(float(a)-float(b)-float(c))
    carpma=(float(a)*float(b)*float(c))
    bolme=(float(a)/float(b)/float(c))
    kok=(float(a)** 0.5)
    print("Toplam :{0} ".format(toplama))
    print("Çıkarma :{0} ".format(cikarma))
    print("Bölme :{0} ".format(bolme))
    print("Çarpma :{0} ".format(carpma))
    print("KaraKök :{0} ".format(kok))
    pass

def toplama():
    a = input('A. Değerine Sayı Gir; ')
    b = input('B. Değerine Sayı Gir; ')
    toplam=float(a)+float(b)
    print("Toplama İşleminin Sonucu; {0} ".format(toplam))
    pass

def çıkarma():
    a = input('A. Değerine Sayı Gir; ')
    b = input('B. Değerine Sayı Gir; ')
    cıkarma=float(a)-float(b)
    print("Çıkarma İşleminin Sonucu; {0} ".format(cıkarma))
    pass

def bolme():
    a = input('A. Değerine Sayı Gir; ')
    b = input('B. Değerine Sayı Gir; ')
    bolme=float(a)/float(b)
    print("Bölme İşleminin Sonucu; {0} ".format(bolme))
    pass

def çarpma():
    a = input('A. Değerine Sayı Gir; ')
    b = input('B. Değerine Sayı Gir; ')
    carmp=float(a)*float(b)
    print("Çarpma İşleminin Sonucu; {0} ".format(carmp))
    pass

def karakok():
    a = input('Değer Girin; ')
    karakok=float(a)** 0.5
    print("karakok İşleminin Sonucu; {0} ".format(karakok))
    pass

def usalma():
    print('Bu İşlem Şuanda kullanılmamakta, Bu İşlem Bakımda !!!')
    pass
    #a = input('A. Değerine Sayı Gir; ')
    #b = input('B. Değerine Sayı Gir; ')
    #us= a**b
    #print("Üs İşlemi Sonucu; {0} ".format(us))
    #pass

def toplamacikarma():
    a = input('A. Değerine Sayı Gir; ')
    b = input('B. Değerine Sayı Gir;')
    c = input('Kaç İle Çıkarılsın; ')
    toplamacikm = float(a)+(b)
    sonc = float(toplamacikm)-(c)
    print('Sonuç: {0}'.format(sonc))
    pass

def carpmabolme():
    a = input('A. Değerine Sayı Gir; ')
    b = input('B. Değerine Sayı Gir;')
    c = input('Kaç İle Çarpılsın; ')
    carpmbol = float(a)+(b)
    sonc = float(carpmbol)*(c)
    print('Sonuç: {0}'.format(sonc))
    pass

def doublekarkok():
    a = input('1. Sayıyı Gir; ')
    b = input('2. Sayıyı Gir; ')
    st=float(a)** 0.5
    at=float(a)** 0.5
    print("1. Sonuç; {0}".format(st))
    print("2. Sonuç; {0}".format(at))
    pass

def main():
    while True:
        print("--- İşlem Menüsü ---")
        print("1. Tüm İşlemler")
        print("2. Toplama İşlemi")
        print("3. Çıkarma İşlemi")
        print("4. Bölme İşlemi")
        print("5. Çarpma İşlemi")
        print("6. Karakok İşlemi")
        print("7. ÜS İşlemi")
        print("8. Çarpma Ve Bölme")
        print("9. Toplama Ve Çıkarma")
        print("10. 2li Karakök Bulma")
        print("0. Çıkış")

        secim = input("İşlem Numarası Girin (0-10): ")
        print("Made by Ali Ramazan and Lexy Team")

        if secim == "1":
            tümislemler()
        elif secim == "2":
            toplama()
        elif secim == "3":
            çıkarma()
        elif secim == "4":
            bolme()
        elif secim == "5":
            çarpma()
        elif secim == "6":
            karakok()
        elif secim == "7":
            usalma()
        elif secim == "9":
            toplamacikarma()
        elif secim == "8":
            carpmabolme()
        elif secim == "10":
            doublekarkok()
        elif secim == "0":
            print("İşlemler koleksiyonundan çıkılıyor...")
            break
        else:
            print("Geçersiz seçim. Lütfen geçerli bir seçim yapın (0-10).")

if __name__ == "__main__":
    print("İşlem koleksiyonuna hoş geldiniz!")
    main()
