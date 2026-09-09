kullanicinin_girdigi_islem=input("işlem seçininiz(+-*/): ")
kullanicinin_girdiği_sayi_1=float(input("sayı giriniz: "))
kullanicinin_girdiği_sayi_2=float(input("sayı giriniz: "))

#işlem seçme ve işlem yapma 
if kullanicinin_girdigi_islem=="+":
 sonuç=kullanicinin_girdiği_sayi_1+kullanicinin_girdiği_sayi_2
 print(sonuç)

elif kullanicinin_girdigi_islem=="-":
 sonuç=kullanicinin_girdiği_sayi_1-kullanicinin_girdiği_sayi_2
 print(sonuç)

elif kullanicinin_girdigi_islem=="*":
 sonuç=kullanicinin_girdiği_sayi_1*kullanicinin_girdiği_sayi_2
 print(sonuç)

elif kullanicinin_girdigi_islem=="/":
 sonuç=kullanicinin_girdiği_sayi_1/kullanicinin_girdiği_sayi_2
 print(sonuç)
#kullanıcı geçersiz bir şey yaparsa
else:
 print("geçersiz işlem...") 