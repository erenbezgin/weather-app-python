import tkinter as tk
from tkinter import messagebox
import requests
import os
from dotenv import load_dotenv
from datetime import datetime, timezone, timedelta

load_dotenv()


class SkyCastPro:
    def __init__(self, root):
        self.root = root
        self.root.title("SkyCast Pro - Global Weather & Time")
        self.root.geometry("450x600")
        self.root.configure(bg="#0f172a")  # Deep slate blue

        # UI Styling constants
        self.accent_color = "#38bdf8"  # Sky blue
        self.text_color = "#f1f5f9"
        self.card_bg = "#1e293b"

        self.setup_ui()

    def setup_ui(self):
        """Build the interface with a modern card-based layout"""
        # Header Section
        self.header = tk.Label(
            self.root,
            text="SKYCAST PRO",
            font=("Inter", 24, "bold"),
            bg="#0f172a",
            fg=self.accent_color,
        )
        self.header.pack(pady=(30, 10))

        # Search Bar
        self.search_frame = tk.Frame(self.root, bg="#0f172a")
        self.search_frame.pack(pady=10)

        self.city_entry = tk.Entry(
            self.search_frame,
            font=("Inter", 12),
            width=25,
            bg=self.card_bg,
            fg="white",
            bd=0,
            insertbackground="white",
        )
        self.city_entry.pack(side=tk.LEFT, ipady=8, padx=5)
        self.city_entry.insert(0, "Search City...")
        self.city_entry.bind("<FocusIn>", lambda e: self.city_entry.delete(0, tk.END))

        self.btn_search = tk.Button(
            self.search_frame,
            text="FIND",
            command=self.fetch_data,
            bg=self.accent_color,
            fg="#0f172a",
            font=("Inter", 10, "bold"),
            bd=0,
            padx=15,
            cursor="hand2",
        )
        self.btn_search.pack(side=tk.LEFT, ipady=7)

        # Result Card
        self.card = tk.Frame(self.root, bg=self.card_bg, padx=20, pady=20)
        self.card.pack(pady=30, padx=40, fill=tk.BOTH)

        self.lbl_city = tk.Label(
            self.card,
            text="---",
            font=("Inter", 18, "bold"),
            bg=self.card_bg,
            fg=self.accent_color,
        )
        self.lbl_city.pack()

        self.lbl_time = tk.Label(
            self.card,
            text="Local Time: --:--",
            font=("Inter", 11),
            bg=self.card_bg,
            fg="#94a3b8",
        )
        self.lbl_time.pack(pady=(0, 15))

        self.lbl_temp = tk.Label(
            self.card,
            text="--°C",
            font=("Inter", 54, "bold"),
            bg=self.card_bg,
            fg=self.text_color,
        )
        self.lbl_temp.pack()

        self.lbl_desc = tk.Label(
            self.card,
            text="Enter a city to explore",
            font=("Inter", 12),
            bg=self.card_bg,
            fg="#cbd5e1",
        )
        self.lbl_desc.pack(pady=10)

        # Stats Grid
        self.stats_frame = tk.Frame(self.card, bg=self.card_bg)
        self.stats_frame.pack(fill=tk.X, pady=10)

        self.lbl_humidity = tk.Label(
            self.stats_frame, text="Humidity: --", bg=self.card_bg, fg="#94a3b8"
        )
        self.lbl_humidity.pack(side=tk.LEFT, expand=True)

        self.lbl_wind = tk.Label(
            self.stats_frame, text="Wind: -- km/h", bg=self.card_bg, fg="#94a3b8"
        )
        self.lbl_wind.pack(side=tk.LEFT, expand=True)

    def fetch_data(self):
        city = self.city_entry.get().strip()

        api_key = os.getenv("API_KEY")

        if not api_key:
            messagebox.showerror(
                "Error", "API Key not found! Please check your .env file."
            )
            return

        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        try:
            res = requests.get(url)
            data = res.json()

            if data["cod"] == 200:
                # 1. Update Weather Info
                self.lbl_city.config(text=f"{data['name']}, {data['sys']['country']}")
                self.lbl_temp.config(text=f"{round(data['main']['temp'])}°C")
                self.lbl_desc.config(text=data["weather"][0]["description"].upper())
                self.lbl_humidity.config(text=f"Humidity: {data['main']['humidity']}%")
                self.lbl_wind.config(text=f"Wind: {data['wind']['speed']} km/h")

                # 2. Calculate Local Time using timezone offset
                offset = data["timezone"]  # Offset in seconds from UTC
                local_time = datetime.now(timezone.utc) + timedelta(seconds=offset)
                self.lbl_time.config(
                    text=f"Local Time: {local_time.strftime('%H:%M')} ({data['name']})"
                )

            else:
                messagebox.showerror("Error", "Location not found!")
        except Exception as e:
            messagebox.showerror("Error", "Connection failed!")


if __name__ == "__main__":
    app_root = tk.Tk()
    SkyCastPro(app_root)
    app_root.mainloop()
