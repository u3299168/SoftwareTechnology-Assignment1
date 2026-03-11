#Loan Qualifier GUI - 1
import tkinter
class myGUI:
    def __init__(self):
        # Create the main window.
        self.main_window = tkinter.Tk()
        self.main_window.title("Loan Qualifier")
        # Create three frames to group widgets.
        self.top_frame = tkinter.Frame()
        self.mid_frame = tkinter.Frame()
        self.button_frame = tkinter.Frame()
        self.result_frame = tkinter.Frame()
        # Create the widgets for the top frame and pack them( a label and a text box)
        salary_label = tkinter.Label(self.top_frame, text="Your Salary")
        self.salary_entry = tkinter.Entry(self.top_frame, bg='light grey', bd=2, width='10')
        salary_label.pack(side='left')
        self.salary_entry.pack(side='left')
        # Create the widgets for the middle frame and pack them( a label and a text box)
        years_label = tkinter.Label(self.mid_frame, text="Years on Job")
        self.years_entry = tkinter.Entry(self.mid_frame, bg='light grey', bd=2, width='10')
        years_label.pack(side='left')
        self.years_entry.pack(side='left')
        # Create the widgets for the button frame and pack them( calc button and a quit button)
        calc_button = tkinter.Button(self.button_frame, text="Calculate",
                                     command=self.calc_loan)
        quit_button = tkinter.Button(self.button_frame, text='Quit',
                                     command=self.main_window.destroy)
        calc_button.pack(side='left')
        quit_button.pack(side='left')
        # Create the widgets for multiline text area widget and pack it(
        # tkinter.Text is a multiline text area)
        self.result_ta = tkinter.Text(self.result_frame, bg='light blue',
                                      height=20, width=60)
        self.result_ta.pack()
        # Pack all the frames.
        self.top_frame.pack()
        self.mid_frame.pack()
        self.button_frame.pack()
        self.result_frame.pack()
        # Enter the tkinter main loop.
        tkinter.mainloop()

    # The calc_sum method is a callback function for
    # the Calculate button.
    def calc_loan(self):
        result_string = ""
        self.result_ta.delete('1.0', tkinter.END)
        salary = float(self.salary_entry.get()) #read the entry textbox data
        years_on_job = int(self.years_entry.get()) #read the entry textbox data
        MIN_SALARY = 30000.0 # The minimum annual salary
        MIN_YEARS = 2 # The minimum years on the job
        # Determine whether the customer qualifies.
        if salary >= MIN_SALARY:
            if years_on_job >= MIN_YEARS:
                result_string += 'You qualify for the loan.'
            else:
                result_string += (f'You must have been employed '
                                  f'for at least {MIN_YEARS} '
                                  f'years to qualify.')
        else:
            result_string += (f'You must earn at least $'
                              f'{MIN_SALARY:,.2f} '
                              f'per year to qualify.')
        #insert the result string into the result_text_area widget
        self.result_ta.insert('1.0', result_string)

my_gui = myGUI()


# Loan qualifier GUI
# Graphical User Interface Program with an info dialog box widget for displaying output
import tkinter
import tkinter.messagebox
class myGUI:
    def __init__(self):
        # Create the main window.
        self.main_window = tkinter.Tk()
        self.main_window.title("Loan Qualifier")
        # Create three frames to group widgets.
        self.top_frame = tkinter.Frame()
        self.mid_frame = tkinter.Frame()
        self.button_frame = tkinter.Frame()
        # Create the widgets for the top frame and pack them( a label and a text box)
        salary_label = tkinter.Label(self.top_frame, text="Your Salary")
        self.salary_entry = tkinter.Entry(self.top_frame, bg='light grey', bd=2, width='10')
        salary_label.pack(side='left')
        self.salary_entry.pack(side='left')
        # Create the widgets for the middle frame and pack them( a label and a text box)
        years_label = tkinter.Label(self.mid_frame, text="Years on Job")
        self.years_entry = tkinter.Entry(self.mid_frame, bg='light grey', bd=2, width='10')
        years_label.pack(side='left')
        self.years_entry.pack(side='left')
        # Create the widgets for the button frame and pack them( calc button and a quit button)
        calc_button = tkinter.Button(self.button_frame, text="Calculate",
                                     command=self.calc_loan)
        quit_button = tkinter.Button(self.button_frame, text='Quit',
                                     command=self.main_window.destroy)
        calc_button.pack(side='left')
        quit_button.pack(side='left')
        # Pack all the frames.
        self.top_frame.pack()
        self.mid_frame.pack()
        self.button_frame.pack()
        # Enter the tkinter main loop.
        tkinter.mainloop()

    # The calc_sum method is a callback function for
    # the Calculate button.
    def calc_loan(self):
        result_string = ""
        salary = float(self.salary_entry.get()) #read the entry textbox data
        years_on_job = int(self.years_entry.get()) #read the entry textbox data
        MIN_SALARY = 30000.0 # The minimum annual salary
        MIN_YEARS = 2 # The minimum years on the job
        # Determine whether the customer qualifies.
        if salary >= MIN_SALARY:
            if years_on_job >= MIN_YEARS:
                result_string += 'You qualify for the loan.'
            else:
                result_string += (f'You must have been employed '
                                  f'for at least {MIN_YEARS} '
                                  f'years to qualify.')
        else:
            result_string += (f'You must earn at least $'
                              f'{MIN_SALARY:,.2f} '
                              f'per year to qualify.')
        #insert the result string into the result_text_area widget
        # Display the results in an info dialog box.
        tkinter.messagebox.showinfo("loaninfo", result_string)

my_gui = myGUI()


#Loan Qualifier Program
# Graphical User Interface Program with a label as widget for displaying output
import tkinter
class myGUI:
    def __init__(self):
        # Create the main window.
        self.main_window = tkinter.Tk()
        self.main_window.title("Loan Qualifier")
        # Create three frames to group widgets.
        self.top_frame = tkinter.Frame()
        self.mid_frame = tkinter.Frame()
        self.button_frame = tkinter.Frame()
        self.result_frame = tkinter.Frame()
        # Create the widgets for the top frame and pack them( a label and a text box)
        salary_label = tkinter.Label(self.top_frame, text="Your Salary")
        self.salary_entry = tkinter.Entry(self.top_frame, bg='light grey', bd=2, width='10')
        salary_label.pack(side='left')
        self.salary_entry.pack(side='left')
        # Create the widgets for the middle frame and pack them( a label and a text box)
        years_label = tkinter.Label(self.mid_frame, text="Years on Job")
        self.years_entry = tkinter.Entry(self.mid_frame, bg='light grey', bd=2, width='10')
        years_label.pack(side='left')
        self.years_entry.pack(side='left')
        # Create the widgets for the button frame and pack them( calc button and a quit button)
        calc_button = tkinter.Button(self.button_frame, text="Calculate",
                                     command=self.calc_loan)
        quit_button = tkinter.Button(self.button_frame, text='Quit',
                                     command=self.main_window.destroy)
        calc_button.pack(side='left')
        quit_button.pack(side='left')
        # We first need a StringVar object (callback variable) to associate with
        # an result label. Use the object's set method
        # to store a string of blank characters.
        self.value = tkinter.StringVar()
        # Then create a result label and associate it with the
        # StringVar object. Any value stored in the
        # StringVar object will automatically be displayed
        # in the label.
        self.result_label = tkinter.Label(self.result_frame,
                                          textvariable=self.value)
        self.result_label.pack()
        # Pack all the frames.
        self.top_frame.pack()
        self.mid_frame.pack()
        self.button_frame.pack()
        self.result_frame.pack()
        # Enter the tkinter main loop.
        tkinter.mainloop()

    # The calc_sum method is a callback function for
    # the Calculate button.
    def calc_loan(self):
        result_string = ""
        salary = float(self.salary_entry.get()) #read the entry textbox data
        years_on_job = int(self.years_entry.get()) #read the entry textbox data
        MIN_SALARY = 30000.0 # The minimum annual salary
        MIN_YEARS = 2 # The minimum years on the job
        # Determine whether the customer qualifies.
        if salary >= MIN_SALARY:
            if years_on_job >= MIN_YEARS:
                result_string += 'You qualify for the loan.'
            else:
                result_string += (f'You must have been employed '
                                  f'for at least {MIN_YEARS} '
                                  f'years to qualify.')
        else:
            result_string += (f'You must earn at least $'
                              f'{MIN_SALARY:,.2f} '
                              f'per year to qualify.')
        #insert the result string into the result_label widget callback variable(value)
        self.value.set(result_string)

my_gui = myGUI()
