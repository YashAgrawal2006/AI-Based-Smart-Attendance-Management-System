import tkinter as tk
from tkinter import *
import os, cv2
import csv
import numpy as np
from PIL import ImageTk, Image
import pandas as pd
import datetime
import time
import tkinter.ttk as tkk
import tkinter.font as font

haarcasecade_path = "haarcascade_frontalface_default.xml"
trainimagelabel_path = "TrainingImageLabel\\Trainner.yml"
trainimage_path = "TrainingImage"
studentdetail_path = "StudentDetails\\studentdetails.csv"
attendance_path = "Attendance"

# for choose subject and fill attendance
def subjectChoose(text_to_speech):
    def FillAttendance():
        sub = tx.get().strip()  # FIX: remove extra spaces

        if sub == "":
            t = "Please enter the subject name!!!"
            text_to_speech(t)
            return

        try:
            recognizer = cv2.face.LBPHFaceRecognizer_create()
            try:
                recognizer.read(trainimagelabel_path)
            except:
                e = "Model not found, please train model"
                Notifica.configure(
                    text=e,
                    bg="black",
                    fg="yellow",
                    width=33,
                    font=("times", 15, "bold"),
                )
                Notifica.place(x=20, y=250)
                text_to_speech(e)
                return

            facecasCade = cv2.CascadeClassifier(haarcasecade_path)
            df = pd.read_csv(studentdetail_path)
            cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

            font_cv = cv2.FONT_HERSHEY_SIMPLEX
            col_names = ["Enrollment", "Name"]
            attendance = pd.DataFrame(columns=col_names)

            # Run camera for 20 seconds
            start_time = time.time()
            duration = 20

            while True:
                ret, im = cam.read()
                if not ret:
                    break

                gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
                faces = facecasCade.detectMultiScale(gray, 1.2, 5)

                for (x, y, w, h) in faces:
                    Id, conf = recognizer.predict(gray[y:y+h, x:x+w])

                    if conf < 70:
                        ts = time.time()
                        date = datetime.datetime.fromtimestamp(ts).strftime("%Y-%m-%d")
                        timeStamp = datetime.datetime.fromtimestamp(ts).strftime("%H:%M:%S")

                        aa = df.loc[df["Enrollment"] == Id]["Name"].values
                        tt = str(Id) + "-" + str(aa)

                        attendance.loc[len(attendance)] = [Id, aa]

                        cv2.rectangle(im, (x, y), (x + w, y + h), (0, 260, 0), 4)
                        cv2.putText(im, tt, (x, y - 10), font_cv, 0.8, (255, 255, 0), 2)
                    else:
                        cv2.rectangle(im, (x, y), (x + w, y + h), (0, 25, 255), 2)
                        cv2.putText(im, "Unknown", (x, y - 10), font_cv, 0.8, (0, 25, 255), 2)

                if time.time() - start_time > duration:
                    break

                attendance = attendance.drop_duplicates(["Enrollment"], keep="first")
                cv2.imshow("Filling Attendance...", im)

                if cv2.waitKey(30) & 0xFF == 27:
                    break

            # Save attendance
            if len(attendance) == 0:
                text_to_speech("No Face found for attendance")
                cam.release()
                cv2.destroyAllWindows()
                return

            ts = time.time()
            date = datetime.datetime.fromtimestamp(ts).strftime("%Y-%m-%d")
            timeStamp = datetime.datetime.fromtimestamp(ts).strftime("%H-%M-%S")

            attendance[date] = 1
            attendance = attendance.drop_duplicates(["Enrollment"], keep="first")

            # Create subject folder safely
            path = os.path.join(attendance_path, sub)
            if not os.path.exists(path):
                os.makedirs(path)

            fileName = f"{sub}_{date}_{timeStamp}.csv"
            full_path = os.path.join(path, fileName)

            attendance.to_csv(full_path, index=False)

            m = "Attendance Filled Successfully of " + sub
            Notifica.configure(
                text=m,
                bg="black",
                fg="yellow",
                width=33,
                relief=RIDGE,
                bd=5,
                font=("times", 15, "bold"),
            )
            text_to_speech(m)
            Notifica.place(x=20, y=250)

            cam.release()
            cv2.destroyAllWindows()

            # Display attendance in table
            root = tk.Toplevel()
            root.title("Attendance of " + sub)
            root.configure(background="black")

            with open(full_path, newline="") as file:
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
                            relief=tk.RIDGE,
                        )
                        label.grid(row=r, column=c)

        except Exception as e:
            text_to_speech("Error occurred while filling attendance")
            cv2.destroyAllWindows()

    # Subject Window UI
    subject = Tk()
    subject.title("Subject...")
    subject.geometry("580x320")
    subject.resizable(0, 0)
    subject.configure(background="black")

    titl = tk.Label(
        subject,
        text="Enter the Subject Name",
        bg="black",
        fg="green",
        font=("arial", 25),
    )
    titl.place(x=160, y=12)

    Notifica = tk.Label(
        subject,
        text="Attendance filled Successfully",
        bg="yellow",
        fg="black",
        width=33,
        height=2,
        font=("times", 15, "bold"),
    )

    def Attf():
        sub = tx.get().strip()
        if sub == "":
            text_to_speech("Please enter the subject name!!!")
        else:
            folder = os.path.join("Attendance", sub)
            if os.path.exists(folder):
                os.startfile(folder)
            else:
                text_to_speech("No attendance folder found for this subject")

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
        text="Fill Attendance",
        command=FillAttendance,
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
