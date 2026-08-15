kullanıcın_girdiği_sayı=int(input("bir tam sayı giriniz: "))
kullanıcı_ne_kadar_azaltacak=int(input("kaçar kaçar azalacak?: "))
i=kullanıcın_girdiği_sayı
while (i>0):
    print(i,  end="  ")
    i=i-kullanıcı_ne_kadar_azaltacak