import tkinter as tk

main = tk.Tk()
main.title('ScoreTracker')
main.geometry('500x560')
main.config(bg='#e8e2e1')

title = tk.Label(main, text='Score Tracker', bg='#e8e2e1')
title.pack()

# =================================================
frame = tk.Frame(main, bg='white')
frame.pack()

studentName = tk.Label(frame, text='Student Name', bg='white')
studentName.grid(row = 1, column = 0)

score = tk.Label(frame, text='Student Score', bg='white')
score.grid(row = 1, column = 1)
# =================================================


main.mainloop()