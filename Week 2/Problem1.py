import tkinter
class myGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Welcome Program")
        self.label1 = tkinter.Label(self.main_window, text = "Welcome to Python")
        self.label2 = tkinter.Label(self.main_window, text = "Welcome to Computer Science")
        self.label3 = tkinter.Label(self.main_window, text = "Programming is fun")
        self.label1.pack()
        self.label2.pack()
        self.label3.pack()

        tkinter.mainloop()

my_gui = myGUI()