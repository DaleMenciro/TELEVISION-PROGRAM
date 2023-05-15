import tkinter as tk
from Television import TV

class TV_GUI:
    def __init__(self,master):
        self.master= master
        master.title("Test TV")
        master.geometry("300x200")