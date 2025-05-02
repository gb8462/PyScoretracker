import tkinter as tk
import openpyxl, os

main = tk.Tk()
main.title('ScoreTracker')
main.geometry('750x400')
main.config(bg='#ced6d6')
# ========== Functions Here ==========

def initialize_database():
    if not os.path.exists("student_scores.xlsx"):
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        sheet.title = "ScoreTracker"
        sheet.append(["studentNames", "studentScores",'grades'])
        sheet.column_dimensions['A'].width = 20
        sheet.column_dimensions['B'].width = 20
        workbook.save("student_scores.xlsx")

def Submit():
    print('Hallooo')

# =========== Title here ==========

title = tk.Label(main, text='ScoreTracker', font=('Arial', 20),bg='#ced6d6')
title.pack(pady=10)

# ========== Frame Here==========
frame = tk.Frame(main,bg='#e9f2f2')
frame.pack(fill='both',expand=True)

studentName = tk.Label(frame, text='Student Name', font=('Arial',12),bg='#e9f2f2')
studentName.pack(pady=(50,2))

entry = tk.Entry(frame)
entry.pack()

score = tk.Label(frame, text='Score', font=('Arial',12), bg='#e9f2f2')
score.pack(pady=(10,2))

entry = tk.Entry(frame)
entry.pack()

submit = tk.Button(frame, text='submit', command=Submit)
submit.pack(pady=20)

# ========== + ==========
initialize_database()
main.mainloop()