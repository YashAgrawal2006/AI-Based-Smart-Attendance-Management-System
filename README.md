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

🌐 Web Application

The modern web application is divided into student and teacher workflows.

Student Routes
/signin
/signup
/student/registrationform
/student/updatedetails
/student/demo-session
/student/view-attendance
Student functionality
Account registration.
Login.
Student registration.
Face capture.
Face recognition demonstration.
Profile updates.
Attendance viewing.
Attendance export.
Teacher Routes
/teacher/dashboard
/teacher/start-session
/teacher/updatedetails
Teacher functionality
Teacher dashboard.
Student management.
Start attendance session.
Live attendance recognition.
Attendance records.
Teacher profile management.
⚙️ Backend API

The Flask backend provides APIs for authentication, student management, face recognition and attendance management.

Examples of attendance-related operations include:

POST /api/attendance/create_session
POST /api/attendance/real-mark
POST /api/attendance/end_session
GET  /api/attendance/models/status
GET  /api/attendance
GET  /api/attendance/export

The face recognition demonstration communicates with the backend through the recognition API.

⚡ Performance Considerations

The modern recognition implementation includes mechanisms for managing face-recognition models and embeddings.

The backend includes:

Model management.
Model initialization and warm-up.
Student embedding handling.
Embedding caching.
Attendance embedding caching.

Caching helps avoid unnecessary repeated processing of the same student embeddings during recognition and attendance operations.

📁 Project Structure
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
📸 Screenshots

The repository contains screenshots demonstrating different parts of the application.

Project Screenshots

🛠️ Installation
1. Clone the Repository
git clone https://github.com/YashAgrawal2006/AI-Based-Smart-Attendance-Management-System.git

Move into the project directory:

cd AI-Based-Smart-Attendance-Management-System
🐍 Desktop Application Setup

Create a Python virtual environment:

python -m venv venv

Activate it:

.\venv\Scripts\activate

Install the required packages:

pip install -r requirements.txt

Run the desktop application:

python attendance.py
🔧 Backend Setup

Navigate to the backend directory:

cd backend

Create a virtual environment:

python -m venv venv

Activate it:

.\venv\Scripts\activate

Install backend dependencies:

pip install -r requirements.txt

Configure the required environment variables using the provided .env.example file.

Start the Flask backend:

python app.py
🌐 Frontend Setup

Open another terminal and navigate to the frontend directory:

cd frontend

Install dependencies:

npm install

Start the development server:

npm run dev

The Next.js application will be available at the local development URL displayed in the terminal.

🔐 Environment Variables

Sensitive configuration should not be committed directly to GitHub.

Use the provided:

.env.example

as a template for local configuration.

Example:

MONGODB_URI=
DATABASE_NAME=
COLLECTION_NAME=
THRESHOLD=

Never commit real database credentials, passwords, API keys, or other sensitive information to the repository.

📌 Important Notes

This project contains two implementations representing different stages of development.

Original Desktop Application
Python
Tkinter
OpenCV
Haar Cascade
LBPH Face Recognition
CSV
Modern Web Application
Next.js
React
TypeScript
Flask
MongoDB
MTCNN
DeepFace
FaceNet512

The original desktop application and the modern web application are both part of the project repository.

🔒 Privacy & Security

Face recognition systems process sensitive biometric information.

For development and demonstration purposes:

Do not upload real student personal information.
Do not upload real attendance records containing private information.
Do not upload real face images without appropriate authorization.
Do not expose database credentials.
Keep .env files out of version control.
Use .env.example to document required environment variables.
🚀 Future Improvements

Potential future improvements include:

Cloud deployment for frontend and backend.
Improved face-recognition accuracy.
Better handling of difficult lighting conditions.
Advanced anti-spoofing mechanisms.
Improved real-time recognition performance.
Advanced attendance analytics.
More detailed reporting and visualization.
Automated email and notification support.
Mobile application support.
Improved production database security.
Containerized deployment using Docker.
📚 Learning Outcomes

This project provided practical experience with:

Python programming.
Computer vision.
Face detection.
Face recognition.
Machine learning concepts.
Facial embeddings.
Cosine distance.
REST API development.
Flask.
MongoDB.
React.
Next.js.
TypeScript.
Tailwind CSS.
Authentication.
Frontend-backend integration.
Database management.
Git and GitHub.
Full-stack application development.
🎓 Project Purpose

This project was developed as an academic and practical implementation of an AI-powered attendance management system.

It demonstrates how computer vision and face recognition can be integrated with modern web technologies to build an automated attendance solution.

The project also represents the evolution of the system from a traditional desktop-based attendance application to a more feature-rich full-stack architecture.

👨‍💻 Author
Yash Agrawal

B.Tech — Computer Science & Engineering

GitHub:
https://github.com/YashAgrawal2006

⭐ Support

If you find this project useful or interesting, consider giving the repository a ⭐ on GitHub.

📄 License

This project is provided for educational and demonstration purposes.

If you intend to reuse, modify, or distribute the project, please review the repository contents and applicable third-party licenses before doing so.
