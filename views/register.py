import tkinter as tk
from tkinter import messagebox

from database.db_untils import register_user 

class Register(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.configure(bg="white")
        self.create_widgets()
    def create_widgets(self):
        tk.Label(self, text="Đăng ký", font=("Arial", 16, "bold")).grid(row=0, columnspan=2, pady=10)
        tk.Label(self, text="Name:").grid(row=1, column=0, sticky=tk.W)
        self.entry_name = tk.Entry(self)
        self.entry_name.grid(row=1, column=1)

        tk.Label(self, text="Email:").grid(row=2, column=0, sticky=tk.W)
        self.entry_email = tk.Entry(self)
        self.entry_email.grid(row=2, column=1)

        tk.Label(self, text="Address:").grid(row=3, column=0, sticky=tk.W)
        self.entry_address = tk.Entry(self)
        self.entry_address.grid(row=3, column=1)

        tk.Label(self, text="Gender:").grid(row=4, column=0, sticky=tk.W)
        self.var_gender = tk.StringVar()
        tk.Radiobutton(self, text="Male", variable=self.var_gender, value="Male").grid(row=4, column=1, sticky=tk.W)
        tk.Radiobutton(self, text="Female", variable=self.var_gender, value="Female").grid(row=4, column=1)

        tk.Label(self, text="Phone:").grid(row=5, column=0, sticky=tk.W)
        self.entry_phone = tk.Entry(self)
        self.entry_phone.grid(row=5, column=1)

        tk.Label(self, text="Password:").grid(row=6, column=0, sticky=tk.W)
        self.entry_password = tk.Entry(self, show="*")
        self.entry_password.grid(row=6, column=1)

        tk.Label(self, text="Role:").grid(row=7, column=0, sticky=tk.W)
        self.var_role = tk.StringVar()
        tk.Radiobutton(self, text="User", variable=self.var_role, value="user").grid(row=7, column=1, sticky=tk.W)
        tk.Radiobutton(self, text="Admin", variable=self.var_role, value="admin").grid(row=7, column=1)

        tk.Button(self, text="Register", command=lambda: [self.register(), self.parent.switch_frame("Login")]).grid(row=8, columnspan=2, pady=10)
    def register(self):
        name = self.entry_name.get()
        email = self.entry_email.get()
        address = self.entry_address.get()
        gender = self.var_gender.get()
        phone = self.entry_phone.get()
        password = self.entry_password.get()
        role = self.var_role.get()

        if not all([name, email, address, gender, phone, password, role]):
            messagebox.showwarning("Input Error", "Please fill out all fields.")
            return

        register_user(name, email, address, gender, phone, password, role)
        messagebox.showinfo("Success", "Registration successful!")


