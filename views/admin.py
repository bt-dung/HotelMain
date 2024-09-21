import tkinter as tk

class Admin(tk.Frame):
    def __init__(self, parent, currentUser):
        super().__init__(parent)
        self.info_label = tk.Label(self, text=f"Welcome, {currentUser['email']}", wraplength=300, justify="right")
        self.info_label.pack(pady=20)
        button = tk.Button(self, text="Go to MainPage", command=lambda: parent.switch_frame('Main_menu'))
        button.pack(pady=10)