import tkinter as tk
import openpyxl, os

main = tk.Tk()
main.title('ScoreTracker')
main.geometry('750x400')
main.config(bg='#e4eaeb')

# ========== Functions Here ==========
def initialize_database():
    if not os.path.exists("student_scores.xlsx"):
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        sheet.title = "ScoreTracker"
        sheet.append(["studentNames", "studentScores"])
        sheet.column_dimensions['A'].width = 20
        sheet.column_dimensions['B'].width = 20
        workbook.save("student_scores.xlsx")

def Submit():
    print('Hallooo')

# ========== Frame1 Here==========
frame1 = tk.Frame(main,bg='#e4eaeb', borderwidth=1, relief='flat')
frame1.pack(side='left',fill='both')

# =========== Title here ==========
title = tk.Label(frame1, text='ScoreTracker', font=('Arial', 20),bg='#e4eaeb')
title.pack(pady=(20,0))

studentName = tk.Label(frame1, text='Student Name', font=('Arial',12),bg='#e4eaeb')
studentName.pack(pady=(40,2), padx=20)

name_entry = tk.Entry(frame1, width=20,font=('Arial',11))
name_entry.pack(padx=20)

score = tk.Label(frame1, text='Student Score', font=('Arial',12), bg='#e4eaeb')
score.pack(pady=(10,2), padx=20)

score_entry = tk.Entry(frame1, width=20, font=('Arial',11))
score_entry.pack(padx=20)

submit = tk.Button(frame1, text='submit', command=Submit)
submit.pack(pady=20, padx=20)

# ========== Frame2 Here==========
frame2 = tk.Frame(main,bg='#d3dadb', borderwidth=1, relief="sunken",highlightthickness=1)
frame2.pack(padx=10,pady=10,side='right',fill='both',expand=True)


# ========== + ==========

initialize_database()
main.mainloop()