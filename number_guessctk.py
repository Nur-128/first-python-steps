#kütüphanelerimiz
import random
import customtkinter as ctk

hak=5
oyun_bitti=False

#pc nin secimi
pcnin_secimi=random.randint(1,40)

#penceremiz
pencere=ctk.CTk()
pencere.title("sayı tahmin oyunu")
pencere.geometry("1920x1040")
pencere._set_appearance_mode("dark")
pencere.rowconfigure(0, weight=1)
pencere.columnconfigure(0, weight=1)

#kullanıcıdan sayı alma
def sayi_almak():
    global hak, pcnin_secimi, oyun_bitti
    if oyun_bitti:
        return
    sayı=int(sayı_kutusu.get())

#sayı 40 dan büyük veya 0 dan küçük mü?
    if sayı<0 or sayı>40:
        sonuç_metni.configure(text="gireceğiniz sayı 40'tan küçük olmalı ve 0 dan büyük olmalı!")
        return
   

#sayıları karşılaştırma
    if sayı==pcnin_secimi:
        oyun_bitti=True
        sonuç_metni.configure(text="tebrikler doğru tahmin ettiniz! bilgisayarın seçimi " + str(pcnin_secimi) + "kalan hakkınız: " +str(hak))
    elif sayı>pcnin_secimi:
        hak-=1
        sonuç_metni.configure(text="daha küçük bir sayı giriniz! " + "kalan hakkınız: " + str(hak))
    elif sayı<pcnin_secimi:
        hak-=1
        sonuç_metni.configure(text="daha büyük bir sayı giriniz! " + "kalan hakkınız: " + str(hak))
    if hak==0:
        oyun_bitti=True
        sonuç_metni.configure(text="oyun bitti bilgisaayrın seçimi: " +str(pcnin_secimi))


#oyun bitince çalışacak funtion
def yeniden_başlat():
    global hak, pcnin_secimi, oyun_bitti
    hak=5
    pcnin_secimi=random.randint(1, 40)
    oyun_bitti=False
    sonuç_metni.configure(text="")
    sayı_kutusu.delete(0, "end")

#yeniden başlat 
return_button=ctk.CTkButton(pencere, text="yeniden başlat", width=150, height=50, fg_color="purple", hover_color="#856fa8", command=yeniden_başlat)
return_button.grid(row=4, column=4, pady=20, padx=20 )
      
#butonumuz
tahmin_button=ctk.CTkButton(pencere, text="tahmin et", command=sayi_almak, width=150, height=50, fg_color="#6b5fad", hover_color="#856fa8")
tahmin_button.grid(row=0, column=1, padx=30, pady=30)

#sayı kutusu
sayı_kutusu=ctk.CTkEntry(pencere, placeholder_text="1 ile 40 arasında 1 sayı giriniz.", font=("arial", 40), height=50, width=300)
sayı_kutusu.grid(row=0, column=0, padx=20, pady=20)

#sonuç yazısı
sonuç_metni=ctk.CTkLabel(pencere, text="", font=("arial", 50))
sonuç_metni.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

pencere.mainloop()