# 🤖 AI-Based Smart Attendance Management System Using Face Recognition

> An intelligent attendance management system that automates student attendance using face recognition and computer vision.

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green?logo=opencv)
![Flask](https://img.shields.io/badge/Backend-Flask-black?logo=flask)
![Next.js](https://img.shields.io/badge/Frontend-Next.js-black?logo=next.js)
![React](https://img.shields.io/badge/React-19-blue?logo=react)
![TypeScript](https://img.shields.io/badge/TypeScript-5-blue?logo=typescript)
![MongoDB](https://img.shields.io/badge/Database-MongoDB-green?logo=mongodb)
![DeepFace](https://img.shields.io/badge/AI-DeepFace-orange)

---

## 📌 Overview

The **AI-Based Smart Attendance Management System** is a face-recognition-based attendance solution developed to simplify and automate the process of recording student attendance.

The project combines **computer vision, artificial intelligence, face detection, face recognition, a Flask backend, a Next.js frontend, and MongoDB** to provide an integrated attendance management system.

The project contains both:

- 🖥️ A Python-based desktop attendance application
- 🌐 A modern web-based attendance management application

---

## 🎯 Objectives

- Automate the student attendance process.
- Reduce manual attendance work.
- Use face recognition for identifying students.
- Provide a web interface for students and teachers.
- Store attendance and student-related information systematically.
- Provide a structured backend API for the web application.
- Make attendance management easier and more efficient.

---

## ✨ Key Features

### 👤 Student Management

- Student registration
- Student profile management
- Student information updates
- Student attendance viewing
- Face image capture during registration

### 👨‍🏫 Teacher Management

- Teacher authentication
- Teacher dashboard
- Attendance session management
- Start and end attendance sessions
- Attendance record management

### 🤖 Face Recognition

- Face detection using MTCNN
- Face representation using DeepFace / FaceNet512
- Face embeddings generation
- Face matching using cosine distance
- Automatic student identification

### 📊 Attendance Management

- Attendance session creation
- Real-time attendance marking
- Duplicate attendance prevention
- Attendance records
- Attendance viewing
- Attendance export functionality

---

## 🧠 AI-Based Face Recognition

The web application uses a face-recognition pipeline based on **MTCNN** and **DeepFace with FaceNet512**.

The recognition process works approximately as follows:

```text
Camera / Image
      │
      ▼
Face Detection
      │
      ▼
MTCNN
      │
      ▼
Face Extraction
      │
      ▼
DeepFace / FaceNet512
      │
      ▼
Face Embedding
      │
      ▼
Cosine Distance Matching
      │
      ▼
Student Identification
      │
      ▼
Attendance Marked
```

The system generates a numerical face representation called an **embedding** and compares it with stored student face representations to identify the corresponding student.

---

## ⚙️ How the System Works

### Student Registration

1. Student opens the registration page.
2. Student enters the required details.
3. The system captures multiple face images.
4. Face information is processed by the recognition system.
5. Student information and recognition data are stored.

### Attendance Process

1. Teacher starts an attendance session.
2. The system accesses the required recognition functionality.
3. Student face is detected.
4. The face is converted into an embedding.
5. The embedding is compared with stored student embeddings.
6. The matching student is identified.
7. Attendance is recorded for the active session.

### Attendance Records

Attendance records can then be viewed through the application's attendance-related interfaces and can also be exported.

---

## 🏗️ System Architecture

```text
                    ┌─────────────────────────┐
                    │       Frontend          │
                    │ Next.js + React + TS    │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │       Flask API         │
                    │        Backend           │
                    └────────────┬────────────┘
                                 │
              ┌──────────────────┼──────────────────┐
              │                  │                  │
              ▼                  ▼                  ▼
       ┌─────────────┐    ┌─────────────┐   ┌──────────────┐
       │   MongoDB   │    │    MTCNN    │   │   DeepFace   │
       │   Database  │    │Face Detection│   │  FaceNet512  │
       └─────────────┘    └─────────────┘   └──────┬───────┘
                                                    │
                                                    ▼
                                             Face Embeddings
                                                    │
                                                    ▼
                                             Face Matching
                                                    │
                                                    ▼
                                             Attendance Data
```

---

## 🛠️ Technology Stack

### Frontend

- Next.js
- React
- TypeScript
- Tailwind CSS
- Framer Motion
- Lucide React
- Socket.IO Client
- XLSX

### Backend

- Python
- Flask
- MongoDB
- MTCNN
- DeepFace
- FaceNet512
- NumPy
- OpenCV

### Desktop Application

- Python
- Tkinter
- OpenCV
- Haar Cascade
- LBPH Face Recognizer
- NumPy
- Pandas
- Pillow
- CSV
- pyttsx3

---

## 🖥️ Desktop Application

The project also contains a Python-based desktop attendance application.

The desktop application provides functionality such as:

- Student registration
- Face image capture
- Face image training
- Automatic attendance
- Manual attendance
- Attendance viewing
- CSV-based attendance records

Important desktop application files include:

```text
attendance.py
automaticAttendance.py
takeImage.py
takemanually.py
trainImage.py
show_attendance.py
```

---

## 🌐 Web Application

The web application is built using **Next.js, React, and TypeScript**.

It provides separate interfaces for students and teachers.

### Student Features

```text
/signin
/signup
/student/registrationform
/student/updatedetails
/student/demo-session
/student/view-attendance
```

### Teacher Features

```text
/teacher/dashboard
/teacher/start-session
/teacher/updatedetails
```

---

## 🔌 Backend API

The Flask backend provides API endpoints for authentication, student management, teacher functionality, and attendance operations.

Important attendance-related endpoints include:

```text
POST /api/attendance/create_session
POST /api/attendance/real-mark
POST /api/attendance/end_session

GET  /api/attendance/models/status
GET  /api/attendance
GET  /api/attendance/export
```

The backend also contains authentication and student/teacher related modules.

---

## 📁 Project Structure

```text
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
```

---

## 📸 Screenshots

Screenshots and UI images from the project are available in the following directories:

```text
Project Snap/
UI_Image/
```

These folders contain screenshots and visual references of different parts of the application.

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YashAgrawal2006/AI-Based-Smart-Attendance-Management-System.git
```

```bash
cd AI-Based-Smart-Attendance-Management-System
```

---

## 🐍 Desktop Application Setup

Create and activate a Python virtual environment:

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the desktop application:

```bash
python attendance.py
```

---
## 🔐 Environment Variables

The project uses environment variables for sensitive configuration.

Create a `.env` file based on the provided example:

```text
.env.example
```

Example:

```env
MONGODB_URI=your_mongodb_connection_string_here
```

Do **not** commit real database credentials or other sensitive information to GitHub.

---

## 🔒 Privacy & Security

This project processes face-related information and student attendance data.

For security and privacy reasons:

- Real student data should not be committed to a public repository.
- Face training data should not be uploaded publicly.
- Attendance records containing personal information should remain private.
- Database credentials must never be committed to GitHub.
- Environment variables should be used for sensitive configuration.
- The `.gitignore` file excludes private and generated project data.

---

## 🔮 Future Improvements

Potential future improvements include:

- Cloud deployment
- Improved face-recognition performance
- Better camera handling
- More advanced attendance analytics
- Role-based access control
- Improved reporting and dashboards
- Mobile application support
- Additional security mechanisms
- Automated notification features
- Better scalability for larger institutions

---

## 📚 Learning Outcomes

Through this project, the following concepts were explored and implemented:

- Python development
- Computer vision
- Face detection
- Face recognition
- AI-based image processing
- Face embeddings
- Next.js development
- React
- TypeScript
- Frontend-backend integration
- Authentication
- Attendance management
- Project structure and version control
- Git and GitHub

---

## 🎯 Project Purpose

The primary purpose of this project is to demonstrate how **artificial intelligence and computer vision can be integrated with a full-stack web application to automate attendance management**.

It combines AI-based face recognition with a structured frontend, backend, and database architecture to create an end-to-end attendance management solution.

---

## 👨‍💻 Author

**Yash Agrawal**

B.Tech — Computer Science & Engineering

**GitHub:**  
https://github.com/YashAgrawal2006

---

## ⭐ Support

If you find this project useful or interesting, consider giving the repository a ⭐ on GitHub.

---

## 📄 License

This project is provided for educational and portfolio purposes.
