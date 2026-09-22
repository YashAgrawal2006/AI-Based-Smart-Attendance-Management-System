# AI-Based Smart Attendance Management System Using Face Recognition

> An intelligent attendance management system that automates student attendance using face recognition and computer vision.

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-5C3EE8?logo=opencv&logoColor=white)](https://opencv.org/)

---

## 📌 Overview

The **AI-Based Smart Attendance Management System** is a face-recognition-based attendance solution developed to automate the process of recording student attendance.

Instead of relying completely on manual attendance, the system captures and recognizes student faces and records attendance digitally.

The project combines **computer vision, face recognition, Python, a web-based frontend, and a backend API** to provide an integrated attendance management solution.

---

## 🎯 Objectives

The main objectives of this project are to:

- Automate the student attendance process.
- Reduce the effort involved in manual attendance.
- Identify registered students using facial recognition.
- Maintain attendance records digitally.
- Provide an easy-to-use interface for attendance management.
- Demonstrate the practical application of computer vision and AI concepts.

---

## ✨ Key Features

### 👨‍🎓 Student Management

- Register students using enrollment details.
- Store student information.
- Capture student face images through a camera.
- Train the face recognition model using registered faces.

### 🤖 Face Recognition

- Detect faces using computer vision.
- Recognize registered students.
- Use trained facial data for attendance identification.
- Automate attendance marking based on recognized faces.

### 📋 Attendance Management

- Mark attendance automatically.
- Support subject-based attendance.
- Provide manual attendance functionality.
- View attendance records.
- Maintain attendance data digitally.

### 🖥️ User Interface

- Desktop-based graphical interface using Tkinter.
- Web-based frontend built using Next.js.
- Backend API implemented using Flask.
- Separate student and teacher-oriented workflows.

---

## 🧠 How the System Works

```text
                    ┌──────────────────────┐
                    │   Student Registration│
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Capture Face Images │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Train Face Recognition│
                    │       Model          │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    Start Attendance  │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Detect & Recognize  │
                    │       Face            │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Mark Attendance    │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │  Attendance Records  │
                    └──────────────────────┘

#📁 Project Structure
AI-Based-Smart-Attendance-Management-System/
│
├── backend/
│   ├── app.py
│   ├── recognition.py
│   ├── requirements.txt
│   │
│   ├── auth/
│   │   └── routes.py
│   │
│   ├── student/
│   │   ├── __init__.py
│   │   ├── demo_session.py
│   │   ├── registration.py
│   │   ├── updatedetails.py
│   │   └── view_attendance.py
│   │
│   └── teacher/
│       ├── __init__.py
│       └── attendance_records.py
│
├── frontend/
│   ├── app/
│   │   ├── components/
│   │   ├── signin/
│   │   ├── signup/
│   │   ├── student/
│   │   └── teacher/
│   │
│   ├── public/
│   ├── types/
│   ├── package.json
│   ├── package-lock.json
│   └── tsconfig.json
│
├── Project Snap/
│   ├── 1.PNG
│   ├── 2.PNG
│   ├── 3.PNG
│   ├── 4.PNG
│   ├── 5.PNG
│   ├── 6.PNG
│   ├── 7.PNG
│   └── 8.PNG
│
├── UI_Image/
│   ├── 0001.png
│   ├── 0002.png
│   ├── 0003.png
│   ├── 0004.png
│   ├── attendance.png
│   ├── register.png
│   └── verifyy.png
│
├── attendance.py
├── automaticAttendance.py
├── takeImage.py
├── trainImage.py
├── show_attendance.py
├── takemanually.py
├── haarcascade_frontalface_alt.xml
├── haarcascade_frontalface_default.xml
├── requirements.txt
├── project_requirement.txt
├── .gitignore
├── .env.example
└── README.md

#👨‍💻 Author
Yash Agrawal

B.Tech — Computer Science & Engineering

GitHub:
https://github.com/YashAgrawal2006

###⭐ Support

If you find this project useful or interesting, consider giving the repository a ⭐ on GitHub.

