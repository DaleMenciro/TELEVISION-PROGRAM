import tkinter as tk
from Television import TV

class TV_GUI:
    def __init__(self,master):
        self.master= master
        master.title("Test TV")
        master.geometry("300x100")

        self.primary_color = "#264653"
        self.secondary_color = "#2a9d8f"
        self.highlight_color = "#e9c46a"

        #Two TV objects
        self.TV_1 = TV()
        self.TV_2 = TV()

        #Setting TV1 channel and volume level
        self.TV_1.set_channel(30)
        self.TV_1.set_volume(3)

        #Setting TV2 channel and volume level
        self.TV_2.set_channel(3)
        self.TV_2.set_volume(2)

        #Create label to display the channel and volume level of TV 1 and TV 2
        self.TV_1_label = tk.Label(master, text=f"TV1's channel is {self.TV_1.get_channel()} and volume level is {self.TV_1.get_volume()}", bg=self.primary_color, fg= "white")
        self.TV_1_label.pack(pady=10)

        self.TV_2_label = tk.Label(master, text=f"TV2's channel is {self.TV_2.get_channel()} and volume level is {self.TV_2.get_volume()}", bg=self.secondary_color, fg= "white")
        self.TV_2_label.pack(pady=10)

        #Configure background color and font style
        master.configure(bg= self.highlight_color)
        for widget in master.winfo_children():
            widget.configure(font=("Helvetica",12))

root = tk.Tk()
TestTV_GUI = TV_GUI(root)
root.mainloop()