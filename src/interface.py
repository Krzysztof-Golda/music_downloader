import tkinter as tk
from tkinter import font, messagebox, ttk
import yt_downloader


class Interface(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1600x900")
        self.title("Music downloader")
        self.main_frame = ttk.Frame(master=self, padding=20)
        self.main_frame.grid(column=0, row=0)
        self.urls = []
        self.media_type = tk.StringVar(value="music")
        self.create_download_screen()

    def create_download_screen(self):
        """
            Creating downloading screen
        """

        # Left side of download interface
        left_frame = ttk.Frame(master=self.main_frame)
        left_frame.grid(column=0, row=0)

        # Url provide field
        enter_frame = ttk.Frame(master=left_frame, padding=(10, 10))
        enter_frame.grid(column=0, row=0, columnspan=3)

        info_label = ttk.Label(
            master=enter_frame, text="Wprowadź adres url:", font=font.Font(size=16, weight="bold"), padding=(20, 0))
        info_label.grid(column=0, row=0, sticky=("NW"))

        url_entry = ttk.Entry(master=enter_frame, width=40)
        url_entry.grid(column=1, row=0)

        url_add_btn = ttk.Button(master=enter_frame, text="+",
                                 width=3, command=lambda: self.add_url(url_entry.get()))
        url_add_btn.grid(column=2, row=0)

        # Radiobutton media-type field
        type_media_frame = ttk.Frame(master=self.main_frame, padding=(30, 10))
        type_media_frame.grid(column=3, row=0)

        music_media_radio = ttk.Radiobutton(
            master=type_media_frame, text="Muzyka", variable=self.media_type, value="music")
        music_media_radio.grid(column=0, row=0, sticky=("W"))

        video_media_radio = ttk.Radiobutton(
            master=type_media_frame, text="Film", variable=self.media_type, value="video")
        video_media_radio.grid(column=0, row=1, sticky=("W"))

        # Right side of download interface
        right_frame = ttk.Frame(master=self.main_frame)
        right_frame.grid(column=4, row=0)

        for url_index, url in enumerate(self.urls):
            displayed_url_frame = ttk.Frame(
                master=right_frame, padding=(10, 3), name=f"{url_index}")
            displayed_url_frame.grid(column=0, row=url_index, columnspan=2)

            displayed_url = ttk.Label(
                master=displayed_url_frame, text=f"URL - {url_index + 1}: {url[12:]}", font=font.Font(size=10), width=40)
            displayed_url.grid(column=0, row=url_index, sticky="W")

            delete_url_btn = ttk.Button(
                master=displayed_url_frame, text="Usuń", width=10, command=lambda frame=displayed_url_frame: self.destroy_frame(frame))
            delete_url_btn.grid(column=1, row=url_index, sticky="E")

        download_btn = ttk.Button(
            master=right_frame, text="Pobierz", width=10, command=self.download_file)
        download_btn.grid(column=3, row=0, columnspan=1)

    def reload(self):
        """Recreate window"""
        self.main_frame.destroy()
        self.main_frame = ttk.Frame(master=self, padding=20)
        self.main_frame.grid(column=0, row=0)
        self.create_download_screen()

    def add_url(self, url):
        """Add url to list"""
        self.urls.append(url)
        self.reload()

    def destroy_frame(self, element):
        url_to_delete = str(element) + ""
        element.destroy()
        self.urls.pop(int(url_to_delete[-1]))

        self.reload()

    def download_file(self):
        """Invoke youtbe donload function from pytube libary"""
        # Guard from empty url
        for url in self.urls:
            if url == '':
                messagebox.showwarning(
                    message="Puste adresy url zostaną pominięte")
                self.urls.remove('')
                self.reload()

        # Check radiobutton media type
        if self.media_type.get() == "music":
            try:
                yt_downloader.download_mp3(self.urls)
            except Exception:
                messagebox.showerror(
                    message="Coś poszło nie tak. Możliwe, że adres url jest nieprawidłowy.")
        elif self.media_type.get() == "video":
            try:
                yt_downloader.download_video(self.urls)
            except Exception:
                messagebox.showerror(
                    message="Coś poszło nie tak. Możliwe, że adres url jest nieprawidłowy.")
