def sistemegiris(tnick,tpass):
    while True:
        in_nick=input("Kullanıcı  Adı : ")
        in_pass=input("Parola : ")
        if in_nick==tnick and in_pass==tpass:
            print("Giriş Başarılı ... ")
            break
            i=input()
        else:
            continue