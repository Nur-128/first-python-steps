#kütüphanelerimiz
import customtkinter as ctk
from datetime import datetime

#penceremiz
window=ctk.CTk()
window.title("saat")
window.geometry("943x337")
window._set_appearance_mode("dark")

#saati yenilemek kullandığımız function
def saati_yenile():
    saat= datetime.now().strftime("%H:%M:%S")
    time_label.configure(text=saat)
    window.after(1000, saati_yenile)

#saat gel artık oğlim
time_label=ctk.CTkLabel(
    window,
    text="00:00:00",font=("Arial", 100) )

time_label.pack(expand=True)#tam ortaya yerleştirmek için

#uygulamayı açık tutmak içim

saati_yenile()
window.mainloop()