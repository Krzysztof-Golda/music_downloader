import tkinter as tk
from tkinter import font


class UserInterface(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1600x900")
        self.title("Music Downloader")
        self.main_frame = tk.Frame(master=self, padx=20, pady=30)
        self.main_frame.pack()
        self.create_initial_screen()
        self.urls = []

    def create_initial_screen(self):
        """
            Metoda uruchamiana na początku dziaania programu odpowiedzialna za wybór serwisu
        """
        self.screen_reloader()
        # Informacje o wyborze pobierania
        initial_label_frame = tk.Frame(
            master=self.main_frame, padx=20, pady=30)
        initial_label_frame.pack()
        self.display = tk.Label(master=initial_label_frame,
                                text="Wybierz skąd chcesz poprać muzykę:",
                                font=font.Font(size=20, weight="bold"))
        self.display.pack()

        # Rama przycisków
        initial_btn_frame = tk.Frame(
            master=self.main_frame, padx=10, pady=20, width=200, cursor="hand2", highlightcolor="red", relief=tk.RAISED)
        initial_btn_frame.pack()
        # Przyciski
        self.source_btn = tk.Button(
            master=initial_btn_frame, bg="lightblue", width=5, height=2, text="YT", command=self.create_url_provider)
        self.source_btn.grid(column=0, row=0)

    def create_url_provider(self):
        self.screen_reloader()

        # Miejsce wprowadzania adresu
        self.entry_frame = tk.Frame(master=self.main_frame, padx=30)
        self.entry_frame.grid(column=0, row=0, columnspan=2, sticky="NW")

        self.info_label = tk.Label(
            master=self.entry_frame, text="Wprowadź adres url do filmu:", font=font.Font(size=18, weight="bold"))
        self.info_label.grid(column=0, row=0)

        self.url_entry = tk.Entry(master=self.entry_frame, width=50)
        self.url_entry.grid(column=0, row=1)

        self.add_url_btn = tk.Button(
            master=self.entry_frame, width=2, height=1, text="+", command=lambda: self.add_url_to_list(self.url_entry.get()))
        self.add_url_btn.grid(column=1, row=1)

        # Miejsce wyświetlania dodanych adresów url
        self.diplay_urls_frame = tk.Frame(
            master=self.main_frame, padx=20,)
        self.diplay_urls_frame.grid(column=2, row=0, columnspan=2)

        # Wyświetlanie adresów url
        row_num = 0
        for url in self.urls:
            self.url_label = tk.Label(
                master=self.diplay_urls_frame, text=f"{url}", font=font.Font(size=18, weight="normal"), background="teal", foreground="white")
            self.url_label.grid(column=0, row=row_num, sticky="N", padx=5)
            row_num += 1

        # Przycisk do pobierania
        self.download_btn = tk.Button(master=self.diplay_urls_frame, background="red",
                                      foreground="white", text="Pobierz", font=font.Font(size=20, weight="bold"), command=self.download_music)
        self.download_btn.grid(column=1, row=0, sticky="NE")

    def add_url_to_list(self, url):
        self.urls.append(url)
        self.screen_reloader()
        self.create_url_provider()

    def screen_reloader(self):
        self.main_frame.destroy()
        self.main_frame = tk.Frame(master=self, padx=20, pady=30)
        self.main_frame.pack()

    def download_music(self):
        pass
