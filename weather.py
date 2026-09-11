#kürtüphanelerimizimportcustomasctimp#apı kısmısı
import customtkinter as ctk
import requests
site = "https://api.open-meteo.com/v1/forecast?latitude=37.07&longitude=37.38&current=temperature_2m,relative_humidity_2m,wind_speed_10m,weather_code"
response = requests.get(site)
veri = response.json()

sicaklik = veri["current"]["temperature_2m"]
nem= veri["current"]["relative_humidity_2m"]
rüzgar=veri["current"]["wind_speed_10m"]
hava_kodu=veri["current"]["weather_code"]

#hava durumunu kont etmek
if hava_kodu==0:
    durum="☀ açık"
elif hava_kodu in [1,2,3]:
    durum="⛅ bulutlu"
elif hava_kodu in[51,53,55,61,63,65]:
    durum="🌧 yağmurlu"
elif hava_kodu in [71,73,75]:
    durum="❄ karlı"
else:
    durum="🌦 değişken"

#penceremiz
window=ctk.CTk()
window.title("Hava Durumu")
window.geometry("918x304")
window._set_appearance_mode("light")

#column row düzeni
for i in range(4):
    window.grid_columnconfigure(i, weight=1)

for i in range(2):
    window.grid_rowconfigure(i, weight=1)
#üstteki labeller 
sıcaklık_labeli=ctk.CTkLabel(
    master=window,
  text="sıcaklık",
  font=("arial", 24),
  text_color="#33022f"
)
sıcaklık_labeli.grid(row=0, column=0, pady=10, padx=10)

hava_labeli=ctk.CTkLabel(
    master=window,
  text="hava durumu",
  font=("arial", 24),
  text_color="#33022f"
)
hava_labeli.grid(row=0, column=1, pady=10, padx=10)

nem_labeli=ctk.CTkLabel(
    master=window,
  text="nem",
  font=("arial", 24),
  text_color="#33022f"
)
nem_labeli.grid(row=0, column=2, pady=10, padx=10)

rüzgar_labeli=ctk.CTkLabel(
    master=window,
  text="rüzgar",
  font=("arial", 24),
  text_color="#33022f"
)
rüzgar_labeli.grid(row=0, column=3, pady=10, padx=10)

#alttaki durum labellerı
rüzgar_durum=ctk.CTkLabel(
    master=window,
  text=f"{rüzgar} km/h",
  font=("arial", 24),
  text_color="#33022f"
)
rüzgar_durum.grid(row=1, column=3, pady=10, padx=10)

nem_durum=ctk.CTkLabel(
    master=window,
  text=f"%{nem}",
  font=("arial", 24),
  text_color="#33022f"
)
nem_durum.grid(row=1, column=2, pady=10, padx=10)

hava_durum=ctk.CTkLabel(
    master=window,
  text=durum,
  font=("arial", 24),
  text_color="#33022f"
)
hava_durum.grid(row=1, column=1, pady=10, padx=10)

sıcaklık_durum=ctk.CTkLabel(
  master=window,
  text=f"{sicaklik}°C",
  font=("arial", 24),
  text_color="#33022f"
)
sıcaklık_durum.grid(row=1, column=0, pady=10, padx=10)

window.mainloop()