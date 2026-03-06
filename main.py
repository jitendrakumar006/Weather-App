import requests
import tkinter as tk
from tkinter import messagebox


API_KEY = "6e9e751a2afb63b6f2762e0390e939a2"   


def get_weather():
    city = city_entry.get()
    
    if city == "":
        messagebox.showwarning("Warning", "Please enter city name!")
        return

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        temp = data["main"]["temp"]
        weather = data["weather"][0]["description"].title()
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]

        result_label.config(
            text=f"{temp}°C",
            font=("Helvetica", 40, "bold")
        )

        info_label.config(
            text=f"{weather}\nHumidity: {humidity}%\nWind Speed: {wind} m/s",
            font=("Helvetica", 14)
        )

    else:
        messagebox.showerror("Error", "City not found!")


root = tk.Tk()
root.title("Modern Weather App")
root.geometry("400x500")
root.resizable(False, False)
root.configure(bg="#1e1e2f")

title_label = tk.Label(root, text="Weather App", 
                       font=("Helvetica", 22, "bold"),
                       bg="#1e1e2f", fg="white")
title_label.pack(pady=20)

city_entry = tk.Entry(root, font=("Helvetica", 14), width=20, justify="center")
city_entry.pack(pady=10)

search_btn = tk.Button(root, text="Search", 
                       font=("Helvetica", 12, "bold"),
                       bg="#4CAF50", fg="white",
                       padx=10, pady=5,
                       command=get_weather)
search_btn.pack(pady=10)

result_label = tk.Label(root, text="", bg="#1e1e2f", fg="white")
result_label.pack(pady=20)

info_label = tk.Label(root, text="", bg="#1e1e2f", fg="white")
info_label.pack()

root.mainloop()