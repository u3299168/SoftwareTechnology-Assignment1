import tkinter
class myGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.title("Acceleration Program")
        result = ((10.5 - 5.6) / 0.5)
        self.label1 = tkinter.Label(self.main_window, text = "Result="+str(result))

        self.label1.pack()

        tkinter.mainloop()
my_gui = myGUI()