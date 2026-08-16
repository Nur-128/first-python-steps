#random'u çağıralım
import random
bilgisayarin_secimi=random.randint(1,20)
hak=3
kullanicinin_tahmini=0

while kullanicinin_tahmini!=bilgisayarin_secimi and hak>0:
    kullanicinin_tahmini=int(input("1-20 arasında bir sayı tahmin ediniz: "))
    
    if kullanicinin_tahmini<bilgisayarin_secimi:
        print("daha büyük bir sayı seç.")
        hak-=1
        print("kalan hakkınız:",hak)
    elif kullanicinin_tahmini>bilgisayarin_secimi:
        print("daha küçük bir sayı seç.")
        hak-=1
        print("kalan hakkınız:",hak)
        
    else:
        print("helal lan! doğru bildin")
print("oyun bitti. bilgisayarın seçtiği sayı,",bilgisayarin_secimi)
