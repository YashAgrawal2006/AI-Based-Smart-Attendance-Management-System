# AI-Based Smart Attendance Management System Using Face Recognition

> An intelligent attendance management system that automates student attendance using face recognition and computer vision.

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-5C3EE8?logo=opencv&logoColor=white)](https://opencv.org/)
[![Next.js](https://img.shields.io/badge/Next.js-Frontend-000000?logo=next.js&logoColor=white)](https://nextjs.org/)
[![Flask](https://img.shields.io/badge/Flask-Backend-000000?logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![MongoDB](https://img.shields.io/badge/MongoDB-Database-47A248?logo=mongodb&logoColor=white)](https://www.mongodb.com/)

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
🛠️ Technologies Used
Core Application
Python
OpenCV
Tkinter
NumPy
Pandas
Pillow
pyttsx3
Computer Vision
Haar Cascade Classifiers
Face Detection
Face Recognition
LBPH-based face recognition workflow
Web Application
Next.js
React
TypeScript
Flask
MongoDB

📂 Project Structure
AI-Based-Smart-Attendance-Management-System/
│
├── backend/
│   ├── app.py
│   ├── recognition.py
│   ├── requirements.txt
│   ├── auth/
│   ├── student/
│   └── teacher/
│
├── frontend/
│   ├── app/
│   ├── public/
│   ├── types/
│   ├── package.json
│   └── package-lock.json
│
├── Project Snap/
│   ├── 1.PNG
│   ├── 2.PNG
│   ├── 3.PNG
│   └── ...
│
├── UI_Image/
│
├── attendance.py
├── automaticAttendance.py
├── takeImage.py
├── takemanually.py
├── trainImage.py
├── show_attendance.py
│
├── haarcascade_frontalface_alt.xml
├── haarcascade_frontalface_default.xml
├── requirements.txt
├── project_requirement.txt
├── .env.example
├── .gitignore
└── README.md
🚀 Getting Started
Prerequisites

Make sure the following are installed:

Python 3.9 or later
Node.js
npm
MongoDB (for the web application/backend)
A working webcam for face registration and recognition

🐍 Running the Python Application
1. Clone the repository
git clone https://github.com/YashAgrawal2006/AI-Based-Smart-Attendance-Management-System.git
2. Navigate to the project
cd AI-Based-Smart-Attendance-Management-System
3. Create a virtual environment
python -m venv venv
4. Activate the environment
Windows:
venv\Scripts\activate
5. Install dependencies
pip install -r requirements.txt
6. Run the application
python attendance.py



