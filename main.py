import tkinter as tk
from views.home import Home
from views.login import Login
from views.register import Register
from views.main_menu import Main_menu
from views.admin import Admin

class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("MyApp")
        self.geometry("400x300")
        self.frames = {} 
        self.currentUser = None
        self.switch_frame("Main_menu")

    def switch_frame(self, frame_name):
        new_frame = None        
        if frame_name == "Main_menu":
            new_frame = Main_menu(self)
        elif frame_name =="Home":
            print("main"+ str(self.currentUser))
            new_frame = Home(self,self.currentUser)
        elif frame_name =="Admin":
            new_frame = Admin(self, self.currentUser)
        elif frame_name == "Login":
            new_frame = Login(self)
        elif frame_name == "Register":
            new_frame = Register(self)

        if hasattr(self, "current_frame"):
            self.current_frame.destroy()
        
        self.current_frame = new_frame
        self.current_frame.pack(fill=tk.BOTH, expand=True)
    def set_user(self, user):
        self.currentUser = user

if __name__ == "__main__":
    app = MyApp()
    app.mainloop()
