import tkinter

class myGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Loan Repayment Calculator")

        self.top_frame = tkinter.Frame()
        self.mid_frame = tkinter.Frame()
        self.button_frame = tkinter.Frame()
        self.result_frame = tkinter.Frame()

        self.loanAmount_label = tkinter.Label(self.top_frame, text="Loan Amount(120000.95): ")
        self.loanAmount_entry = tkinter.Entry(self.top_frame, bg='light grey', bd=2, width='20')
        self.loanAmount_label.pack(side='left')
        self.loanAmount_entry.pack(side='left')

        self.numYears_label = tkinter.Label(self.mid_frame, text="Number of Years(5)")
        self.numYears_entry = tkinter.Entry(self.mid_frame, bg='light grey', bd=2, width='20')
        self.numYears_label.pack(side='left')
        self.numYears_entry.pack(side='left')

        self.calc_button = tkinter.Button(self.button_frame, text="Show Loan Repayments", command=self.loan_repay)
        self.quit_button = tkinter.Button(self.button_frame, text='Quit', command=self.main_window.destroy)
        self.clear_button = tkinter.Button(self.button_frame, text='Clear', command=self.clear_text)

        self.calc_button.pack(side='left')
        self.clear_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.result_ta = tkinter.Text(self.result_frame, bg='light blue', height=30, width=80)
        self.result_ta.pack()

        # Pack all the frames.
        self.top_frame.pack()
        self.mid_frame.pack()
        self.button_frame.pack()
        self.result_frame.pack()

        tkinter.mainloop()
        
    # The clear_text method is a callback function calculating clear text button
    def clear_text(self):
        self.result_ta.delete('1.0', 'end')

    # The loan_repay method is a callback function calculating loan repayments button
    def loan_repay(self):
        result = ""
        result += ("{0:<20s}{1:<20s}{2:<20s}".format("Interest Rate", "Monthly Payment", "Total Payment\n"))

        #read the entry textbox data
        loan_amount = float(self.loanAmount_entry.get())

        #read the entry textbox data
        num_years = int(self.numYears_entry.get())

        annualInterestRate = 5.0
        while annualInterestRate <= 8.0:
            monthlyInterestRate = annualInterestRate / 1200
            monthlyPayment = loan_amount * monthlyInterestRate / \
                (1 - (pow(1 / (1 + monthlyInterestRate), num_years * 12)))
            totalPayment = monthlyPayment * num_years * 12

            # Display results
            result += ("\n{0:5.3f}% {1:20,.2f} {2:20,.2f}".format(annualInterestRate, monthlyPayment, totalPayment))
            annualInterestRate += 1.0 / 8

        #insert the result string into the result_text_area widget
        self.result_ta.insert('1.0', result)

my_gui = myGUI()