# Loan Qualifier GUI - 1
import tkinter

class myGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Loan Qualifier")

        self.top_frame = tkinter.Frame()
        self.mid_frame = tkinter.Frame()
        self.button_frame = tkinter.Frame()
        self.result_frame = tkinter.Frame()

        salary_label = tkinter.Label(self.top_frame, text="Your Salary")
        self.salary_entry = tkinter.Entry(self.top_frame, bg='light grey', bd=2, width='10')
        salary_label.pack(side='left')
        self.salary_entry.pack(side='left')

        years_label = tkinter.Label(self.mid_frame, text="Years on Job")
        self.years_entry = tkinter.Entry(self.mid_frame, bg='light grey', bd=2, width='10')
        years_label.pack(side='left')
        self.years_entry.pack(side='left')

        calc_button = tkinter.Button(self.button_frame, text="Calculate", command=self.calc_loan)
        quit_button = tkinter.Button(self.button_frame, text='Quit', command=self.main_window.destroy)
        calc_button.pack(side='left')
        quit_button.pack(side='left')

        self.result_ta = tkinter.Text(self.result_frame, bg='light blue', height=20, width=60)
        self.result_ta.pack()

        self.top_frame.pack()
        self.mid_frame.pack()
        self.button_frame.pack()
        self.result_frame.pack()

        tkinter.mainloop()

    def calc_loan(self):
        result_string = ""
        self.result_ta.delete('1.0', tkinter.END)

        salary = float(self.salary_entry.get())
        years_on_job = int(self.years_entry.get())

        MIN_SALARY = 30000.0
        MIN_YEARS = 2

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

        self.result_ta.insert('1.0', result_string)

my_gui = myGUI()