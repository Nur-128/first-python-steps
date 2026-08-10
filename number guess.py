#random'u çağıralım
import random
bilgisayarın_seçimi=random.randint(1,20)
kullanıcının_tahmini=0
while kullanıcının_tahmini!=bilgisayarın_seçimi:
    kullanıcının_tahmini=int(input("1 ile 20 arasında bir sayı tahmin edin: "))
    if kullanıcının_tahmini<bilgisayarın_seçimi:
         print("daha büyük bir sayı seç.")
    elif kullanıcının_tahmini>bilgisayarın_seçimi:
        print("daha küçük bir sayı seç.")
    else:
        print("helal lan! doğru bildin")
