def b(istenilen,mevcut,gelir):
    hafta=(istenilen-mevcut)/gelir
    ay=hafta/4
    yil=ay/12
    print("""
    Biriktirme Süresi :
    Hafta : {}
    Ay  : {}
    Yıl  : {}
    """.format(hafta,ay,yil))
    i=input()