import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog

class TestScoresGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Test Score Averages Report")

        self.top_frame = tkinter.Frame()
        self.mid_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()
        self.result_frame = tkinter.Frame()

        self.num_students_label = tkinter.Label(self.top_frame,
                                                text='Enter number of students in the report(0-10):')
        self.num_students_entry = tkinter.Entry(self.top_frame, width=10)

        self.num_students_label.pack(side='left')
        self.num_students_entry.pack(side='left')

        self.num_scores_label = tkinter.Label(self.mid_frame,
                                              text='Enter number of test scores per student(0-5):')
        self.num_scores_entry = tkinter.Entry(self.mid_frame, width=10)

        self.num_scores_label.pack(side='left')
        self.num_scores_entry.pack(side='left')

        self.scores_read_button = tkinter.Button(self.bottom_frame,
                                                 text='Read Scores',
                                                 command=self.scores_read)
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text='Quit',
                                          command=self.main_window.destroy)

        self.scores_read_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.result_ta = tkinter.Text(self.result_frame, bg='light blue', height=20, width=60)
        self.result_ta.pack()

        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()
        self.result_frame.pack()

        tkinter.mainloop()

    def scores_read(self):
        self.result_ta.delete('1.0', 'end')
        result_string = ""

        num_students = int(self.num_students_entry.get())

        while num_students < 0:
            tkinter.messagebox.showerror("Error", "Number of students can't be negative")
            num_students = int(self.num_students_entry.get())
            return

        num_test_scores = int(self.num_scores_entry.get())

        while num_test_scores < 0:
            tkinter.messagebox.showerror("Error", "Student scores can't be negative")
            num_test_scores = int(self.num_scores_entry.get())
            return

        result_string += f'===Students Test Scores Report==='
        result_string += f'\nNumber of Students: {num_students}'
        result_string += f'\nNumber of Test Scores: {num_test_scores}'
        result_string += '\n=====================================\n'

        for student in range(num_students):
            total = 0.0
            average = 0.0

            for test_num in range(num_test_scores):
                test_score = (simpledialog.askstring(title="Student#" + str(student + 1)
                                                     + ",Test#" + str(test_num + 1) + " Scores",
                                                     prompt="Enter Test Scores: "))
                test_score = float(test_score)
                result_string += (f'\nThe test scores for student#{student + 1}'
                                  f',test#{test_num + 1}'
                                  f' is: {test_score:.1f}')

                total += test_score

            average = total / num_test_scores

            result_string += (f'\nThe average for student#{student + 1}'
                              f' is:{average:.1f}')
            result_string += '\n=====================================\n'

        self.result_ta.insert('1.0', result_string)

my_test_scores = TestScoresGUI()