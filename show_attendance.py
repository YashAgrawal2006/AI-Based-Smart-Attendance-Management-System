import pandas as pd
from glob import glob
import os
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import csv

def subjectchoose(text_to_speech):

    def calculate_attendance():
        Subject = tx.get().strip()

        if Subject == "":
            text_to_speech('Please enter the subject name.')
            return

        # Correct path
        folder_path = f"Attendance\\{Subject}"

        # Check if subject folder exists
        if not os.path.exists(folder_path):
            messagebox.showerror("Error", f"No folder found for subject: {Subject}")
            return

        # Get all CSV files of that subject
        filenames = glob(f"{folder_path}\\{Subject}*.csv")

        # 🔥 MAIN FIX: Prevent crash if no files found
        if len(filenames) == 0:
            messagebox.showerror("No Data", "No attendance records found for this subject!")
            return

        # Read all CSV files
        df_list = [pd.read_csv(f) for f in filenames]

        # Merge all attendance sheets
        newdf = df_list[0]
        for i in range(1, len(df_list)):
            newdf = newdf.merge(df_list[i], how="outer")

        newdf.fillna(0, inplace=True)
        newdf["Attendance"] = ""

        # Calculate percentage safely
        for i in range(len(newdf)):
            try:
                percentage = int(round(newdf.iloc[i, 2:-1].mean() * 100))
                newdf.at[i, "Attendance"] = str(percentage) + '%'
            except:
                newdf.at[i, "Attendance"] = "0%"

        # Save final attendance file
        final_path = f"{folder_path}\\attendance.csv"
        newdf.to_csv(final_path, index=False)

        # Display in GUI table
        root = tk.Toplevel()
        root.title("Attendance of " + Subject)
        root.configure(background="black")

        with open(final_path) as file:
            reader = csv.reader(file)
            for r, col in enumerate(reader):
                for c, row in enumerate(col):
                    label = tk.Label(
                        root,
                        width=12,
                        height=1,
                        fg="yellow",
                        font=("times", 15, "bold"),
                        bg="black",
                        text=row,
                        relief=RIDGE,
                    )
                    label.grid(row=r, column=c)

        print(newdf)

    # Main Subject Window
    subject = tk.Tk()
    subject.title("Subject...")
    subject.geometry("580x320")
    subject.resizable(0, 0)
    subject.configure(background="black")

    titl = tk.Label(
        subject,
        text="Which Subject of Attendance?",
        bg="black",
        fg="green",
        font=("arial", 25),
    )
    titl.place(x=100, y=12)

    def Attf():
        sub = tx.get().strip()
        if sub == "":
            text_to_speech("Please enter the subject name!!!")
        else:
            folder = f"Attendance\\{sub}"
            if os.path.exists(folder):
                os.startfile(folder)
            else:
                messagebox.showerror("Error", "Subject folder not found!")

    attf = tk.Button(
        subject,
        text="Check Sheets",
        command=Attf,
        bd=7,
        font=("times new roman", 15),
        bg="black",
        fg="yellow",
        height=2,
        width=12,
        relief=RIDGE,
    )
    attf.place(x=360, y=170)

    sub_label = tk.Label(
        subject,
        text="Enter Subject",
        width=10,
        height=2,
        bg="black",
        fg="yellow",
        bd=5,
        relief=RIDGE,
        font=("times new roman", 15),
    )
    sub_label.place(x=50, y=100)

    tx = tk.Entry(
        subject,
        width=15,
        bd=5,
        bg="black",
        fg="yellow",
        relief=RIDGE,
        font=("times", 30, "bold"),
    )
    tx.place(x=190, y=100)

    fill_a = tk.Button(
        subject,
        text="View Attendance",
        command=calculate_attendance,
        bd=7,
        font=("times new roman", 15),
        bg="black",
        fg="yellow",
        height=2,
        width=15,
        relief=RIDGE,
    )
    fill_a.place(x=180, y=170)

    subject.mainloop()
