import cv2
import face_recognition
import numpy as np
import webbrowser
from encoded import encoded_face_train, classNames

cap = cv2.VideoCapture(0)  # Adjust 0 or 1 according to your camera input
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1024)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 768)

flag = 0
ans = []
index = 0

while True:
    index += 1
    if index == 500:  # Change according to your need
        print("Frame limit reached")
        break
    
    success, img = cap.read()
    if not success:
        print("Failed to capture image")
        break

    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
    faces_in_frame = face_recognition.face_locations(imgS)
    encoded_faces = face_recognition.face_encodings(imgS, faces_in_frame)
    
    if not encoded_faces:
        print("No faces detected")
        continue

    for encode_face, faceloc in zip(encoded_faces, faces_in_frame):
        matches = face_recognition.compare_faces(encoded_face_train, encode_face)
        faceDist = face_recognition.face_distance(encoded_face_train, encode_face)
        matchIndex = np.argmin(faceDist)
        
        print(f"Matches: {matches}")
        print(f"Face Distances: {faceDist}")
        print(f"Match Index: {matchIndex}")
        
        if matches[matchIndex]:
            ans.append(classNames[matchIndex])
            flag += 1
            print(f"Detected: {classNames[matchIndex]}")
            break
    
    if (cv2.waitKey(1) & 0xFF == ord('q')) or flag == 10:
        most_common_face = max(set(ans), key=ans.count) if ans else "No face detected"
        print(f"Exiting loop. Most common detected face: {most_common_face}")
        break

cap.release()
cv2.destroyAllWindows()
print("Resources released and windows closed. Proceeding to next step.")

# Redirect to login page
webbrowser.open("https://localhost:3000/login")
