import tkinter as tk
from tkinter import messagebox
from database.db_untils import login_user
class Login(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.configure(bg = 'white')
        self.create_widgets()
    def create_widgets(self):
        content_frame= tk.Frame(self, bg = "white")
        content_frame.pack(pady =20, fill=tk.BOTH, expand=True)

        tk.Label(content_frame, text="Dang Nhap", font=("Arial", 16, "bold")).grid(row=0, columnspan=2, pady=10)
        tk.Label(content_frame, text="Email:").grid(row=1, column=0, sticky=tk.W)
        self.entry_email = tk.Entry(content_frame)
        self.entry_email.grid(row=1, column=1)

        tk.Label(content_frame, text="Password:").grid(row=2, column=0, sticky=tk.W)
        self.entry_password = tk.Entry(content_frame, show="*")
        self.entry_password.grid(row=2, column=1)
        tk.Button(content_frame, text="Login", command=lambda: self.login()).grid(row=3, columnspan=2, pady=5)
    def login(self):
        email = self.entry_email.get()
        password = self.entry_password.get()
        if not all([email,password]):
            messagebox.showwarning("Input Error", "Please fill out all fields.")
            return

        result = login_user(email,password)
        if result["status"]:
            self.parent.set_user({"email": email})
            messagebox.showinfo("Login Successful!!")
            if result["role"] == "admin":
                self.parent.switch_frame("Admin")
            else: 
                self.parent.switch_frame("Home")
        else:
            messagebox.showwarning("Tài khoản hoặc mật khẩu không đúng!! Vui lòng nhập lại")
        
        