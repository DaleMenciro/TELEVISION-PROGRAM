import tkinter as tk
from Television import TV

class TV_GUI:
    def __init__(self,master):
        self.master= master
        master.title("Test TV")
        master.geometry("300x200")

        self.primary_color = "#264653"
        self.secondary_color = "#2a9d8f"
        self.highlight_color = "#e9c46a"

        #Two TV objects
        self.TV_1 = TV()
        self.TV_2 = TV()

root = tk.Tk()
TestTV_GUI = TV_GUI(root)
root.mainloop()