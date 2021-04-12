import mod
while True:
    print("""
    Toplama : 1 
    Çıkarma : 2
    Çarpma : 3
    Bölme : 4
    Üs bulma : 5
    faktoriyel : 6
    permütasyon : 7
    Kombinasyon : 8
    Çıkış : q
    """)

    """
    Toplama
    """
    giris=input("İşlem Numarası Giriniz : ")
    if giris=="q" or giris=="Q":
        print("Programdan Çıkılıyor ....")
        print("Çıkış Başarılı !")
        break
    else:
        giris=int(giris)
        if giris==1:
            t1=int(input("1.Eleman : "))
            t2=int(input("2.Eleman : "))
            print("Sonuç : {}".format(mod.toplama(t1,t2)))
            continue

        elif giris==2:
            c1=int(input("1.Eleman : "))
            c2=int(input("2.Eleman : "))
            print("Sonuç : {}".format(mod.cikar(c1,c2)))
            continue

        elif giris==3:
            car1=int(input("1.Eleman : "))
            car2=int(input("2.Eleman : "))
            print("Sonuç : {}".format(mod.carp(car1,car2)))
            continue
    
        elif giris==4:
            bol1=int(input("1.Eleman : "))
            bol2=int(input("2.Eleman : "))
            print("Sonuç : {}".format(mod.bol(bol1,bol2)))
            continue
        
        elif giris==5:
            taban=int(input("Taban : "))
            us=int(input("Üs : "))
            print("Sonuç : {}".format(mod.usbul(taban,us)))
            continue
        
        elif giris==6:
            fac=int(input("Sayı : "))
            print("Faktoriyel : {}".format(mod.faktoriyel(fac)))
            continue
       
        elif giris==7:
            sayi=int(input("Sayı : "))
            sayma=int(input("Sayma Değeri : "))
            print("Permütasyon p({},{}) : {}".format(sayi,sayma,mod.p(sayi,sayma)))
            continue
       
        elif giris==8:
            sayi1=int(input("Sayı : "))
            secme=int(input("Seçme Değeri : "))
            print("Kombinasyon c({},{}) : {}".format(sayi1,secme,mod.c(sayi1,secme)))
            continue
        else:
            print("Hatalı İşlem Numarası !")
            continue
i=input()