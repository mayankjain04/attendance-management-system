import tkinter as tk
from tkinter import *
import cv2
import csv
import os
import numpy as np
from PIL import Image, ImageTk
import pandas as pd
import datetime
import time

# Main window for the Attendance Management System
window = tk.Tk()
window.title("Attendance Management System using Face Recognition")
window.geometry('1280x720')
window.configure(background='#f0f8ff')  # Light blue background for a friendly look

# Function to manually fill attendance
def manually_fill():
    global sb
    sb = tk.Tk()
    sb.title("Enter Subject Name...")
    sb.geometry('580x320')
    sb.configure(background='#f0f8ff')  # Consistent background color

    # Function to show error message for subject entry
    def err_screen_for_subject():
        def ec_delete():
            ec.destroy()
        global ec
        ec = tk.Tk()
        ec.geometry('300x100')
        ec.title('Warning!!')
        ec.configure(background='lightcoral')  # Red background for warnings
        Label(ec, text='Please enter your subject name!!!', fg='white', bg='red', font=('times', 16, 'bold')).pack()
        Button(ec, text='OK', command=ec_delete, fg="black", bg="lightgreen", width=9, height=1, activebackground="Red", font=('times', 15, 'bold')).place(x=90, y=50)

    # Function to fill attendance
    def fill_attendance():
        ts = time.time()
        Date = datetime.datetime.fromtimestamp(ts).strftime('%Y_%m_%d')
        timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
        Hour, Minute, Second = timeStamp.split(":")

        # Create a CSV file for attendance
        global subb
        subb = SUB_ENTRY.get()
        DB_table_name = str(subb + "_" + Date + "_Time_" + Hour + "_" + Minute + "_" + Second)

        # Check if subject name is provided
        if subb == '':
            err_screen_for_subject()
        else:
            sb.destroy()
            MFW = tk.Tk()
            MFW.title("Manually Attendance of " + str(subb))
            MFW.geometry('880x470')
            MFW.configure(background='#f0f8ff')  # Consistent background color

            # Function to show error message for student entry
            def err_screen1():
                global errsc2
                errsc2 = tk.Tk()
                errsc2.geometry('330x100')
                errsc2.title('Warning!!')
                errsc2.configure(background='lightcoral')  # Red background for warnings
                Label(errsc2, text='Please enter Student & Enrollment!!!', fg='white', bg='red', font=('times', 16, 'bold')).pack()
                Button(errsc2, text='OK', command=lambda: errsc2.destroy(), fg="black", bg="lightgreen", width=9, height=1, activebackground="Red", font=('times', 15, 'bold')).place(x=90, y=50)

            # Labels and Entry fields for enrollment and student name
            ENR = tk.Label(MFW, text="Enter Enrollment", width=15, height=2, fg="black", bg="#add8e6", font=('times', 15))
            ENR.place(x=30, y=100)

            STU_NAME = tk.Label(MFW, text="Enter Student Name", width=15, height=2, fg="black", bg="#add8e6", font=('times', 15))
            STU_NAME.place(x=30, y=200)

            global ENR_ENTRY
            ENR_ENTRY = tk.Entry(MFW, width=20, bg="white", fg="black", font=('times', 23))
            ENR_ENTRY.place(x=290, y=105)

            STUDENT_ENTRY = tk.Entry(MFW, width=20, bg="white", fg="black", font=('times', 23))
            STUDENT_ENTRY.place(x=290, y=205)

            # Function to enter data into CSV
            def enter_data_DB():
                ENROLLMENT = ENR_ENTRY.get()
                STUDENT = STUDENT_ENTRY.get()
                if ENROLLMENT == '' or STUDENT == '':
                    err_screen1()
                else:
                    time = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                    Insert_data = "INSERT INTO " + DB_table_name + " (ENROLLMENT, NAME, DATE, TIME) VALUES (%s, %s, %s, %s)"
                    VALUES = (str(ENROLLMENT), str(STUDENT), str(Date), str(time))
                    with open(DB_table_name + '.csv', 'a+', newline='') as csvFile:
                        writer = csv.writer(csvFile)
                        writer.writerow(VALUES)  # Write the attendance data to CSV
                    ENR_ENTRY.delete(0, tk.END)  # Clear the enrollment entry
                    STUDENT_ENTRY.delete(0, tk.END)  # Clear the student name entry

            # Function to create CSV file
            def create_csv():
                csv_name = './Attendance/' + DB_table_name + '.csv'
                with open(csv_name, "w", newline='') as csv_file:
                    csv_writer = csv.writer(csv_file)
                    csv_writer.writerow(['ENROLLMENT', 'NAME', 'DATE', 'TIME'])  # Write headers
                    csv_writer.writerow([ENR_ENTRY.get(), STUDENT_ENTRY.get(), Date, timeStamp])  # Write the attendance data
                    Notification.configure(text="CSV created Successfully", bg="green", fg="white", width=33, font=('times', 19, 'bold'))
                    Notification.place(x=180, y=380)

            # Notification label for CSV creation
            Notification = tk.Label(MFW, text="", bg="green", fg="white", width=33, height=2, font=('times', 19, 'bold'))

            # Buttons for data entry and CSV creation
            DATA_SUB = tk.Button(MFW, text="Enter Data", command=enter_data_DB, fg="black", bg="skyblue", width=20, height=2, activebackground="white", font=('times', 15, 'bold'))
            DATA_SUB.place(x=170, y=300)

            MAKE_CSV = tk.Button(MFW, text="Convert to CSV", command=create_csv, fg="black", bg="skyblue", width=20, height=2, activebackground="white", font=('times', 15, 'bold'))
            MAKE_CSV.place(x=570, y=300)

            MFW.mainloop()

    # Label and Entry for subject name
    SUB = tk.Label(sb, text="Enter Subject: ", width=15, height=2, fg="black", bg="#add8e6", font=('times', 15, 'bold'))
    SUB.place(x=30, y=100)

    global SUB_ENTRY
    SUB_ENTRY = tk.Entry(sb, width=20, bg="white", fg="black", font=('times', 23))
    SUB_ENTRY.place(x=250, y=105)

    fill_manual_attendance = tk.Button(sb, text="Fill Attendance", command=fill_attendance, fg="black", bg="skyblue", width=20, height=2, activebackground="white", font=('times', 15, 'bold'))
    fill_manual_attendance.place(x=250, y=160)
    sb.mainloop()

# Function to clear textboxes
def clear():
    txt.delete(0, tk.END)

def clear1():
    txt2.delete(0, tk.END)

# Function to show error message for enrollment and name
def err_screen():
    global sc1
    sc1 = tk.Tk()
    sc1.geometry('300x100')
    sc1.title('Warning!!')
    sc1.configure(background='lightcoral')  # Red background for warnings
    Label(sc1, text='Enrollment & Name required!!!', fg='white', bg='red', font=('times', 16)).pack()
    Button(sc1, text='OK', command=lambda: sc1.destroy(), fg="black", bg="lightgreen", width=9, height=1, activebackground="Red", font=('times', 15, 'bold')).place(x=90, y=50)

# Function to take images for datasets
def take_img():
    l1 = txt.get()
    l2 = txt2.get()
    if l1 == '' or l2 == '':
        err_screen()
    else:
        try:
            cam = cv2.VideoCapture(0)
            detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
            Enrollment = txt.get()
            Name = txt2.get()
            sampleNum = 0
            while True:
                ret, img = cam.read()
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = detector.detectMultiScale(gray, 1.3, 5)
                for (x, y, w, h) in faces:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    sampleNum += 1
                    cv2.imwrite("TrainingImage/" + Name + "." + Enrollment + '.' + str(sampleNum) + ".jpg", gray)
                    print(f"Image saved for Enrollment: {Enrollment} Name: {Name}, Sample Number: {sampleNum}")
                    cv2.imshow('Frame', img)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
                elif sampleNum > 70:
                    break

            cam.release()
            cv2.destroyAllWindows()
            ts = time.time()
            Date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
            Time = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
            row = [Enrollment, Name, Date, Time]
            with open('StudentDetails/StudentDetails.csv', 'a+', newline='') as csvFile:
                writer = csv.writer(csvFile, delimiter=',')
                writer.writerow(row)
                print(f"Student details saved: Enrollment: {Enrollment}, Name: {Name}, Date: {Date}, Time: {Time}")
            Notification.configure(text=f"Images saved for Enrollment: {Enrollment}, Name: {Name}", bg="SpringGreen3", width=50, font=('times', 18, 'bold'))
            Notification.place(x=250, y=400)
        except FileExistsError as F:
            Notification.configure(text='Student Data already exists', bg="Red", width=21)
            Notification.place(x=450, y=400)

# Function to choose subject and fill attendance
def subjectchoose():
    def Fillattendances():
        sub = tx.get()
        now = time.time()  # For calculate seconds of video
        future = now + 5
        if time.time() < future:
            if sub == '':
                err_screen1()
            else:
                recognizer = cv2.face.LBPHFaceRecognizer_create()
                try:
                    recognizer.read("TrainingImageLabel/Trainer.yml")
                except:
                    e = 'Model not found,Please train model'
                    Notifica.configure(
                        text=e, bg="red", fg="black", width=33, font=('times', 15, 'bold'))
                    Notifica.place(x=20, y=250)

                faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                df = pd.read_csv("StudentDetails/StudentDetails.csv")
                cam = cv2.VideoCapture(0)
                font = cv2.FONT_HERSHEY_SIMPLEX
                col_names = ['Enrollment', 'Name', 'Date', 'Time']
                attendance = pd.DataFrame(columns=col_names)
                while True:
                    ret, im = cam.read()
                    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
                    faces = faceCascade.detectMultiScale(gray, 1.2, 5)
                    for (x, y, w, h) in faces:
                        global Id

                        Id, conf = recognizer.predict(gray[y:y + h, x:x + w])
                        if conf < 70:
                            print(conf)
                            Subject = tx.get()
                            ts = time.time()
                            date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                            timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                            aa = df.loc[df['Enrollment'] == Id]['Name'].values
                            attendance.loc[len(attendance)] = [Id, aa, date, timeStamp]
                            cv2.rectangle(im, (x, y), (x + w, y + h), (0, 260, 0), 7)
                            cv2.putText(im, str(Id) + "-" + str(aa), (x + h, y), font, 1, (255, 255, 0), 4)
                        else:
                            Id = 'Unknown'
                            cv2.rectangle(im, (x, y), (x + w, y + h), (0, 25, 255), 7)
                            cv2.putText(im, str(Id), (x + h, y), font, 1, (0, 25, 255), 4)
                    if time.time() > future:
                        break

                    attendance = attendance.drop_duplicates(['Enrollment'], keep='first')
                    cv2.imshow('Filling Attendance...', im)
                    if cv2.waitKey(30) & 0xff == 27:
                        break

                # Save attendance to CSV
                ts = time.time()
                date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                fileName = "Attendance/" + Subject + "_" + date + "_" + timeStamp.replace(":", "-") + ".csv"
                attendance = attendance.drop_duplicates(['Enrollment'], keep='first') # idk why but if you dont drop duplicates again it saves attendance twice
                attendance.to_csv(fileName, index=False)
                print(f"Attendance saved to {fileName} at {timeStamp}")

                Notifica.configure(text='Attendance filled successfully', bg="green", fg="white", width=33, font=('times', 15, 'bold'))
                Notifica.place(x=20, y=250)

                cam.release()
                cv2.destroyAllWindows()

    # Window for subject chooser
    windo = tk.Tk()
    windo.title("Enter Subject Name...")
    windo.geometry('580x320')
    windo.configure(background='#f0f8ff')  # Light blue background for a friendly look
    Notifica = tk.Label(windo, text="Attendance filled Successfully", bg="green", fg="white", width=33, height=2, font=('times', 15, 'bold'))

    sub = tk.Label(windo, text="Enter Subject: ", width=15, height=2, fg="black", bg="#add8e6", font=('times', 15, 'bold'))
    sub.place(x=30, y=100)

    tx = tk.Entry(windo, width=20, bg="white", fg="black", font=('times', 23))
    tx.place(x=250, y=105)

    fill_a = tk.Button(windo, text="Fill Attendance", fg="white", command=Fillattendances, bg="skyblue", width=20, height=2, activebackground="white", font=('times', 15, 'bold'))
    fill_a.place(x=250, y=160)
    windo.mainloop()

# Function for admin panel
def admin_panel():
    win = tk.Tk()
    win.title("LogIn")
    win.geometry('880x420')
    win.configure(background='#f0f8ff')  # Light blue background for a friendly look

    def log_in():
        username = un_entr.get()
        password = pw_entr.get()

        if username == 'admin' and password == 'admin123':
            win.destroy()
            root = tk.Tk()
            root.title("Student Details")
            root.configure(background='#f0f8ff')  # Light blue background for a friendly look

            cs = './StudentDetails/StudentDetails.csv'
            with open(cs, newline="") as file:
                reader = csv.reader(file)
                r = 0
                for col in reader:
                    c = 0
                    for row in col:
                        label = tk.Label(root, width=10, height=1, fg="black", font=('times', 15, 'bold'), bg="white", text=row, relief=tk.RIDGE)
                        label.grid(row=r, column=c)
                        c += 1
                    r += 1
            root.mainloop()
        else:
            Nt.configure(text='Incorrect ID or Password', bg="red", fg="white", width=38, font=('times', 19, 'bold'))
            Nt.place(x=120, y=350)

    Nt = tk.Label(win, text="", bg="green", fg="white", width=40, height=2, font=('times', 19, 'bold'))

    un = tk.Label(win, text="Enter Username: ", width=15, height=2, fg="black", bg="#add8e6", font=('times', 15, 'bold'))
    un.place(x=30, y=50)

    pw = tk.Label(win, text="Enter Password: ", width=15, height=2, fg="black", bg="#add8e6", font=('times', 15, 'bold'))
    pw.place(x=30, y=150)

    un_entr = tk.Entry(win, width=20, bg="white", fg="black", font=('times', 23))
    un_entr.place(x=290, y=55)

    pw_entr = tk.Entry(win, width=20, show="*", bg="white", fg="black", font=('times', 23))
    pw_entr.place(x=290, y=155)

    c0 = tk.Button(win, text="Clear", command=lambda: un_entr.delete(0, tk.END), fg="white", bg="black", width=10, height=1, activebackground="white", font=('times', 15, 'bold'))
    c0.place(x=690, y=55)

    c1 = tk.Button(win, text="Clear", command=lambda: pw_entr.delete(0, tk.END), fg="white", bg="black", width=10, height=1, activebackground="white", font=('times', 15, 'bold'))
    c1.place(x=690, y=155)

    Login = tk.Button(win, text="LogIn", fg="black", bg="skyblue", width=20, height=2, activebackground="Red", command=log_in, font=('times', 15, 'bold'))
    Login.place(x=290, y=250)
    win.mainloop()

# Function to train the model
def trainimg():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    global detector
    detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    try:
        global faces, Id
        faces, Id = getImagesAndLabels("TrainingImage")
    except Exception as e:
        Notification.configure(text='Please make "TrainingImage" folder & put Images', bg="SpringGreen3", width=50, font=('times', 18, 'bold'))
        Notification.place(x=350, y=400)

    recognizer.train(faces, np.array(Id))
    try:
        recognizer.save("TrainingImageLabel/Trainer.yml")
    except Exception as e:
        Notification.configure(text='Please make "TrainingImageLabel" folder', bg="SpringGreen3", width=50, font=('times', 18, 'bold'))
        Notification.place(x=350, y=400)

    Notification.configure(text="Model Trained Successfully", bg="olive drab", width=50, font=('times', 18, 'bold'))
    Notification.place(x=250, y=400)

# Function to get images and labels for training
def getImagesAndLabels(path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    faceSamples = []
    Ids = []
    for imagePath in imagePaths:
        pilImage = Image.open(imagePath).convert('L')
        imageNp = np.array(pilImage, 'uint8')
        Id = int(os.path.split(imagePath)[-1].split(".")[1])
        faces = detector.detectMultiScale(imageNp)
        for (x, y, w, h) in faces:
            faceSamples.append(imageNp[y:y + h, x:x + w])
            Ids.append(Id)
    return faceSamples, Ids

# Configure the main window's grid
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

# Function to handle window closing
def on_closing():
    from tkinter import messagebox
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        window.destroy()

window.protocol("WM_DELETE_WINDOW", on_closing)

# Main message label
message = tk.Label(window, text="Attendance Management System using Face Recognition", bg="black", fg="white", width=50, height=3, font=('times', 30, 'bold'))
message.place(x=80, y=20)

# Notification label for general messages
Notification = tk.Label(window, text="All things good", bg="green", fg="white", width=15, height=3, font=('times', 17))

# Label and Entry for enrollment
lbl = tk.Label(window, text="Enter Enrollment: ", width=20, height=2, fg="black", bg="#add8e6", font=('times', 15, 'bold'))
lbl.place(x=200, y=200)

def testVal(inStr, acttyp):
    if acttyp == '1':  # insert
        if not inStr.isdigit():
            return False
    return True

txt = tk.Entry(window, validate="key", width=20, bg="white", fg="black", font=('times', 25))
txt['validatecommand'] = (txt.register(testVal), '%P', '%d')
txt.place(x=550, y=210)

# Label and Entry for student name
lbl2 = tk.Label(window, text="Enter Name: ", width=20, fg="black", bg="#add8e6", height=2, font=('times', 15, 'bold'))
lbl2.place(x=200, y=300)

txt2 = tk.Entry(window, width=20, bg="white", fg="black", font=('times', 25))
txt2.place(x=550, y=310)

# Clear buttons for text entries
clearButton = tk.Button(window, text="Clear", command=clear, fg="white", bg="black", width=10, height=1, activebackground="white", font=('times', 15, 'bold'))
clearButton.place(x=950, y=210)

clearButton1 = tk.Button(window, text="Clear", command=clear1, fg="white", bg="black", width=10, height=1, activebackground="white", font=('times', 15, 'bold'))
clearButton1.place(x=950, y=310)

# Button to access admin panel
AP = tk.Button(window, text="Check Registered Students", command=admin_panel, fg="black", bg="skyblue", width=19, height=1, activebackground="white", font=('times', 15, 'bold'))
AP.place(x=990, y=410)

# Button to take images for training
takeImg = tk.Button(window, text="Take Images", command=take_img, fg="black", bg="skyblue", width=20, height=3, activebackground="white", font=('times', 15, 'bold'))
takeImg.place(x=90, y=500)

# Button to train the model
trainImg = tk.Button(window, text="Train Images", fg="black", command=trainimg, bg="skyblue", width=20, height=3, activebackground="white", font=('times', 15, 'bold'))
trainImg.place(x=390, y=500)

# Button for automatic attendance
FA = tk.Button(window, text="Automatic Attendance", fg="black", command=subjectchoose, bg="skyblue", width=20, height=3, activebackground="white", font=('times', 15, 'bold'))
FA.place(x=690, y=500)

# Button to manually fill attendance
quitWindow = tk.Button(window, text="Manually Fill Attendance", command=manually_fill, fg="black", bg="skyblue", width=20, height=3, activebackground="white", font=('times', 15, 'bold'))
quitWindow.place(x=990, y=500)

# Start the main loop of the application
window.mainloop()