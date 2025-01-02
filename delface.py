import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

# Path to the folder containing images for attendance
path = 'ImageAttendance'
images = []
classNames = []
myList = os.listdir(path)
print(f"Images found in directory: {myList}")

# Load the images and their corresponding class names
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    if curImg is not None:
        images.append(curImg)
        classNames.append(os.path.splitext(cl)[0])  # Remove the file extension for the class name
    else:
        print(f"Warning: {cl} could not be loaded.")

print(f"Class names: {classNames}")

# Function to find face encodings for a list of images
def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encodings = face_recognition.face_encodings(img)
        if len(encodings) > 0:
            encodeList.append(encodings[0])
        else:
            print("No face found in one of the images, skipping this image.")
    return encodeList

# Function to mark attendance by writing the recognized name into a CSV file
def markAttendance(name):
    with open('Attendance.csv', 'a+', encoding='ISO-8859-1') as f:
        myDataList = f.readlines()
        nameList = [entry.split(',')[0] for entry in myDataList]
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtString}')
            print(f"{name} marked at {dtString}")

# Find encodings for the known images
encodeListKnown = findEncodings(images)
print('Encoding Complete')

# Capture video from the webcam
cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    if not success or img is None:
        print("Failed to capture image from webcam.")
        break

    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    # Debugging output for the image shape
    print(f"Captured image shape: {imgS.shape}")

    if imgS.shape[2] == 3:  # Check for RGB
        facesCurFrame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)
        
        for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)

            if len(faceDis) > 0:
                matchIndex = np.argmin(faceDis)

                if faceDis[matchIndex] < 0.50:  # Face is recognized
                    name = classNames[matchIndex].upper()
                else:
                    name = 'Unknown'

                markAttendance(name)

                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = [val * 4 for val in (y1, x2, y2, x1)]
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
    else:
        print("Invalid image shape for face detection.")

    cv2.imshow('Webcam', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()