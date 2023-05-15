import tkinter as tk
from Television import TV

class TV_GUI:
    def __init__(self,master):
        self.master= master
        master.title("Test TV")
        master.geometry("300x200")

root = tk.Tk()
TestTV_GUI = TV_GUI(root)
root.mainloop()