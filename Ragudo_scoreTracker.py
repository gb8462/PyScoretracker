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
    student_name = name_entry.get()
    student_score = score_entry.get()

    if student_name.strip() == "" or student_score.strip() == "":
        print("Please enter both name and score.")
        return
    try:
        workbook = openpyxl.load_workbook("student_scores.xlsx")
        sheet = workbook.active

        sheet.append([student_name, student_score])
        workbook.save("student_scores.xlsx")
        print("Data saved!")

        name_entry.delete(0, tk.END)
        score_entry.delete(0, tk.END)            
        load_data()
    except Exception as e:
        print("Error saving data:", e)

def load_data():
    try:
        workbook = openpyxl.load_workbook("student_scores.xlsx")
        sheet = workbook.active

        display_box.config(state='normal')
        display_box.delete('1.0', tk.END)  # clear old content

        display_box.insert(tk.END, f"{'Name':<20} | {'Score':<10}\n")
        display_box.insert(tk.END, "-"*32 + "\n")

        for row in sheet.iter_rows(min_row=2, values_only=True):
            name, score = row
            display_box.insert(tk.END, f"{name:<20} | {score:<10}\n")

        display_box.config(state='disabled')

    except Exception as e:
        print("Error loading data:", e)

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

display_box = tk.Text(frame2, font=('Arial', 11), state='disabled', bg='#f5f5f5')
display_box.pack(padx=10, pady=10, fill='both', expand=True)

# ========== + ==========

initialize_database()
main.mainloop()