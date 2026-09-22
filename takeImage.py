import csv
import os, cv2
import numpy as np
import pandas as pd
import datetime
import time


def TakeImage(l1, l2, haarcasecade_path, trainimage_path, message, err_screen, text_to_speech):

    if l1 == "" and l2 == "":
        text_to_speech("Please enter your Enrollment Number and Name.")
        return
    elif l1 == "":
        text_to_speech("Please enter your Enrollment Number.")
        return
    elif l2 == "":
        text_to_speech("Please enter your Name.")
        return

    try:
        cam = cv2.VideoCapture(0)

        # check if camera opened
        if not cam.isOpened():
            text_to_speech("Camera not detected. Please check your webcam.")
            message.configure(text="Camera not detected.")
            return

        detector = cv2.CascadeClassifier(haarcasecade_path)
        Enrollment = l1
        Name = l2
        sampleNum = 0

        directory = f"{Enrollment}_{Name}"
        path = os.path.join(trainimage_path, directory)

        # Create directory if not exists
        os.makedirs(path, exist_ok=True)

        while True:
            ret, img = cam.read()
            if not ret:
                continue

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5)

            # Draw rectangle around face
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

                sampleNum += 1

                # FIXED: save image path properly
                save_path = os.path.join(
                    path,
                    f"{Name}_{Enrollment}_{sampleNum}.jpg"
                )

                cv2.imwrite(save_path, gray[y:y+h, x:x+w])

            # ALWAYS show camera feed (IMPORTANT)
            cv2.imshow("Camera - Press Q to Exit", img)

            # press q to exit
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

            # take 50 images max
            if sampleNum >= 50:
                break

        cam.release()
        cv2.destroyAllWindows()

        # Save student record
        row = [Enrollment, Name]
        with open("StudentDetails/studentdetails.csv", "a+", newline="") as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)

        res = f"Images Saved for ER No: {Enrollment} Name: {Name}"
        message.configure(text=res)
        text_to_speech(res)

    except Exception as e:
        text_to_speech("Something went wrong while saving images.")
        print("Error:", e)
