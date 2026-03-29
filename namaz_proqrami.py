from tkinter import *
from datetime import datetime
import time
import requests

def get_prayer_times():
    try:
        url = "http://api.aladhan.com/v1/timingsByCity?city=Baku&country=Azerbaijan&method=2"
        response=requests.get(url)
        data=response.json()
        return data['data']['timings']
    except:
        return None


def update_time():
    current_time = datetime.now().strftime("%H:%M:%S")
    time_label.config(text=current_time)
    time_label.after(1000, update_time)
root=Tk()
root.title("Namaz Proqrami")
root.geometry("300x400")
time_label=Label(root, font=("Helvetica", 24))
time_label.pack(pady=20)
update_time()
l=Label(root, text="Namaz vaxtları", font=("Helvetica", 18))
l.pack(pady=20)
l=Label(root, text="(Baku, Azerbaijan)", font=("Helvetica", 12))
l.pack(pady=5)
timings = get_prayer_times()
if timings:
    prayers = {"Fajr": "Sübh", "Dhuhr": "Zöhr", "Asr": "Əsr", "Maghrib": "Məğrib", "Isha": "İşa"}
    for en, az in prayers.items():
        Label(root, text=f"{az}: {timings[en]}", font=("Helvetica", 16)).pack(pady=5)
else:
    Label(root, text="Xəta baş verdi", font=("Helvetica", 14)).pack(pady=20)

root.mainloop()
