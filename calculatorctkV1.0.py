#kütüphanemiz
import customtkinter as ctk
import calculator

#penceremiz(asıl olay)
window=ctk.CTk()
window.title("Calculator App")
window._set_appearance_mode("light")
window.geometry("777x510")

#değişkenlerimiz
sayı_1=""
seçilen_işlem=""

#label kutusu
işlem_kutusu = ctk.CTkFrame(
    master=window,
    width=753,                
    height=108,              
    fg_color="transparent",  
    border_color="#87aae2",   
    border_width=3,            
    corner_radius=10          
)
işlem_kutusu.grid(row=0, column=0, columnspan=4, pady=10, padx=10)
#işlem labeli
işlem=ctk.CTkLabel(
    window,
    text="buraya işlem gelecek",
    font=("arial", 50)
)
işlem.grid(row=0, column=0, columnspan=4, pady=10, padx=10)

#eşittir fonksiyonumuz
def eşittir():
     global sayı_1,seçilen_işlem,tıklanan_sayı
     sonuç=calculator.hesaplama(
          float(sayı_1),
          float(tıklanan_sayı),
          seçilen_işlem
     )
     işlem.configure(text=str(sonuç))

#işlem seçme fonksiyonumuz
def işlem_seç(operatör):
     global sayı_1,seçilen_işlem,tıklanan_sayı
     sayı_1=tıklanan_sayı
     seçilen_işlem=operatör
     tıklanan_sayı=""



#butonlara basınca çalışacak fonksiyonumuz
tıklanan_sayı=""
def sayı_basmak(sayi):
    global tıklanan_sayı
    tıklanan_sayı+=sayi
    işlem.configure(text=tıklanan_sayı)


button1=ctk.CTkButton(
    window,
    width= 88,
    height=75,
    fg_color="#3c6079",
    hover_color="#60839c",
    text="1",
    corner_radius=20,
    command=lambda: sayı_basmak("1")
)
button1.grid(row=1, column=0, pady=10, padx=10)

button2=ctk.CTkButton(
    window,
    width=88,
    height=75,
    fg_color="#3c6079",
    hover_color="#60839c",
    text="2",
    corner_radius=20,
    command=lambda: sayı_basmak("2")
)
button2.grid(row=1, column=1, pady=10, padx=10)

button3=ctk.CTkButton(
    window,
    width= 88,
    height=75,
    fg_color="#3c6079",
    hover_color="#60839c",
    text="3",
    corner_radius=20,
    command=lambda: sayı_basmak("3")
)
button3.grid(row=1, column=2, pady=10, padx=10)

button4=ctk.CTkButton(
    window,
    width= 88,
    height=75,
    fg_color="#3c6079",
    hover_color="#60839c",
    text="4",
    corner_radius=20,
    command=lambda: sayı_basmak("4")
)
button4.grid(row=2, column=0, pady=10, padx=10)

button5=ctk.CTkButton(
    window,
    width= 88,
    height=75,
    fg_color="#3c6079",
    hover_color="#60839c",
    text="5",
    corner_radius=20,
    command=lambda: sayı_basmak("5")
)
button5.grid(row=2, column=1, pady=10, padx=10)

button6=ctk.CTkButton(
    window,
    width= 88,
    height=75,
    fg_color="#3c6079",
    hover_color="#60839c",
    text="6",
    corner_radius=20,
    command=lambda: sayı_basmak("6")
)
button6.grid(row=2, column=2, pady=10, padx=10)

button7=ctk.CTkButton(
    window,
    width= 88,
    height=75,
    fg_color="#3c6079",
    hover_color="#60839c",
    text="7",
    corner_radius=20,
    command=lambda: sayı_basmak("7")
)
button7.grid(row=3, column=0, pady=10, padx=10)

button8=ctk.CTkButton(
    window,
    width= 88,
    height=75,
    fg_color="#3c6079",
    hover_color="#60839c",
    text="8",
    corner_radius=20,
    command= lambda: sayı_basmak("8")
)
button8.grid(row=3, column=1, pady=10, padx=10)

button9=ctk.CTkButton(
    window,
    width= 88,
    height=75,
    fg_color="#3c6079",
    hover_color="#60839c",
    text="9",
    corner_radius=20,
    command=lambda: sayı_basmak("9")
)
button9.grid(row=3, column=2, pady=10, padx=10)

button0=ctk.CTkButton(
    window,
    width= 88,
    height=75,
    fg_color="#3c6079",
    hover_color="#60839c",
    text="0",
    corner_radius=20,
    command=lambda: sayı_basmak("0")
)
button0.grid(row=4, column=0, pady=10, padx=10)

#işlem butonlarımız
bölme_butonu=ctk.CTkButton(
    window,
    width= 88,
    height=75,
    fg_color="#3c6079",
    hover_color="#60839c",
    text="÷",
    corner_radius=20,
    command=lambda: işlem_seç("÷")
)
bölme_butonu.grid(row=1, column=3, pady=10, padx=10)

çarpma_butonu=ctk.CTkButton(
    window,
    width= 88,
    height=75,
    fg_color="#3c6079",
    hover_color="#60839c",
    text="x",
    corner_radius=20,
    command=lambda: işlem_seç("x")
)
çarpma_butonu.grid(row=2, column=3, pady=10, padx=10)

toplama_butonu=ctk.CTkButton(
    window,
    width= 88,
    height=75,
    fg_color="#3c6079",
    hover_color="#60839c",
    text="+",
    corner_radius=20,
    command=lambda: işlem_seç("+")
)
toplama_butonu.grid(row=3, column=3, pady=10, padx=10)

çıkarma_butonu=ctk.CTkButton(
    window,
    width= 88,
    height=75,
    fg_color="#3c6079",
    hover_color="#60839c",
    text="-",
    corner_radius=20,
    command=lambda: işlem_seç("-")
)
çıkarma_butonu.grid(row=4, column=3, pady=10, padx=10)

eşittir_butonu=ctk.CTkButton(
    window,
    width= 88,
    height=75,
    fg_color="#3c6079",
    hover_color="#60839c",
    text="=",
    corner_radius=20,
    command=eşittir
)
eşittir_butonu.grid(row=4, column=2, pady=10, padx=10)

c_butonu=ctk.CTkButton(
    window,
    width= 88,
    height=75,
    fg_color="#3c6079",
    hover_color="#60839c",
    text="C",
    corner_radius=20
)
c_butonu.grid(row=4, column=1, pady=10, padx=10)

window.mainloop()