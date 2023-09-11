import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=671
        height=479
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.configure(bg="lightblue")
        root.resizable(width=False, height=False)

        GLabel_987=tk.Label(root)
        GLabel_987["activebackground"] = "#f80c0c"
        GLabel_987["activeforeground"] = "#132aff"
        ft = tkFont.Font(family='Times',size=22)
        GLabel_987["font"] = ft
        GLabel_987["fg"] = "#000000"
        GLabel_987["justify"] = "center"
        GLabel_987["text"] = "VIRTUAL COMPUTER SYSTEM"
        GLabel_987.place(x=100,y=20,width=437,height=114)

        GButton_752=tk.Button(root)
        GButton_752["bg"] = "#150de8"
        GButton_752["disabledforeground"] = "#6ffc10"
        ft = tkFont.Font(family='Times',size=16)
        GButton_752["font"] = ft
        GButton_752["fg"] = "#ffffff"
        GButton_752["justify"] = "center"
        GButton_752["text"] = "VIRTUAL KEYBOARD"
        GButton_752.place(x=200,y=140,width=255,height=151)
        GButton_752["command"] = self.GButton_752_command

        GButton_577=tk.Button(root)
        GButton_577["bg"] = "#000000"
        ft = tkFont.Font(family='Times',size=16)
        GButton_577["font"] = ft
        GButton_577["fg"] = "#ffffff"
        GButton_577["justify"] = "center"
        GButton_577["text"] = "VIRTUAL VOLUME CONTROL"
        GButton_577.place(x=180,y=310,width=288,height=134)
        GButton_577["command"] = self.GButton_577_command

    def GButton_752_command(self):
        print("command")


    def GButton_577_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
