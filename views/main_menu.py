import tkinter as tk
import tkinter as ttk

class Main_menu(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.header_frame = tk.Frame(self)
        self.header_frame.pack(side=tk.TOP, fill=tk.X)
        
        self.info_label = tk.Label(self, text="", wraplength=300, justify="left")
        self.info_label.pack(pady=20)

        self.btn_home = ttk.Button(self.header_frame, text="Home", command=lambda: parent.switch_frame("Home"))
        self.btn_login = ttk.Button(self.header_frame, text="Login", command=lambda: parent.switch_frame("Login"))
        self.btn_register = ttk.Button(self.header_frame, text="Register", command=lambda: parent.switch_frame("Register"))

        self.btn_home.pack(side=tk.LEFT, padx=10, pady=5)
        self.btn_login.pack(side=tk.LEFT, padx=10, pady=5)
        self.btn_register.pack(side=tk.LEFT, padx=10, pady=5)
        