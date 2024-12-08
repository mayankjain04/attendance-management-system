# Attendance Management System using Face Recognition

## Overview
The **Attendance Management System** is a Python-based application that uses face recognition to automate student attendance tracking. It utilizes **OpenCV** for face detection and recognition, and **Tkinter** for the graphical user interface. The system captures images for training, recognizes faces to mark attendance, and exports attendance records in CSV format.

---

## Features
- **Face Recognition**: Automatically recognizes students' faces and marks attendance.
- **Image Capture**: Capture and save student images for training the model.
- **Manual Attendance**: Option to manually log attendance.
- **CSV Export**: Attendance records can be exported as CSV files.

---

## Technologies Used
- **Python**
- **OpenCV (with OpenCV-Contrib-Python)** for face recognition
- **Tkinter** for GUI
- **NumPy** and **Pandas** for data processing

---

## Installation

1. **Clone the Repository**
    ```bash
    git clone https://github.com/mayankjain04/attendance-management-system.git
    cd attendance-management-system
    ```

2. **Install Required Packages**
    ```bash
    pip install -r requirements.txt
    ```

---

## Usage

1. **Capture Images**:
   - Run `main_Run.py` to open the GUI.
   - Enter the student's enrollment number and name.
   - Click **"Take Images"** to capture face images for training.

2. **Train the Model**:
   - After capturing images, click **"Train Images"** to train the face recognition model.

3. **Automatic Attendance**:
   - Select **"Automatic Attendance"** to begin real-time face recognition via webcam.

4. **Manual Attendance**:
   - Use **"Manually Fill Attendance"** to manually log attendance.

---

## Acknowledgments
- **OpenCV** for face detection and recognition.
- **Tkinter** for building the graphical user interface.
- **NumPy** and **Pandas** for data processing.

For any questions or issues, feel free to contact **[dm.mayankjain@gmail.com]**.

