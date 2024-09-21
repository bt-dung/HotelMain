import tkinter as tk
import tkinter as ttk

class Home(tk.Frame):
    def __init__(self, parent, currentUser):
        super().__init__(parent)
        print("home:" + str(currentUser))
        self.currentUser = currentUser
        self.header_frame = tk.Frame(self)
        self.header_frame.pack(side=tk.TOP, fill=tk.X)

        self.info_label = tk.Label(self, text=f"Welcome, {self.currentUser['email']}", wraplength=300, justify="right")
        self.info_label.pack(pady=20)

        self.btn_home = ttk.Button(self.header_frame, text="Home", command=lambda: parent.switch_frame("Home"))
        self.btn_login = ttk.Button(self.header_frame, text="Cart", command=lambda: parent.switch_frame("Cart"))
        self.btn_logout = ttk.Button(self.header_frame, text="Logout", command=lambda: parent.switch_frame("Main_menu"))
        self.label_user = tk.Label(self.header_frame, text=str(self.currentUser['email']))

        self.btn_home.pack(side=tk.LEFT, padx=10, pady=5)
        self.btn_login.pack(side=tk.LEFT, padx=10, pady=5)
        self.btn_logout.pack(side=tk.RIGHT, padx=10, pady=5)
        self.label_user.pack(side=tk.RIGHT, padx=5, pady=5)
