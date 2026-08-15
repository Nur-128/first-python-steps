#bizim şifremiz
sifre=int(2580)

#kulanıcı bir girisn bakalım
kullanicinin_girdiği_sifre=int(input("sifreyi giriniz: "))

#acaba kullanıcı ne yapmış????

while kullanicinin_girdiği_sifre != sifre:
 print("giriş başarısız,yeniden sifreyi giriniz:")  
 kullanicinin_girdiği_sifre=int(input("sifreyi tekrar giriniz: "))
print("sisteme hoş geldiniz!")

