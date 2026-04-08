import tkinter

class myGUI:
    def __init__(self):
        # Create the main window.
        self.main_window = tkinter.Tk()
        self.main_window.title("Calculator")

        # Create three frames to group widgets.
        self.top_frame = tkinter.Frame()
        self.mid_frame = tkinter.Frame()
        self.button_frame = tkinter.Frame()
        self.result_frame = tkinter.Frame()

        # Create the widgets for the top frame and pack them (a label and a text box)
        num1_label = tkinter.Label(self.top_frame, text="Enter a number1")
        self.num1_entry = tkinter.Entry(self.top_frame, bg='light grey', bd=2, width='10')
        num1_label.pack(side='left')
        self.num1_entry.pack(side='left')

        # Create the widgets for the top frame and pack them (a label and a text box)
        num2_label = tkinter.Label(self.mid_frame, text="Enter a number2")
        self.num2_entry = tkinter.Entry(self.mid_frame, bg='light grey', bd=2, width='10')
        num2_label.pack(side='left')
        self.num2_entry.pack(side='left')

        # Create the widgets for the button frame and pack them (calc button and a quit button)
        calc_button = tkinter.Button(self.button_frame, text="Calculate Sum", command=self.calc_sum)
        quit_button = tkinter.Button(self.button_frame, text='Quit', command=self.main_window.destroy)
        calc_button.pack(side='left')
        quit_button.pack(side='left')

        # Create the widgets for multiline text area widget and pack it
        # (tkinter.Text is a multiline text area)
        self.result_ta = tkinter.Text(self.result_frame, bg='light blue', height=10, width=40)
        self.result_ta.pack()

        self.top_frame.pack()
        self.mid_frame.pack()
        self.button_frame.pack()
        self.result_frame.pack()

        # Enter the tkinter main loop.
        tkinter.mainloop()

    # The calc_sum method is a callback function for
    # the Calculate button.
    def calc_sum(self):
        self.result_ta.delete('1.0', tkinter.END)

        num1 = int(self.num1_entry.get())
        num2 = int(self.num2_entry.get())
        sum = num1 + num2
        self.result_ta.insert('1.0', "the sum of 2 digits is " + str(sum))

my_gui = myGUI()