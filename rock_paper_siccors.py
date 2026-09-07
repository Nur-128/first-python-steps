# -*- coding: utf-8 -*-
import customtkinter as ctk
import random

#penceremiz
pencere=ctk.CTk()
pencere.title("taş kağıt makas")
pencere.geometry("1920x1040")
ctk.set_appearance_mode("dark")

for i in range(4):
    pencere.rowconfigure(i, weight=1)
for i in range(3):
    pencere.columnconfigure(i, weight=1)

#pcnin secimi 
secenekler=["taş", "kağıt","makas"]

#kullanıcının ve bilgisayarın puanı için değişkenler
user=0
pc=0

#OYUN BİTTİ
oyun_bitti=False

#fonksiyonlar
def oyun(kullanıcı_secimi):
    if oyun_bitti:
        return
    
    global pc, user
    pc_secimi=random.choice(secenekler)
    if (kullanıcı_secimi==pc_secimi):
        sonuç_metni.configure(text="berabere")
    elif (
        (kullanıcı_secimi=="taş" and pc_secimi=="makas")
        or (kullanıcı_secimi=="kağıt" and pc_secimi=="taş")
        or (kullanıcı_secimi=="makas" and pc_secimi=="kağıt")
    ):
        user+=1 
        puan_metni.configure(text="puanınz: "+ str(user) + " bilgisayarın  puanı :"+ str(pc))
        sonuç_metni.configure(text="siz kazandınız tebrikler! bilgisayarın seçimi: " + pc_secimi)
    else:
        pc+=1
        puan_metni.configure(text="puanınız: "+ str(user) + " bilgisayarın  puanı :"+ str(pc))
        sonuç_metni.configure(text="bilgisayar kazandı, siz kaybettiniz! bilgisayarın seçimi: " +pc_secimi)
    oyun_sonu()

#oyunu bitirme fonksiyonu
def oyun_sonu():
    global pc, user
    global oyun_bitti

    if user==10:
        oyun_bitti=True
        sonuç_metni.configure(text="oyun bitti, siz kazandınız tebrikler!")
    elif pc==10:
        oyun_bitti=True
        sonuç_metni.configure(text="oyun bitti, bilgisayar kazandı")
    else:
        ...

#puan yazısı
puan_metni=ctk.CTkLabel(pencere, text="puanınız: " + str(user) + " bilgisayarın puanı : " + str(pc), font=("arial", 30))
puan_metni.grid(row=3, column=0, columnspan=3, sticky="nsew", pady=20)

#seçim yaptırma yazısı
secim=ctk.CTkLabel(pencere, text="seçiminizi yapınız", font=("Arial", 30))
secim.grid(row=0, column=0, columnspan=3)

#sonuç yazısı
sonuç_metni=ctk.CTkLabel(pencere, text="", font=("Arial", 50))
sonuç_metni.grid(row=2, column=0, columnspan=3, sticky="nsew", pady=20)

#butonlar
tas_butonu = ctk.CTkButton(pencere, text="taş", command=lambda: oyun("taş"), fg_color="#a55af4", hover_color="#eecffe", width=300, height=60)
tas_butonu.grid(row=1, column=0, padx=10)

kağıt_butonu = ctk.CTkButton(pencere, text="kağıt", command=lambda: oyun("kağıt"), fg_color="#a55af4", hover_color="#eecffe", width=300, height=60)
kağıt_butonu.grid(row=1, column=1, padx=10)

makas_butonu = ctk.CTkButton(pencere, text="makas", command=lambda: oyun("makas"), fg_color="#a55af4", hover_color="#eecffe", width=300, height=60)
makas_butonu.grid(row=1, column=2, padx=10)

pencere.mainloop()