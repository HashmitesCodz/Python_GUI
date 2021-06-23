from tkinter import*
from tkinter import ttk
import sqlite3
import os
os.system('clear')

class ML_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("500x400+400+150")
        self.root.title("COVID-19 Analysis")
        self.root.resizable(False, False)
        bg_color = "#7857fe"
        
        title = Label(self.root, text = "COVID-19 Analysis", bd = 8, relief = GROOVE, bg = bg_color, fg="white", font = ("times new roman", 25, "bold"), pady = 2).pack(fill = X)
        Label_Frame1 = LabelFrame(self.root, font = ("times new roman", 20, "bold"), fg = "gold", bg = bg_color)
        Label_Frame1.place(x = 0, y = 60, relwidth = 1, height = 345)
        login_lbl = Label(Label_Frame1, text = "Login", bg = bg_color, fg = "white", font = ("times new roman", 20, "bold")).grid(row = 0, column = 2, padx = 70, pady = 5) 
        username_lbl = Label(Label_Frame1, text = "Username", bg = bg_color, fg = "white", font = ("times new roman", 15, "bold")).grid(row = 1, column = 1, padx = 30, pady = 20) 
        username_entry = Entry(Label_Frame1, width = 15, font = "arial 15", bd = 5, relief = SUNKEN).grid(row = 1, column = 2)
        password_lbl = Label(Label_Frame1, text = "Password", bg = bg_color, fg = "white", font = ("times new roman", 15, "bold")).grid(row = 2, column = 1, padx = 30, pady = 20) 
        password_entry = Entry(Label_Frame1, width = 15, font = "arial 15", bd = 5, relief = SUNKEN).grid(row = 2, column = 2)
        
        options = ["admin", "user"]
        global options
        combo = ttk.Combobox(Label_Frame1, font = ("arial", 10), value = options, width = 22, height = 30)
        combo.grid(row = 3, column = 2)
        combo.current(0)
        
        Login_Btn = Button(Label_Frame1, text = "Login", bg = bg_color, bd = 3, fg = "white", pady = 15, width = 20, height = 0, font = "arial 10 bold").grid(row = 4, column = 2, padx = 10, pady = 10)
        
    def connection():
        connection = sqlite3.connect('pythonProject.db')
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Admin")
        
        
    def login()
        
        
        
root = Tk()
object = ML_App(root)
root.mainloop()